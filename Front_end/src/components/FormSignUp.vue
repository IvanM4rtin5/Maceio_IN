<template>
    <div class="login-container">
      <div class="login-card">
        <div class="avatar-container">
          <div class="avatar">
            <i class="pi pi-user"></i>
          </div>
        </div>
        
        <h2>Crie sua conta</h2>
  
        <div class="form-group">
          <label>Usuário:</label>
          <InputText
            v-model="nome" 
            placeholder="Informe seu nome"
            class="w-full sm:w-[435px]"
          />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <InputText 
            v-model="email" 
            placeholder="Informe seu email"
            class="w-full sm:w-[435px]"
          />
        </div>
  
        <div class="form-group">
          <label>Senha:</label>
          <Password 
            v-model="password" 
            placeholder="Informe a senha"
            :feedback="false"
            toggleMask
            class="w-full sm:w-[435px]"
          />
        </div>

        <div class="form-group">
          <label>Senha:</label>
          <Password 
            v-model="confPassword" 
            placeholder="Confirme sua senha"
            :feedback="false"
            toggleMask
            class="w-full  sm:w-[435px]"
          />
        </div>
  
        <Button 
          label="Criar conta" 
          class="login-button"
          @click="handleSignUp"
          :loading="loading"
        />
  
        <div class="register-link">
          <span style="color: #345B7C; font-size: 16px; font-weight: bold;">Já possui uma conta?</span>
          <p style="padding-top: 20px;">
            <a href="/signin">Login</a>
          </p>
        </div>
      </div>
    </div>
  </template>

<script setup>
  import Button from 'primevue/button';
  import api from '@/axios';
  import { ref } from 'vue'; 
  import { useToast } from 'primevue/usetoast';
  import { useRouter } from 'vue-router';
  
  const toast = useToast();
  const router = useRouter();
  const nome = ref('');
  const email = ref('');
  const password = ref('');
  const confPassword = ref('');
  const loading = ref(false);
  
  const handleSignUp = async () => {
    if (!nome.value || !email.value || !password.value || !confPassword.value) {
      toast.add({ 
        severity: 'error', 
        summary: 'Erro', 
        detail: 'Por favor, preencha todos os campos', 
        life: 3000 
      });
      return;
    }
  
    if (password.value !== confPassword.value) {
      toast.add({ 
        severity: 'error', 
        summary: 'Erro', 
        detail: 'As senhas não coincidem.', 
        life: 3000 
      });
      return;
    }
  
    loading.value = true;
  try {
    const response = await api.post('/api/register/', {
      nome: nome.value,
      email: email.value,
      password: password.value
    });
  
    if (response.status === 201) {
      toast.add({ 
        severity: 'success', 
        summary: 'Sucesso', 
        detail: 'Cadastro realizado! Redirecionando...', 
        life: 3000 
      });
      router.push('/signin');
    } else {
      console.error('Erro ao cadastrar:', response);
    }
  } catch (error) {
    console.error('Erro ao cadastrar:', error);
  }
  
    loading.value = false;
  };
</script>
    
  
  <style scoped>
  .login-container {
    font-family: sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #0088cc;
    padding: 7rem;
  }

  .avatar-container {
  position: absolute;
  margin: -100px 0;
  left: 50%;
  transform: translateX(-50%);
  }
  .avatar {
  width: 80px;
  height: 80px;
  background-color: #345B7C;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.avatar i {
  font-size: 2.5rem;
  color: white;
}
  
  .login-card {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    width: 100%;
    max-width: 500px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    position: relative;
    padding-top: 60px; 
  }
  
  h2 {
    text-align: center;
    color: #345B7C;
    margin-bottom: 1.5rem;
  }
  
  .person-type {
    display: flex;
    gap: 2rem;
    justify-content: center;
    margin-bottom: 1.5rem;
  }
  
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #333;
  }
  
  :deep(.p-inputtext), :deep(.p-password) {
  width: 100%;
  }
  
  :deep(.p-password-input) {
    width: 100%;
  }
  
  .forgot-password {
    text-align: left;
    margin-bottom: 1.5rem;
  }
  
  .forgot-password a {
    color: #0088cc;
    text-decoration: none;
  }
  
  .login-button {
    width: 100%;
    background-color: #345B7C !important;
    border: none;
    padding: 0.75rem !important;
    font-weight: bold;
  }
  
  .register-link {
    text-align: center;
    margin-top: 1rem;
  }
  
  .register-link a {
    color: #0088cc;
    text-decoration: none;
  }
  :deep(.p-password) {
  width: 100%;
  display: block;
}

:deep(.p-password input) {
  width: 100%;
}

:deep(.p-inputtext input) {
  width: 100%;
}

@media (max-width: 680px) {
  .login-card {
    padding: 1.5rem;
    padding-top: 60px; 
    margin-top: 40px; 
  }
  
   .person-type {
      flex-direction: column;
      gap: 0.5rem;
      align-items: flex-start;
    }
  }
  </style>
