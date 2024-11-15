# Master Parts changeover matrix
 


```
pip install -r requirements.txt
cd backend
env\Scripts\activate
uvicorn main:app --reload
```


```
cd .\project-name\
npm run serve
```

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
