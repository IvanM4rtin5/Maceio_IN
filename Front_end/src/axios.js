import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // URL do seu backend Django
});

// Adiciona o token no header das requisições, se existir
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

export default api;