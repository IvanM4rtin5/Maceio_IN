<template>
    <div class="card">
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
              style="background-color: green; color: white; font-size: 15px; margin-right: 5px; border-radius: 20px;"
            />
            <Button
              icon="pi pi-trash"
              class="p-button-rounded p-button-danger p-button-text"
              @click="deleteEmployee(slotProps.data.id)"
              style="background-color: red; color: white; font-size: 15px; border-radius: 20px;"
            />
          </template>
        </Column>
        <template #empty>
          <p>Nenhum funcionário cadastrado.</p>
        </template>
      </DataTable>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Button from 'primevue/button';
  
  // Props: Recebe a lista de funcionários
  const props = defineProps({
    employees: {
      type: Array,
      required: true,
    },
  });
  
  // Emits: Comunica eventos para o componente pai
  const emits = defineEmits(['edit-employee', 'delete-employee']);
  
  // Função para editar um funcionário
  const editEmployee = (employee) => {
    emits('edit-employee', employee);
  };
  
  // Função para deletar um funcionário
  const deleteEmployee = (id) => {
    emits('delete-employee', id);
  };
  </script>
  
  <style scoped>
  .card {
    margin-top: 20px;
  }
  </style>