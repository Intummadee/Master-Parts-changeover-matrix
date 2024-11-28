import Vue from "vue";
import Router from "vue-router";
import AboutPage from "../components/AboutPage.vue";
import DashboardHome from "@/components/DashboardHome";

Vue.use(Router);

export default new Router({
  mode: "history", // ใช้ History Mode เพื่อให้ URL สวยงาม
  routes: [
    {
      path: "/",
      name: "DashboardHome",
      component: DashboardHome, //  จะโหลดคอมโพเนนต์นี้เมื่อไปที่หน้า Home
    },
    {
      path: "/AboutPage",
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
