from sqlalchemy.orm import Session
from models import Project, BlogPost, Contact
from schemas import ProjectCreate, BlogPostCreate, ContactCreate

# CRUD operations for Project
def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Project).offset(skip).limit(limit).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, project: ProjectCreate):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project is None:
        return None
    for key, value in project.dict().items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return True
    return False

# CRUD operations for BlogPost
def create_blogpost(db: Session, blogpost: BlogPostCreate):
    db_blogpost = BlogPost(**blogpost.dict())
    db.add(db_blogpost)
    db.commit()
    db.refresh(db_blogpost)
    return db_blogpost

def get_blogposts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(BlogPost).offset(skip).limit(limit).all()

def get_blogpost(db: Session, blogpost_id: int):
    return db.query(BlogPost).filter(BlogPost.id == blogpost_id).first()

def update_blogpost(db: Session, blogpost_id: int, blogpost: BlogPostCreate):
    db_blogpost = db.query(BlogPost).filter(BlogPost.id == blogpost_id).first()
    if db_blogpost is None:
        return None
    for key, value in blogpost.dict().items():
        setattr(db_blogpost, key, value)
    db.commit()
    db.refresh(db_blogpost)
    return db_blogpost

def delete_blogpost(db: Session, blogpost_id: int):
    db_blogpost = db.query(BlogPost).filter(BlogPost.id == blogpost_id).first()
    if db_blogpost:
        db.delete(db_blogpost)
        db.commit()
        return True
    return False

# CRUD operations for Contact
def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Contact).offset(skip).limit(limit).all()

def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, contact: ContactCreate):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        return None
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
        return True
    return False
