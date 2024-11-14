import pandas as pd
from sqlalchemy.orm import Session
from models import Part

def export_to_excel(parts):
    data = [{"name": part.name, "changeover_time": part.changeover_time} for part in parts]
    df = pd.DataFrame(data)
    df.to_excel("parts.xlsx", index=False)

def import_from_excel(file_path, db: Session):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        part = db.query(Part).filter(Part.name == row['name']).first()
        if part:
            part.changeover_time = row['changeover_time']
        else:
            part = Part(name=row['name'], changeover_time=row['changeover_time'])
            db.add(part)
    db.commit()
