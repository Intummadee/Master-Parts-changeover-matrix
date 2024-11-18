# Master Parts changeover matrix
 
<img width="100%" height="60%" src="https://github.com/Intummadee/Master-Parts-changeover-matrix/blob/main/assets/image_web.png">

Figma Link
: https://www.figma.com/design/Vusfg2R4YJApNm5rVVGK8o/Untitled?node-id=0-1&t=G8Zprf9IyEEWs42b-1


```
project/
├── backend/
│   ├── data/ # ข้อมูลไว้เทสตอนลองDB
│   ├── Dockerfile
│   ├── requirements.txt
│   │── main.py           
│   │── database.py       
│   │── migrations.py     # Auto Migration Script
├── docker-compose.yml        # Docker Compose Configuration
├── frontend/
│   ├── Dockerfile
│   ├── package.json          
│   ├── src/
│   │   ├── App.vue           
│   │   └── components/       
│   │       ├── DownloadTable.vue  
│   │       ├── UploadTable.vue 
└── README.md                
```



> [!IMPORTANT]
> ## สำหรับการ Deploy


1. ทำการติดตั้ง Docker และ Docker Compose ซึ่งตรวจสอบการติดตั้งได้ผ่านทาง ถ้าติดตั้งแล้วจะได้ เวอร์ชั่นออกมาเช่น Docker version 27.3.1, build ce12230 และ Docker Compose version v2.29.7-desktop.1
```
docker -v
docker-compose -v
```

2. Clone โปรเจกต์จาก GitHub
```
git clone https://github.com/Intummadee/Master-Parts-changeover-matrix.git
cd Master-Parts-changeover-matrix
```

3. ขั้นตอนการ Deploy ด้วย Docker Compose
- รันคำสั่งนี้เพื่อสร้างและรัน container ทั้งหมด
```docker-compose up -d --build```
- คำสั่งตรวจสอบสถานะการรัน ```docker-compose ps```


4. ทดสอบการเข้าถึง 
เปิดเบราว์เซอร์และเข้าผ่าน URL ดังนี้:
Frontend: ```http://your-server-ip/```
Backend: ```http://your-server-ip:8000/```

ตรวจสอบ server-ip 
- คำสั่ง ```curl ifconfig.me```
- ถ้าเป็นสำหรับ IP Address ภายในเครือข่าย ```hostname -I```
- ถ้าเป็น บริการ Cloud เช่น AWS, Google Cloud สามารถดู IP Address ของเซิร์ฟเวอร์ได้จากหน้า Dashboard ของผู้ให้บริการ





> [!IMPORTANT]
> ## สำหรับการ อัพเดตโปรเจกต์

1. หากคุณมีการอัพเดตโค้ดบน GitHub และต้องการ pull โค้ดใหม่ ให้ใช้คำสั่งนี้
```
git pull
docker-compose up -d --build
```
2. รีสตาร์ท container ทั้งหมด ด้วยคำสั่ง
```docker-compose restart```




<details>
<summary><h2>คำสั่งอื่นๆ เพิ่มเติม</h2></summary>
<ul>
   <li>คำสั่งหยุด container ทั้งหมด
```docker-compose down```</li>
   <li>ลบ container และ volume ทั้งหมด 
```docker-compose down -v```</li>
   <li>ดูสถานะของ container ที่รันอยู่ทั้งหมดในเครื่อง:
```docker ps```</li>
   <li></li>
</ul>





> [!NOTE]
> ## สรุปขั้นตอนง่าย ๆ
> 1. ติดตั้ง docker และ docker compose
> 2. Clone โปรเจกต์ จาก GitHub
> 3. รันคำสั่ง docker-compose up -d --build
> 4. ทดสอบการเข้าถึง ที่ IP ของเซิร์ฟเวอร์
> 5. อัพเดตโปรเจกต์ ด้วย git pull และรันใหม่

