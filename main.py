from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal, engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Project endpoints
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db=db, skip=skip, limit=limit)

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db=db, project_id=project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    updated_project = crud.update_project(db=db, project_id=project_id, project=project)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    if not crud.delete_project(db=db, project_id=project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Project deleted"}

# BlogPost endpoints
@app.post("/blogposts/", response_model=schemas.BlogPost)
def create_blogpost(blogpost: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_blogpost(db=db, blogpost=blogpost)

@app.get("/blogposts/", response_model=List[schemas.BlogPost])
def read_blogposts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_blogposts(db=db, skip=skip, limit=limit)

@app.get("/blogposts/{blogpost_id}", response_model=schemas.BlogPost)
def read_blogpost(blogpost_id: int, db: Session = Depends(get_db)):
    blogpost = crud.get_blogpost(db=db, blogpost_id=blogpost_id)
    if blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blogpost

@app.put("/blogposts/{blogpost_id}", response_model=schemas.BlogPost)
def update_blogpost(blogpost_id: int, blogpost: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    updated_blogpost = crud.update_blogpost(db=db, blogpost_id=blogpost_id, blogpost=blogpost)
    if updated_blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return updated_blogpost

@app.delete("/blogposts/{blogpost_id}")
def delete_blogpost(blogpost_id: int, db: Session = Depends(get_db)):
    if not crud.delete_blogpost(db=db, blogpost_id=blogpost_id):
        raise HTTPException(status_code=404, detail="Blog post not found")
    return {"detail": "Blog post deleted"}

# Contact endpoints
@app.post("/contacts/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contact=contact)

@app.get("/contacts/", response_model=List[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contacts(db=db, skip=skip, limit=limit)

@app.get("/contacts/{contact_id}", response_model=schemas.Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.put("/contacts/{contact_id}", response_model=schemas.Contact)
def update_contact(contact_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    updated_contact = crud.update_contact(db=db, contact_id=contact_id, contact=contact)
    if updated_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated_contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    if not crud.delete_contact(db=db, contact_id=contact_id):
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"detail": "Contact deleted"}
