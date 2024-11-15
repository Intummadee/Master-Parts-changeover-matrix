# Master Parts changeover matrix
 
<img width="100%" height="60%" src="https://github.com/Intummadee/Master-Parts-changeover-matrix/blob/main/assets/image_web.png">


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



# Deployment Instructions

## Prerequisites
- Install Docker and Docker Compose

## Steps to Deploy
1. Clone the project repository:
   ```
   git clone https://github.com/your-repo/project.git
   cd project
   ```

2. Build and start the containers:

   ```docker-compose up --build```

Frontend: http://localhost:8080
Backend: http://localhost:8000/docs

- Stop the services:
```docker-compose down```












