import Vue from "vue";
import Router from "vue-router";
import AboutPage from "../components/AboutPage.vue";
import DashboardHome from "@/components/DashboardHome";

import DashBoardViews from '../components/FixComponent/views/DashBoardViews.vue'
import Projects from '../components/FixComponent/views/ProjectsPage.vue'
import Team from '../components/FixComponent/views/TeamPage.vue'


import HomeMain from '../components/HomeMain.vue'

Vue.use(Router);

export default new Router({
  mode: "history", // ใช้ History Mode เพื่อให้ URL สวยงาม
  routes: [
    {
      path: "/",
      name: "HomeMain",
      component: HomeMain,
    },
    {
      path: "/DashboardHome",
      name: "DashboardHome",
      component: DashboardHome, //  จะโหลดคอมโพเนนต์นี้เมื่อไปที่หน้า Home
    },
    {
      path: "/AboutPage",
      name: "AboutPage",
      component: AboutPage, // แสดงคอมโพเนนต์ About เมื่ออยู่ที่เส้นทาง "/about"
      children: [
        // ใช้ nested routes ทำให้ Team และ DashBoardViews เป็นส่วนย่อย (child routes) ของ AboutPage
        {
          path: 'team', // '/about/team'
          name: 'team',
          component: Team,
        },
        {
          path: 'DashBoardViews', // '/about/dashboard'
          name: 'DashBoardViews',
          component: DashBoardViews,
        },
        {
          path: 'projects',
          name: 'projects',
          component: Projects
        }
      ],
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
