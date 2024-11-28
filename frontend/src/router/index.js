import Vue from "vue";
import Router from "vue-router";
import Home from "../App.vue";
import AboutPage from "@/components/AboutPage.vue";

Vue.use(Router);

export default new Router({
  mode: "history", // ใช้ History Mode เพื่อให้ URL สวยงาม
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home, // แสดงคอมโพเนนต์ Home เมื่ออยู่ที่เส้นทาง "/"
    },
    {
      path: "/about",
      name: "AboutPage",
      component: AboutPage, // แสดงคอมโพเนนต์ About เมื่ออยู่ที่เส้นทาง "/about"
    },
    // {
    //     path: "/user/:id",
    //     name: "User",
    //     component: User,
    // } 
    // Dynamic Routes สามารถเข้าถึง id ได้จาก this.$route.params.id ในคอมโพเนนต์ User
    // Navigation Guards ใช้ตรวจสอบสิทธิ์ก่อนเปลี่ยนหน้า
  ],
});
