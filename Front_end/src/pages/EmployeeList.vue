<template>
  <div>
    <Header />
    <div class="description-section">
      <h1>SEFAZ de Maceió</h1>
      <p>
        A Secretaria da Fazenda (SEFAZ) de Maceió é responsável pela administração tributária, finanças e contabilidade do município. 
        Nossa missão é garantir a arrecadação de recursos necessários para o desenvolvimento da cidade, promovendo a transparência e a eficiência na gestão pública.
      </p>
    </div>

    <div class="content">
      <h2>Lista de Funcionários</h2>

    <!-- Componente DataTable -->
     <DataTable
        :employees="employees"
        @edit-employee="editEmployee"
        @delete-employee="deleteEmployee"
        style="margin-bottom: 60px;"
      />

      <!-- Formulário para criar/editar funcionários -->
      <div class="form-section">
        <h2>{{ isEditing ? 'Editar Funcionário' : 'Novo Funcionário' }}</h2>
        <hr />
        <form @submit.prevent="handleSubmit">
          <div class="p-fluid">
            <div class="p-field">
              <label for="nome">Nome</label>
              <InputText id="nome" v-model="form.nome" placeholder="Digite o nome" required />
            </div>
            <div class="p-field">
              <label for="email">Email</label>
              <InputText id="email" v-model="form.email" placeholder="Digite o email" type="email" required />
            </div>
            <div class="p-field">
              <label for="setor">Setor</label>
              <InputText id="setor" v-model="form.setor" placeholder="Digite o setor" required />
            </div>
            <div class="p-field">
              <Button type="submit" :label="isEditing ? 'Atualizar' : 'Criar'" class="p-button-primary" />
              <Button v-if="isEditing" type="button" label="Cancelar" class="p-button-secondary" @click="cancelEdit" />
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Componente Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../components/Header.vue';
import DataTable from '../components/DataTable.vue';
import Footer from '../components/Footer.vue';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
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
  form.value = { ...employee };
  isEditing.value = true;
};

// Função para deletar um funcionário
const deleteEmployee = async (id) => {
  try {
    await api.delete(`/api/funcionarios/${id}/`);
    await fetchEmployees();
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
.content {
  padding: 100px;
  background-color:  #007bff;

  h2 {
    color: #fff;
    text-align: center;
    margin-bottom: 20px;
    font-size: 2.5rem;
    font-family: sans-serif !important;
  }
}

.form-section {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.p-field {
  margin-bottom: 1rem;
}

.p-field label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}
.description-section {
  padding: 2rem;
  text-align: center;
  background-color:#004a77;
  color: #fff5f9;
  font-family: sans-serif;

  p{
    font-size: 18px;
  }
}
</style>