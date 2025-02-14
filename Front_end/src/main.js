import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// PrimeVue
import PrimeVue from 'primevue/config';
import "@vueuse/core";
import ToastService from 'primevue/toastservice';

// PrimeVue Styles 
import 'primevue/resources/themes/saga-blue/theme.css'  
import 'primevue/resources/primevue.css'  
import 'primeicons/primeicons.css'

// Apenas Bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// PrimeVue Components
import RadioButton from 'primevue/radiobutton';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Menubar from 'primevue/menubar';
import Sidebar from 'primevue/sidebar';
import Dialog from 'primevue/dialog';

const app = createApp(App);

app.use(router);
app.use(PrimeVue);
app.use(ToastService);

// Register PrimeVue components
app.component('RadioButton', RadioButton);
app.component('InputText', InputText);
app.component('Password', Password);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('Button', Button);
app.component('Menubar', Menubar);
app.component('Sidebar', Sidebar);
app.component('Dialog', Dialog);

app.mount('#app');