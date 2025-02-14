# Maceio In - API Backend

## Descrição
API backend desenvolvida em Django para gerenciar dados de funcionários e autenticação de usuários. A API permite registrar, autenticar e gerenciar usuários, bem como acessar dados dos funcionários.

## Requisitos
- Python 3.x
- Django 5.1.5
- Django Rest Framework
- SQLite (ou outro banco de dados de sua escolha)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/maceio_in.git
    ```

2. Navegue para o diretório do projeto:
    ```bash
    cd maceio_in
    ```

3. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Faça as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

7. Acesse a API na URL:
    ```bash
    http://localhost:8000
    ```

## Endpoints

### Registro de Usuário

**POST** `/api/register/`  
Registro de um novo usuário com nome, e-mail e senha. Retorna o token de autenticação.

### Login de Usuário

**POST** `/api/login/`  
Login de usuário com e-mail e senha. Retorna um token de autenticação.

### Funcionários

**GET** `/api/funcionarios/`  
Retorna uma lista de todos os funcionários.  
**POST** `/api/funcionarios/`  
Cria um novo funcionário.
**PUT** `/api/funcionarios/id/`  
Para Att funcionário.
**DELETE** `/api/funcionarios/id/`  
Deleta o funcionário.

## Dependências

- Django==5.1.5
- djangorestframework
- djangorestframework-authtoken
- corsheaders
