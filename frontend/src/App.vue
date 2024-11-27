

<template>
  <v-app>
    <!-- app ระบุว่า <v-app-bar> นี้จะอยู่ในบริบทของ v-app ซึ่งเป็นโครงสร้างหลักของแอปพลิเคชัน -->
    <!-- dark ทำให้ข้อความและไอคอนในแถบใช้โหมดสีเข้ม (เหมาะกับพื้นหลังสีสว่าง) -->
     <!-- ถ้าเป็น light นางคาดหวังว่าตัว text จะเป็นสีดำ กรณี dark คือเป็นสีขาว มันคือการปรับธีม -->
    <v-app-bar 
      app 
      color="primary"
      light
      height="100rem"
    >
    <v-toolbar-title>My App</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <p>Welcome to my Vuetify app!</p>
      </v-container>
    </v-main>
  </v-app>
</template>




<script>
// import axios from "axios";
// import DownloadTable from './components/DownloadTable.vue';
// import UploadTable from './components/UploadTable.vue';
// import chileSlot from './components/chileSlot.vue';
import { ref } from 'vue';

const theme = ref('light')

export default {
  components: {
    // DownloadTable,
    // UploadTable
  },
  data() {
    return {
      theme: 'light', // กำหนดธีมเริ่มต้น
    };
  },
  methods: {
    onToggleTheme () {
      theme.value = theme.value === 'light' ? 'dark' : 'light' // ถ้าใช่ (true) จะคืนค่า 'dark' 
    }
    
  },
  mounted() {
    // this.fetchParts();
  }
};
</script>

<style scoped>
.light {
  background-color: #ffffff;
  color: #000000;
}

.dark {
  background-color: #000000;
  color: #ffffff;
}
</style>
