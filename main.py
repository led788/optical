from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_client(db=db, client=client)


@app.get("/clients/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@app.post("/clients/{client_id}/standard/", response_model=schemas.StandardRecipe)
def create_standard_for_client(
    client_id: int, recipe: schemas.StandardRecipeCreate, db: Session = Depends(get_db)
):
    return crud.create_standard_recipe(db=db, recipe=recipe, client_id=client_id)


@app.get("/standard/", response_model=list[schemas.StandardRecipe])
def read_standard_recipe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes = crud.get_standard_recipes(db, skip=skip, limit=limit)
    return recipes


# todo bifocal recipes ...
