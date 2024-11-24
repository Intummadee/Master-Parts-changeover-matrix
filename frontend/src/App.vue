




<!-- Parent Component -->
<template>
  <MyComponent>
    <template v-slot:chileSlot>
      Header content
    </template>
    <template v-slot:default>
      Main content
    </template>
    <template v-slot:footer>
      Footer content
    </template>
  </MyComponent>
</template>






<script>
// import axios from "axios";
// import DownloadTable from './components/DownloadTable.vue';
// import UploadTable from './components/UploadTable.vue';
import chileSlot from './components/chileSlot.vue';
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
