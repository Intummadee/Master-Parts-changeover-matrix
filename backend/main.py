from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Response
import shutil
from sqlmodel import Session, select
import json
import pathlib
from typing import List, Union  
from database import engine, Parts , Changeover

app = FastAPI()

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
@app.post("/parts/", response_model=Parts, status_code=201)  # Changed Track to Parts here
def create_parts(part: Parts, session: Session = Depends(get_session)): 
    session.add(part)
    session.commit()
    session.refresh(part)
    return part



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
