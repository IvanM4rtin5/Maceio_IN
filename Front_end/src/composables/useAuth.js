import { ref } from 'vue';
import api from '../axios';
import { useRouter } from 'vue-router';

export function useAuth() {
  const isAuthenticated = ref(localStorage.getItem('token') !== null);
  const router = useRouter();

  const login = async (email, password) => {
    try {
      const response = await api.post('/login/', { email, password });
      const token = response.data.token;
      localStorage.setItem('token', token);
      isAuthenticated.value = true;
      router.push({ name: 'employees' });
    } catch (error) {
      console.error('Erro ao fazer login:', error);
      throw error;
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    isAuthenticated.value = false;
    router.push({ name: 'signin' });
  };

  return {
    isAuthenticated,
    login,
    logout,
  };
}