<template>
  <nav>
    <v-app-bar  color="purple" dark app >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- .stop: เป็น event modifier ที่ใช้เพื่อหยุด (stop) การแพร่กระจาย (propagation) ของ event ไปยัง element บรรจุ (parent element) ซึ่งหมายความว่า event click จะไม่ถูกส่งต่อขึ้นไปยัง parent element อื่น ๆ -->
      <v-toolbar-title class="text-uppercase ">
          <span class="font-weight-light">AAE   </span>
          <span>IdeaPro</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <!-- {on} เป็น object ที่มี event listeners (เช่น @click, @mouseenter) ซึ่งเชื่อมโยงกับการแสดง/ซ่อนเมนู. โดยไม่ต้องกำหนด manual เช่น @click. -->
          <v-btn text v-on="on">
            <v-icon left>expand_more</v-icon>
            <span>Menu</span>
          </v-btn>
        </template>

        <v-list flat>
          <v-list-item v-for="link in links"  :key="link.text" router :to="link.route" active-class="border">
            <v-list-item-title >{{link.text}}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <!-- ปุ่ม exit -->
      <v-btn text>
          <span>Exit</span>
          <v-icon right>exit_to_app</v-icon>
      </v-btn>
    </v-app-bar>


    <v-navigation-drawer  v-model="drawer" dark app class="red darken-4">
      <v-layout column align-center>
          <v-flex class="mt-5"> 
                <v-avatar size="100">
                    <img src="https://i2.wp.com/genshinbuilds.aipurrjects.com/genshin/characters/nilou/image.png?strip=all&quality=75&w=256" alt="" srcset="">
                </v-avatar>
                <p class="white--text subheading mt-1 text-center">Username</p>
          </v-flex>
          <v-flex class="mt-4 mb-4">
            <!-- Popup -->
            <Popup />
          </v-flex>
      </v-layout>
      <v-list flat>
          <v-list-item v-for="link in links"  :key="link.text" router :to="link.route" active-class="border">
              <v-list-item-action>
                <v-icon >{{link.icon}}</v-icon>
              </v-list-item-action>
              <v-list-item-content >
                  <v-list-item-title >{{link.text}}</v-list-item-title>
              </v-list-item-content>
          </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>
<script>
import Popup from './PopupPage.vue'
export default {
  data: () => ({
     drawer: true,
     links :[
         {icon: 'dashboard', text:'Dashboard', route: '/AboutPage/DashBoardViews'},
         {icon: 'folder', text:'My Project', route: '/AboutPage/projects'},
         {icon: 'person', text:'Team', route: '/AboutPage/team'}
     ]
    
   }),
   components: {
   Popup
 },

  
}
</script>
<style scoped>
.border {
  border-left: 4px solid #0ba518;
  padding: 8px;
  border-radius: 0%;
}
</style>