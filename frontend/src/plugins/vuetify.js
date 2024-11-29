import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import "echarts"


Vue.use(Vuetify);

export default new Vuetify({
    icons: {
        iconfont: 'fa' || 'md'
    },
    theme: {
        // dark: false, // เริ่มต้นเป็นธีม Light
        defaultTheme: 'light',
        themes:{
            dark: {
                background: '#EEEEEE',
                primary: "#BB86FC",
                secondary: "#03DAC6",
                accent: "#CF6679",
            },
            light: {
                background: '#EEEEEE',
                primary: "#1976D2",
                secondary: "#424242",
                accent: "#82B1FF",
            }
        }
    }
});
