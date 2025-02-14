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
            class="w-full"
            style="width: 435px;"
          />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <InputText 
            v-model="email" 
            placeholder="Informe seu email"
            class="w-full"
            style="width: 435px;"
          />
        </div>
  
        <div class="form-group">
          <label>Senha:</label>
          <Password 
            v-model="password" 
            placeholder="Informe a senha"
            :feedback="false"
            toggleMask
            class="w-full"
          />
        </div>

        <div class="form-group">
          <label>Senha:</label>
          <Password 
            v-model="password" 
            placeholder="Confirme sua senha"
            :feedback="false"
            toggleMask
            class="w-full"
          />
        </div>
  
        <div class="forgot-password">
          <a href="#">Esqueceu a senha?</a>
        </div>
  
        <Button 
          label="ENTRAR" 
          class="login-button"
          @click="handleLogin"
        />
  
        <div class="register-link">
          <a href="#">Cadastrar-se</a>
        </div>
      </div>
    </div>
  </template>
  
  <script >
  import { ref } from 'vue'
  import InputText from 'primevue/inputtext';
  import Password from 'primevue/password';
  import Button from 'primevue/button';   
  const personType = ref('fisica')
  const email = ref('')
  const password = ref('')
  
  const handleLogin = () => {
    // Implementar lógica de login aqui
    console.log('Login attempt:', {
      personType: personType.value,
      username: username.value,
      password: password.value
    })
  }
  </script>
  
  <style scoped>
  .login-container {
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
    padding-top: 60px; /* Espaço para o avatar */
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
  
  :deep(.p-password) {
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

/* Para garantir que os inputs tenham a mesma largura */
:deep(.p-inputtext input) {
  width: 100%;
}

@media (max-width: 480px) {
  .login-card {
    padding: 1.5rem;
    padding-top: 60px; /* Mantém o espaço para o avatar em telas menores */
    margin-top: 40px; /* Adiciona margem para o avatar não ficar cortado */
  }
  
   .person-type {
      flex-direction: column;
      gap: 0.5rem;
      align-items: flex-start;
    }
  }
  </style>
