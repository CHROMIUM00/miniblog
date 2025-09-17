import "./assets/normalize.css"

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';

import '@/assets/art.css'

import createHljsTheme from '@kangc/v-md-editor/lib/theme/hljs';

import hljs from 'highlight.js'

const hljsTheme = createHljsTheme({
    Hljs: hljs,
});

VueMarkdownEditor.vMdParser.theme(hljsTheme);


import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)

app.use(router)

app.use(VueMarkdownEditor)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.mount('#app')
