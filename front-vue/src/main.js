import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import axios from 'axios'
// import VueAxios from 'vue-axios'

createApp(App).use(store).use(router).mount('#app')

// const app = createApp(App)

// // Configurar o Axios
// const axiosInstance = axios.create({
//   baseURL: 'https://api.example.com',  // Substitua pela sua URL base
// })

// // Integrar o Axios ao Vue usando VueAxios
// app.use(VueAxios, axiosInstance)

// // Monte o aplicativo
// app.mount('#app')

