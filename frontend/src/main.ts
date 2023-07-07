// @ts-ignore
import Vue, {App as Application, createApp} from "vue";

// Components
// @ts-ignore
import App from "@/App.vue";

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap/dist/js/bootstrap.js'


const ticTacToeApp: Application = createApp(App);
ticTacToeApp.mount("#app");
