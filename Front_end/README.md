# Maceió IN Front

[![Versão](https://img.shields.io/badge/version-0.0.0-green.svg)](https://github.com/seu-usuario/maceio_in_front)

O **Maceió IN Front** é um projeto front-end desenvolvido com Vue 3, PrimeVue e Bootstrap. Ele oferece uma interface moderna e responsiva para gerenciamento de autenticação de usuários e listagem de funcionários.

## 🛠️ Tecnologias Utilizadas

<div align="left">
  <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" alt="Vue.js" />
  <img src="https://img.shields.io/badge/PrimeVue-1976D2?style=for-the-badge&logo=vue.js&logoColor=white" alt="PrimeVue" />
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E" alt="Vite" />
  <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white" alt="Axios" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
</div>

## 🚀 Começando

Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

### 📋 Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- [Node.js](https://nodejs.org/) (v18 ou superior)
- [npm](https://www.npmjs.com/) ou [Yarn](https://yarnpkg.com/) (gerenciador de pacotes)

### 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/maceio_in_front.git
```
2. Navegue até a pasta do projeto:

````bash

cd maceio_in_front
````
3. Instale as dependências:

```bash

npm install
```
4. Execute o projeto em modo de desenvolvimento:

```bash

npm run dev
```
O projeto estará disponível em http://localhost:5173.

### 🗂️ Estrutura do Projeto
Aqui está uma visão geral da estrutura do projeto:

```Copy
maceio_in_front/
├── .vscode/
│   └── extensions.json
├── src/
│   ├── assets/
│   │   ├── logoNova.png
│   │   ├── logo_prefeitura_de_maceio.svg
│   │   └── maceio_topo.svg
│   ├── components/
│   │   ├── DataTable.vue
│   │   ├── Footer.vue
│   │   ├── Form.vue
│   │   ├── FormSignUp.vue
│   │   ├── Header.vue
│   ├── composables/
│   │   └── useAuth.js
│   ├── pages/
│   │   ├── EmployeeList.vue
│   │   ├── SignIn.vue
│   │   └── SignUp.vue
│   ├── router/
│   │   └── index.js
│   ├── App.vue
│   ├── axios.js
│   └── main.js
├── .gitignore
├── README.md
├── index.html
├── jsconfig.json
├── package-lock.json
├── package.json
└── vite.config.js
```
### 🧩 Funcionalidades

Autenticação de Usuários:

- Login (SignIn.vue).

- Registro (SignUp.vue).

- Listagem de Funcionários:

- Tabela de funcionários com PrimeVue DataTable (EmployeeList.vue).

- Roteamento:

- Proteção de rotas autenticadas (router/index.js).

### 🛡️ Proteção de Rotas
O projeto utiliza o Vue Router para proteger rotas que exigem autenticação. A função isAuthenticated verifica se o usuário possui um token válido no localStorage. Caso contrário, o usuário é redirecionado para a página de login.

javascript
```Copy
const isAuthenticated = () => {
  return localStorage.getItem('token') !== null;
};
```



### 📧 Contato
- **LinkedIn :** https://www.linkedin.com/in/ivan-martins-alves/?locale=pt_BR
- **E-mail :** Ivanmarti.alves@gmail.com
- **Link do Projeto :** https://github.com/IvanM4rtin5/Maceio_IN/
