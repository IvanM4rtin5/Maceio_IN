<template>
  <div>
    <Header />
    <div class="description-section">
      <h1>SEFAZ de Maceió</h1>
      <p>
        A Secretaria da Fazenda (SEFAZ) de Maceió é responsável pela
        administração tributária, finanças e contabilidade do município. Nossa
        missão é garantir a arrecadação de recursos necessários para o
        desenvolvimento da cidade, promovendo a transparência e a eficiência na
        gestão pública.
      </p>
    </div>

    <div class="content">
      <h2>Lista de Funcionários</h2>

      <!-- Componente DataTable -->
      <DataTable
        :employees="employees"
        @edit-employee="openEditModal"
        @delete-employee="deleteEmployee"
        style="margin: 50px;"
      />

      <!-- Modal de Edição de Funcionário -->
      <Dialog
        v-model:visible="modalVisible"
        header="Editar Funcionário"
        :modal="true"
        class="p-fluid"
        :style="{ width: '50vw' }"
      >
        <form @submit.prevent="handleSubmit">
          <div class="p-fluid">
            <div class="p-field">
              <label for="nome">Nome</label>
              <InputText
                id="nome"
                v-model="form.nome"
                placeholder="Digite o nome"
                required
              />
            </div>
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
            <div class="p-field">
              <label for="setor">Setor</label>
              <InputText
                id="setor"
                v-model="form.setor"
                placeholder="Digite o setor"
                required
              />
            </div>
            <Button
              type="button"
              label="Cancelar"
              class="p-button-secondary"
              @click="closeModal"
            />
            <Button type="submit" :label="isEditing ? 'Atualizar' : 'Salvar'" class="p-button-primary" />
          </div>
        </form>
      </Dialog>

      <div class="description-funcionarios">
        <h3>Sistema de Registro de Funcionários - SEFAZ Maceió</h3>

        <h5 style="margin-bottom: 30px">
          Instruções para Adicionar um Novo Funcionário
        </h5>
        <ul>
          <span> 1. Preencha os Campos:</span>

          <li>Nome: Insira o nome completo do funcionário.</li>

          <li>
            Email: Informe o endereço de e-mail corporativo do funcionário.
          </li>

          <li>
            Setor: Selecione ou insira o setor ao qual o funcionário está
            vinculado.
          </li>

          <span>Salvar Registro:</span>
        </ul>
        <p style="text-align: left; margin-left: 15px">
          Após preencher todos os campos, clique no botão
          <span style="font-weight: bold">"Salvar"</span> para cadastrar o novo
          funcionário no sistema.
        </p>

        <ul>
          <span
            >2. Instruções para Editar as Informações de um Funcionário</span
          >
          Localize o Funcionário:

          <li>
            Utilize a busca ou a lista de funcionários para encontrar o registro
            que deseja editar.
          </li>

          <li>Atualize os Campos:</li>

          <li>Nome: Edite o nome do funcionário, se necessário.</li>

          <li>
            Email: Edite o endereço de e-mail corporativo do funcionário, se
            necessário.
          </li>

          <li>
            Setor: Edite o setor ao qual o funcionário pertence, se necessário.
          </li>

          <li>Escolha uma Ação:</li>

          <li style="list-style-type: none">
            <span>Atualizar:</span> Clique no botão "Atualizar" para salvar as
            alterações.
          </li>

          <li style="list-style-type: none">
            <span>Cancelar:</span> Clique no botão "Cancelar" para descartar as
            alterações e voltar à tela anterior.
          </li>
        </ul>

        <ul>
          <h5 style="margin-left: -20px">Campos do Formulário</h5>
          <li style="list-style-type: none">
            <span style="font-size: 16px">Campos para Adicionar:</span>
          </li>

          <li>Nome</li>
          <li>Email</li>
          <li>Setor</li>

          <li style="list-style-type: none">
            <span style="font-size: 16px">Campos para Atualizar:</span>
          </li>
          <li>Nome</li>
          <li>Email</li>
          <li>Setor</li>

          <span> Botões Disponíveis</span>
          <li>Adicionar Funcionário:</li>
          <li>Salvar: Cadastra um novo funcionário.</li>

          <li>Cancelar: Descarta as alterações e volta à tela anterior.</li>

          <li>Editar Funcionário:</li>

          <li>Atualizar: Salva as alterações feitas no registro.</li>
        </ul>

        Este sistema foi desenvolvido para facilitar o gerenciamento de
        funcionários da SEFAZ de Maceió, garantindo que as informações estejam
        sempre atualizadas e organizadas. Em caso de dúvidas, entre em contato
        com o suporte técnico.
      </div>

      <!-- Formulário para criar/editar funcionários -->
      <div class="form-section">
        <h3>{{ isEditing ? "Editar Funcionário" : "Novo Funcionário" }}</h3>
        <hr />
        <form @submit.prevent="handleSubmit">
          <div class="p-fluid">
            <div class="p-field">
              <label for="nome">Nome</label>
              <InputText
                id="nome"
                v-model="form.nome"
                placeholder="Digite o nome"
                required
              />
            </div>
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
            <div class="p-field">
              <label for="setor">Setor</label>
              <InputText
                id="setor"
                v-model="form.setor"
                placeholder="Digite o setor"
                required
              />
            </div>
            <div class="p-field">
              <Button type="submit" :label="isEditing ? 'Atualizar' : 'Salvar'" class="p-button-primary" />
            </div>
          </div>
          <Button
            type="button"
            label="Voltar"
            class="p-button-secondary"
            @click="Logout"
            style="background-color: red"
          />
        </form>
      </div>
    </div>

    <!-- Componente Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useToast } from "primevue/usetoast"
import Header from "../components/Header.vue"
import DataTable from "../components/DataTable.vue"
import Footer from "../components/Footer.vue"
import InputText from "primevue/inputtext"
import Button from "primevue/button"
import api from "../axios"
import router from "@/router"

// Estado do formulário
const form = ref({
  id: null,
  nome: "",
  email: "",
  setor: "",
})

const toast = useToast()
// Estado da lista de funcionários
const employees = ref([])

// Estado para controle do modal
const modalVisible = ref(false);

// Estado para controlar se está editando
const isEditing = ref(false)

// Carrega os funcionários ao montar o componente
onMounted(async () => {
  await fetchEmployees()
})

// Função para buscar a lista de funcionários
const fetchEmployees = async () => {
  try {
    const response = await api.get("/api/funcionarios/")
    employees.value = response.data
  } catch (error) {
    console.error("Erro ao carregar funcionários:", error)
  }
}

const handleSubmit = async () => {
  if (!form.value.nome || !form.value.email || !form.value.setor) {
    toast.add({
      severity: "error",
      summary: "Erro",
      detail: "Por favor, preencha todos os campos e sem espaços em brancos",
      life: 3000,
    });
    return;
  }

  try {
    if (isEditing.value) {
      await api.put(`/api/funcionarios/${form.value.id}/`, form.value);
      toast.add({
        severity: "success",
        summary: "Sucesso",
        detail: "Funcionário atualizado com sucesso",
        life: 3000,
      });
    } else {
      const response = await api.post("/api/funcionarios/", form.value);
      
      if (response.status === 201 || response.status === 200) {
        toast.add({
          severity: "success",
          summary: "Sucesso",
          detail: "Funcionário criado com sucesso",
          life: 3000,
        });

        // Atualiza a lista do DataTable
        await fetchEmployees();
      }
    }

    // Limpa o formulário e fecha o modal
    resetForm();
    closeModal();
  } catch (error) {
    console.error("Erro ao salvar funcionário:", error);
    toast.add({
      severity: "error",
      summary: "Erro",
      detail: "Não foi possível salvar o funcionário",
      life: 3000,
    });
  }
};

// Função para editar um funcionário e abrir o modal
const openEditModal = (employee) => {
  form.value = { ...employee };
  isEditing.value = true; 
  modalVisible.value = true; 
};

// Função para deletar um funcionário
const deleteEmployee = async (id) => {
  try {
    await api.delete(`/api/funcionarios/${id}/`)
    await fetchEmployees()
  } catch (error) {
    console.error("Erro ao deletar funcionário:", error)
  }
}

// Função para fechar o modal
const closeModal = () => {
  modalVisible.value = false;
  resetForm();
};

// Função para logout
const Logout = () => {
  localStorage.removeItem("token")
  window.location.href = "/signin"
}

// Função para resetar o formulário
const resetForm = () => {
  form.value = {
    id: null,
    nome: "",
    email: "",
    setor: "",
  }
  isEditing.value = false
}
</script>

<style scoped>
.content {
  padding: 100px;
  background-color: #007bff;

  h2 {
    color: #fff;
    text-align: center;
    margin-bottom: 20px;
    font-size: 2.5rem;
    font-weight: bold;
    font-family: sans-serif !important;
  }
  h3 {
    text-align: center;
    margin-bottom: 20px;
    font-size: 2rem;
    font-weight: bold;
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
  background-color: #004a77;
  color: #fff5f9;
  font-family: sans-serif;

  p {
    font-size: 18px;
  }
}
.description-funcionarios {
  padding: 2rem;
  text-align: center;
  color: #fff5f9;
  font-family: sans-serif;

  p {
    font-size: 18px;
  }
}
ul {
  text-align: left;
  gap: 0.5rem;

  span {
    font-size: 18px;
    font-weight: bold;
    margin-left: -20px;
  }
}
li {
  font-size: 16px;
  text-align: left;
}
.custom-modal {
  width: 150vw; /* Largura de 50% da viewport */
  max-width: 800px; /* Largura máxima de 800px */
  min-width: 600px; /* Largura mínima de 600px */
}
</style>
