from sqlalchemy.orm import Session

from . import models, schemas


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def get_client_by_tel(db: Session, tel: str):
    return db.query(models.Client).filter(models.Client.tel == tel).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(email=client.email, tel=client.tel)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_standard_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StandardRecipe).offset(skip).limit(limit).all()


def create_standard_recipe(db: Session, recipe: schemas.StandardRecipeCreate, client_id: int):
    db_recipe = models.StandardRecipe(**recipe.dict(), client_id=client_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def get_bifocal_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BifocalRecipe).offset(skip).limit(limit).all()


def create_bifocal_recipe(db: Session, recipe: schemas.BifocalRecipeCreate, client_id: int):
    db_recipe = models.BifocalRecipe(**recipe.dict(), client_id=client_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe
