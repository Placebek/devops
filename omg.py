from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn # type: ignore
import os
from app.services import TextExtractorService, TTSService

app = FastAPI(title="Talk To Docs API", version="1.0.0")

# Настройка CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене укажи конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Добавляем статические файлы для аудио
app.mount("/static", StaticFiles(directory="audio_files"), name="static")

# Инициализируем сервисы
text_extractor = TextExtractorService()
tts_service = TTSService()

app = FastAPI(title="Talk To Docs API", version="1.0.0")

# Настройка CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене укажи конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализируем сервисы
text_extractor = TextExtractorService()
tts_service = TTSService()

@app.get("/")
async def root():
    return {"message": "Talk To Docs API is running!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Проверяем тип файла
        if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/plain"]:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        # Читаем файл
        content = await file.read()
        
        # Извлекаем текст
        extracted_text = text_extractor.extract_text(content, file.content_type)
        
        # Базовый анализ
        word_count = len(extracted_text.split())
        char_count = len(extracted_text)
        
        return {
            "filename": file.filename,
            "text": extracted_text[:1000] + "..." if len(extracted_text) > 1000 else extracted_text,
            "full_text": extracted_text,
            "stats": {
                "word_count": word_count,
                "char_count": char_count
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/text-to-speech")
async def convert_to_speech(request: dict):
    try:
        text = request.get("text", "")
        language = request.get("language", "ru")  # По умолчанию русский
        
        if not text:
            raise HTTPException(status_code=400, detail="Text is required")
        
        # Генерируем аудио
        audio_file = tts_service.generate_speech(text, language)
        
        return {"audio_file": audio_file, "message": "Speech generated successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

from fastapi import FastAPI, UploadFile, File, HTTPException