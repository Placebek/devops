from sqlalchemy import Column, Integer, String
from db.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, nullable=False)