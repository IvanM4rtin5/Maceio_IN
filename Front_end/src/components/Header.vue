<template>
  <div class="header-container">
    <Menubar :model="items" class="custom-menubar">
      <template #start>
        <img src="#" alt="Logo" height="40" class="mr-2" />
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
      <img src="#" alt="Logo Maceió" class="logo-maceio" />
      <span class="info-text">INFORMA MACEIÓ</span>
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
import { ref, onMounted, onUnmounted } from 'vue'
import { useMediaQuery } from '@vueuse/core'

const sidebarVisible = ref(false)
const isMobile = useMediaQuery('(max-width: 768px)')

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
])

const toggleMenu = () => {
  sidebarVisible.value = !sidebarVisible.value
}
</script>

<style scoped>
.header-container {
  position: relative;
}

.custom-menubar {
  background: #f58428;
  border: none;
  padding: 1rem;
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

:deep(.p-menuitem-link:hover) {
  background-color: #fff;  
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

.mobile-menu-item:hover {
  background-color: #f5f5f5;
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

@media (max-width: 768px) {
  :deep(.p-menubar-root-list) {
    display: none;
  }
}
</style>