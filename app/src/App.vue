<script>
import api from '@/stores/api'
import axios from 'axios';
export default {
  data() {
    return {
      libraries: [],
      loading: false,
      error: ''
    }
  },
  mounted() {
    this.fetchLibraries()
  },
  methods: {
    async fetchLibraries() {
      this.loading = true
      this.error = ''
      try {
        const response = await axios.get('http://localhost:8000/library')
        this.libraries = response.data
      } catch (err) {
        this.error = 'Ошибка загрузки'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<template>
  <div>
    <h3>Список библиотек:</h3>
    <ul>
      <li v-for="library in libraries" :key="library.id">{{ library.name }} - {{ library.author }}</li>
    </ul>
  </div>
</template>

<style scoped></style>
