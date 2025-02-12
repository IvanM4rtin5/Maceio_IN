import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// PrimeVue
import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/saga-blue/theme.css'     // tema
import 'primevue/resources/primevue.css'                  // core css
import 'primeicons/primeicons.css'                       // icons

// PrimeVue Components
import RadioButton from 'primevue/radiobutton'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Menubar from 'primevue/menubar'
import Sidebar from 'primevue/sidebar'

const app = createApp(App)

// Use plugins
app.use(router)
app.use(PrimeVue)

// Register PrimeVue components
app.component('RadioButton', RadioButton)
app.component('InputText', InputText)
app.component('Password', Password)
app.component('Button', Button)
app.component('Menubar', Menubar)
app.component('Sidebar', Sidebar)

app.mount('#app')