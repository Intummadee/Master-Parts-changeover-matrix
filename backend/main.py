from fastapi import FastAPI

from fastapi import HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from models import Part
from database import SessionLocal, engine
from excel_handler import export_to_excel, import_from_excel
import shutil

app = FastAPI()


Part.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/parts")
def home():
    return {"message": "Hello world!"}


@app.post("/parts")
def add_part(name: str, time: int, db: Session = Depends(get_db)):
    new_part = Part(name=name, changeover_time=time)
    db.add(new_part)
    db.commit()
    return {"message": "Part added successfully"}

@app.post("/export")
def export_excel(db: Session = Depends(get_db)):
    parts = db.query(Part).all()
    export_to_excel(parts)
    return {"message": "Exported to parts.xlsx"}

@app.post("/import")
async def import_excel(file: UploadFile, db: Session = Depends(get_db)):
    with open("uploaded.xlsx", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    import_from_excel("uploaded.xlsx", db)
    return {"message": "Import completed successfully"} 
