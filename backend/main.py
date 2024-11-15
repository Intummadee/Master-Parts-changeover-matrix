from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Response
import shutil
from sqlmodel import Session, select
import json
import pathlib
from typing import List, Union  
from database import engine, Parts , Changeover 
from fastapi.responses import FileResponse
from io import BytesIO
import pandas as pd
from fastapi.responses import StreamingResponse



# Excel
import pandas as pd
from io import BytesIO


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:8080"],  # frontend origin
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

data = []

# define app start-up event
@app.on_event("startup")
async def startup_event():
    DATAFILE = pathlib.Path() / 'data' / 'allParts.json'

    session = Session(engine)
    stmt = select(Parts)
    result = session.exec(stmt).first()

    # load data if there's no result
    if result is None:
        with open(DATAFILE, 'r') as f:
            allParts = json.load(f)
            for eachPart in allParts:
                session.add(Parts(**eachPart))
        session.commit()


    # Load changeover data
    DATAFILE_CHANGEOVER = pathlib.Path() / 'data' / 'changeOver.json'

    # Check if Changeover table is empty, then load changeover data
    stmt_changeover = select(Changeover)
    result_changeover = session.exec(stmt_changeover).first()
    if result_changeover is None:
        with open(DATAFILE_CHANGEOVER, 'r') as f:
            changeovers = json.load(f)
            for changeover in changeovers:
                session.add(Changeover(**changeover))
        session.commit()


    session.close()


def get_session():
    with Session(engine) as session:
        yield session



@app.get("/parts", response_model=List[Parts])  # Changed Track to Parts here
def parts(session: Session = Depends(get_session)): 
    stmt = select(Parts)
    result = session.exec(stmt).all()
    return result



@app.get("/parts/{parts_id}", response_model=Union[Parts, str])
def parts(parts_id: int , response: Response, session: Session = Depends(get_session)): 
    part = session.get(Parts , parts_id)
    if parts is None:
        response.status_code = 404
        return "Not found this Part"
    return part


# Post
@app.post("/parts/", response_model=Parts, status_code=201) 
def create_parts(part: Parts, session: Session = Depends(get_session)):
    # ตรวจสอบว่า part_name ไม่เป็นค่าว่าง
    if not part.part_name or part.part_name.strip() == "":
        raise HTTPException(status_code=400, detail="Part name is required")

    # ตรวจสอบว่า part_name ไม่ซ้ำ
    existing_part = session.query(Parts).filter(Parts.part_name == part.part_name).first()
    if existing_part:
        raise HTTPException(status_code=400, detail="Part name already exists")

    # สร้างข้อมูล part ใหม่
    new_part = Parts(part_name=part.part_name)

    # เพิ่มข้อมูลลงในฐานข้อมูล
    session.add(new_part)
    session.commit()
    session.refresh(new_part)

    return new_part

# Put
@app.put("/parts/{parts_id}", response_model=Union[Parts, str])  # Changed Track to Parts here
def update_parts(parts_id: int , updated_part: Parts , response: Response, session: Session = Depends(get_session)): 
    part = session.get(Parts , parts_id)

    if part is None:
        response.status_code = 404
        return "Parts not found"
    
    # update
    part_dict = updated_part.dict(exclude_unset=True)
    for key , val in part_dict.items():
        setattr(part, key , val)
    session.add(part)
    session.commit()
    session.refresh(part)

    return part


# Delete
@app.delete("/parts/{parts_id}")  # Changed Track to Parts here
def delete_parts(parts_id: int ,response: Response, session: Session = Depends(get_session)): 
    
    part = session.get(Parts , parts_id)

    if part is None:
        response.status_code = 404
        return "Parts not found"
    
    session.delete(part)
    session.commit()
    return Response(status_code=200)




@app.get("/changeOver", response_model=List[Changeover])  # Changed Track to Parts here
def parts(session: Session = Depends(get_session)): 
    stmt = select(Changeover)
    result = session.exec(stmt).all()
    return result



# Delete
@app.delete("/changeOver/{from_part_id}/{to_part_id}")
def delete_changeover(from_part_id: int, to_part_id: int, response: Response, session: Session = Depends(get_session)):
    stmt = select(Changeover).where(Changeover.from_part_id == from_part_id, Changeover.to_part_id == to_part_id)
    changeover = session.exec(stmt).first()
    
    if not changeover:
        response.status_code = 404
        return "Changeover entry not found"
    
    session.delete(changeover)
    session.commit()
    return Response(status_code=200)



# Post
@app.post("/changeOver/", response_model=Changeover, status_code=201)  # Changed Track to Parts here
def create_parts(Changeover: Changeover, session: Session = Depends(get_session)): 
    session.add(Changeover)
    session.commit()
    session.refresh(Changeover)
    return Changeover








@app.post("/export-to-excel")
async def export_to_excel(data: list):
    df = pd.DataFrame(data)

    excel_file = BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    return Response(
        content=excel_file.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=parts_changeover.xlsx"
        }
    )

@app.get("/table", response_model=List)
def get_table(session: Session = Depends(get_session)):
    parts = session.query(Parts).all()
    changeovers = session.query(Changeover).all()

    table_data = []

    for part in parts:
        changeover_times = {}

        for changeover in changeovers:
            if changeover.from_part_id == part.id:
                to_part = next((p for p in parts if p.id == changeover.to_part_id), None)
                if to_part:
                    changeover_times[to_part.part_name] = changeover.changeover_time

        table_data.append({
            "id": part.id,
            "part_name": part.part_name,
            "changeoverTimes": changeover_times
        })

    df = pd.DataFrame([
        {
            "Part Name": part["part_name"],
            **part["changeoverTimes"]
        }
        for part in table_data
    ])

    tg_columns = sorted([col for col in df.columns if col.startswith("TG")], key=lambda x: int(x[2:]))

    ordered_columns = ["Part Name"] + tg_columns

    df = df.loc[:, ordered_columns]

    print(df)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Parts Table')

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=parts_table.xlsx"}
    )