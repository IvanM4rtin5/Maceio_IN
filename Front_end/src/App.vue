<script setup>
import Toast from 'primevue/toast';
</script>

<template>
  <div>
    <Toast />
    <router-view></router-view> <!-- Aqui as páginas serão renderizadas -->
  </div>
</template>

<style scoped>
/* Estilos globais ou específicos para o App.vue */
</style>