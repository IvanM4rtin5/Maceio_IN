<template>
  <div>
    <Header />
  </div>
  <div>
    <!-- Lista de funcionários com DataTable -->
    <div class="card" >
      <h3 style="text-align: center;">Funcionarios Cadastrados</h3>
      <DataTable :value="employees" showGridlines tableStyle="min-width: 50rem">
        <Column field="nome" header="Nome"></Column>
        <Column field="email" header="Email"></Column>
        <Column field="setor" header="Setor"></Column>
        <Column header="Ações">
          <template #body="slotProps">
            <Button
              icon="pi pi-pencil"
              class="p-button-rounded p-button-success p-button-text"
              @click="editEmployee(slotProps.data)"
            />
            <Button
              icon="pi pi-trash"
              class="p-button-rounded p-button-danger p-button-text"
              @click="deleteEmployee(slotProps.data.id)"
            />
          </template>
        </Column>
        <template #empty>
          <p>Nenhum funcionário cadastrado.</p>
        </template>
      </DataTable>
    </div>
        <!-- Formulário para criar/editar funcionários com PrimeVue -->
      <div class="form-section" style="margin-top: 50px;">
      <h2>{{ isEditing ? 'Editar Funcionário' : 'Criar Novo Funcionário' }}</h2>
      <form @submit.prevent="handleSubmit">
        <div class="p-fluid">
          <!-- Campo Nome -->
          <div class="p-field">
            <label for="nome">Nome</label>
            <InputText
              id="nome"
              v-model="form.nome"
              placeholder="Digite o nome"
              required
            />
          </div>

          <!-- Campo Email -->
          <div class="p-field">
            <label for="email">Email</label>
            <InputText
              id="email"
              v-model="form.email"
              placeholder="Digite o email"
              type="email"
              required
            />
          </div>

          <!-- Campo Setor -->
          <div class="p-field">
            <label for="setor">Setor</label>
            <InputText
              id="setor"
              v-model="form.setor"
              placeholder="Digite o setor"
              required
            />
          </div>

          <!-- Botões de ação -->
          <div class="p-field">
            <Button
              type="submit"
              :label="isEditing ? 'Atualizar' : 'Criar'"
              class="p-button-primary"
            />
            <Button
              v-if="isEditing"
              type="button"
              label="Cancelar"
              class="p-button-secondary"
              @click="cancelEdit"
            />
          </div>
        </div>
      </form>
    </div>
    <div class="description-section">
      <p> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tenetur cum corporis facere. Quibusdam delectus fuga tenetur reprehenderit eligendi qui excepturi recusandae? Deleniti dolorem voluptatum eum possimus saepe veniam magnam tempore!</p>
    </div>

     <!-- Formulário do PrimeVue -->
     <div class="form-section" style="margin: 50px auto;">
      <h2>Entre em Contato</h2>
      <form @submit.prevent="handleSubmit">
        <div class="p-fluid">
          <div class="p-field">
            <label for="name">Nome</label>
            <InputText id="name" v-model="form.name" placeholder="Seu nome" required />
          </div>
          <div class="p-field">
            <label for="email">Email</label>
            <InputText id="email" v-model="form.email" placeholder="Seu email" type="email" required />
          </div>
          <div class="p-field">
            <label for="message">Mensagem</label>
            <Textarea id="message" v-model="form.message" placeholder="Sua mensagem" rows="5" required />
          </div>
          <Button type="submit" label="Enviar" class="p-button-primary" />
        </div>
      </form>
    </div>
    
      <!-- Redes Sociais -->
    <div class="social-media-section">
      <h3>Siga-nos nas redes sociais</h3>
      <div class="social-icons">
        <a href="https://facebook.com" target="_blank" class="social-icon">
          <i class="pi pi-facebook"></i>
        </a>
        <a href="https://instagram.com" target="_blank" class="social-icon">
          <i class="pi pi-instagram"></i>
        </a>
        <a href="https://youtube.com" target="_blank" class="social-icon">
          <i class="pi pi-youtube"></i>
        </a>
        <a href="https://twitter.com" target="_blank" class="social-icon">
          <i class="pi pi-twitter"></i>
        </a>
        <a href="https://spotify.com" target="_blank" class="social-icon">
          <i class="pi pi-spotify"></i>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../components/Header.vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import api from '../axios';

// Estado do formulário
const form = ref({
  id: null,
  nome: '',
  email: '',
  setor: '',
});

// Estado da lista de funcionários
const employees = ref([]);

// Estado para controlar se está editando
const isEditing = ref(false);

// Carrega os funcionários ao montar o componente
onMounted(async () => {
  await fetchEmployees();
});

// Função para buscar a lista de funcionários
const fetchEmployees = async () => {
  try {
    const response = await api.get('/api/funcionarios/');
    employees.value = response.data;
  } catch (error) {
    console.error('Erro ao carregar funcionários:', error);
  }
};

// Função para criar ou atualizar um funcionário
const handleSubmit = async () => {
  try {
    if (isEditing.value) {
      // Atualiza um funcionário existente
      await api.put(`/api/funcionarios/${form.value.id}/`, form.value);
    } else {
      // Cria um novo funcionário
      await api.post('/api/funcionarios/', form.value);
    }
    // Limpa o formulário e recarrega a lista
    resetForm();
    await fetchEmployees();
  } catch (error) {
    console.error('Erro ao salvar funcionário:', error);
  }
};

// Função para editar um funcionário
const editEmployee = (employee) => {
  form.value = { ...employee }; // Preenche o formulário com os dados do funcionário
  isEditing.value = true;
};

// Função para deletar um funcionário
const deleteEmployee = async (id) => {
  try {
    await api.delete(`/api/funcionarios/${id}/`);
    await fetchEmployees(); // Recarrega a lista após deletar
  } catch (error) {
    console.error('Erro ao deletar funcionário:', error);
  }
};

// Função para cancelar a edição
const cancelEdit = () => {
  resetForm();
};

// Função para resetar o formulário
const resetForm = () => {
  form.value = {
    id: null,
    nome: '',
    email: '',
    setor: '',
  };
  isEditing.value = false;
};
</script>

<style scoped>
.form-section {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* .p-field {
  margin-bottom: 1rem;
}

.p-field label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
} */
 
.p-field {
  margin-bottom: 1rem;
}
.description-section {
  padding: 2rem;
  text-align: center;
  background-color: #f9f9f9;
}
.p-field label {
  display: block;
  width: 100%x;
  margin-bottom: 0.5rem;
}

.card {
  margin-top: 20px;
}
.social-media-section {
  text-align: center;
  margin-top: 2rem;
  padding: 1rem;
  background-color: #f9f9f9;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
}

.social-icon {
  color: #007bff;
  font-size: 1.5rem;
  transition: color 0.3s ease;
}

.social-icon:hover {
  color: #0056b3;
}
</style>