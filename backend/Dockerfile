#! Dockerfile สำหรับ Backend (FastAPI + SQLite) 


FROM python:3.10-slim

WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์แอปทั้งหมด
COPY . .

# รัน migrations ครั้งเดียวในขั้นตอน build
RUN python -m app.migrations


# รันคำสั่ง migration ก่อนเริ่มแอป
# การรัน migration ในตอนเริ่มต้นแอปพลิเคชัน
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# เปิดพอร์ต 8000 สำหรับการสื่อสาร
EXPOSE 8000
