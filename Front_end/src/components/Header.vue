<template>
  <div class="header-container">
    <Menubar :model="items" class="custom-menubar">
      <template #start>
      </template>
      <template #end>
        <Button 
          icon="pi pi-bars" 
          @click="toggleMenu" 
          class="p-button-text p-button-white menu-button"
          v-if="isMobile"
        />
      </template>
    </Menubar>
    <div class="info-bar">
      <img src="../assets/logo_prefeitura_de_maceio.svg" style="height: 70px; width: 80;" alt="Logo Maceió" class="logo-maceio" />
      <img src="../assets/logoNova.png" style="height: 70px; width: 150px;" alt="Maceio_informa">
    </div>
    <Sidebar v-model:visible="sidebarVisible" position="right" class="mobile-menu">
      <nav>
        <ul class="mobile-menu-list">
          <li v-for="(item, i) in items" :key="i">
            <a :href="item.to" class="mobile-menu-item">{{ item.label }}</a>
          </li>
        </ul>
      </nav>
    </Sidebar>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import Sidebar from 'primevue/sidebar';

const sidebarVisible = ref(false);
const isMobile = ref(false);

const items = ref([
  {
    label: 'TRANSPARÊNCIA',
    to: '/transparencia'
  },
  {
    label: 'OUVIDORIA',
    to: '/ouvidoria'
  },
  {
    label: 'DIÁRIO OFICIAL',
    to: '/diario-oficial'
  },
  {
    label: 'COVID-19',
    to: '/covid'
  },
  {
    label: 'ACESSO À INFORMAÇÃO',
    to: '/acesso-informacao'
  },
  {
    label: 'SECRETARIAS E ÓRGÃOS',
    items: [
      {
        label: 'Educação',
        to: '/educacao'
      },
      {
        label: 'Saúde',
        to: '/saude'
      },
      {
        label: 'Fazenda',
        to: '/fazenda'
      }
    ]
  }
]);

const toggleMenu = () => {
  sidebarVisible.value = !sidebarVisible.value;
};

const checkScreenSize = () => {
  isMobile.value = window.innerWidth < 720;
};

onMounted(() => {
  checkScreenSize();
  window.addEventListener('resize', checkScreenSize);
});

onUnmounted(() => {
  window.removeEventListener('resize', checkScreenSize);
});
</script>

<style scoped>
.header-container {
  position: relative;
  border-radius: 0%;
}

.custom-menubar {
  background: #f58428;
  border: none;
  padding: 1rem;
  border-radius: 0;

}

:deep(.p-menubar-root-list) {
  gap: 1rem;
}

:deep(.p-menuitem-link) {
  color: white !important;
  font-weight: bold;
  border: none !important;
  text-decoration: none;
  padding: 0.5rem 1rem;
  transition: background-color 0.2s;
}

:deep(.p-menuitem-content:hover) {
  background-color: rgba(34, 2, 2, 0.144);  
}

:deep(.p-menuitem-text) {
  color: white !important;
}

.menu-button {
  color: white !important;
}
.mobile-menu {
  width: 80vw;
  max-width: 300px;
}

.mobile-menu-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.mobile-menu-item {
  display: block;
  padding: 1rem;
  color: #333;
  text-decoration: none;
  border-bottom: 1px solid #eee;
}

.info-bar {
  background: #f4f4f4; /* Cor clara da faixa */
  padding: 2rem 0;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.description-section {
  padding: 2rem;
  text-align: center;
  background-color: #f9f9f9;
}

.form-section {
  padding: 2rem;
  max-width: 600px;
  margin: 0 auto;
}

@media (max-width: 720px) {
  :deep(.p-menubar-root-list) {
    display: none;
  }
  :deep(a.p-menubar-button) {
    display: none;
  }
}
</style>