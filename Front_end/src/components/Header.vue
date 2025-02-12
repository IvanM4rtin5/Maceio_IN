<template>
    <div>
      <!-- Barra superior (Laranja) -->
      <!-- <div class="top-bar">
        <div class="container">
          <ul class="top-menu">
            <li><a href="#">TRANSPARÊNCIA</a></li>
            <li><a href="#">OUVIDORIA</a></li>
            <li><a href="#">DIÁRIO OFICIAL</a></li>
            <li><a href="#">COVID-19</a></li>
            <li><a href="#">ACESSO À INFORMAÇÃO</a></li>
          </ul>
        </div>
      </div> -->
  
      <!-- Navbar principal (Azul) -->
      <b-navbar class="custom-navbar">
        <div class="container d-flex align-items-center justify-content-between">
          <!-- Itens do menu -->
          <b-navbar-nav class="nav-links">
            <b-nav-item href="#">CIDADÃO</b-nav-item>
            <b-nav-item href="#">SERVIDOR</b-nav-item>
            <b-nav-item href="#">EMPRESÁRIO</b-nav-item>
            <b-nav-item href="#">TURISMO</b-nav-item>
            <b-nav-item href="#">IMPRENSA</b-nav-item>
            <b-nav-item-dropdown text="SECRETARIAS E ÓRGÃOS">
              <b-dropdown-item href="#">Educação</b-dropdown-item>
              <b-dropdown-item href="#">Saúde</b-dropdown-item>
              <b-dropdown-item href="#">Fazenda</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </div>
      </b-navbar>
    </div>
  </template>
  
  <style>
  .custom-navbar {
    background-color: #f58428 !important;
    height: 70px;
    padding: 0;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 20px;
  }
  
  /* Itens do menu */
  .nav-links .nav-link {
    color: white !important;
    font-size: 16px;
    font-weight: bold;
    padding: 10px 15px;
  }
  
  .nav-links .nav-link:hover {
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 5px;
    }
  
  .search-box input {
    border: none;
    outline: none;
    padding: 5px;
  }
  @media (max-width: 720px) {
  .nav-links .nav-link {
    font-size: 12px; /* Diminui o tamanho do texto */
    padding: 8px 5px; /* Ajusta o espaçamento */
    }
    }
  </style>
  
  <script setup>
  import { BNavbar, BNavbarNav, BNavItem, BNavItemDropdown, BDropdownItem } from 'bootstrap-vue-next'
  </script>
  