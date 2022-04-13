import datetime
import decimal

from pydantic import BaseModel


# Standard recipe Pydantic model

class StandardRecipeBase(BaseModel):
    od_sph: decimal.Decimal
    od_cyl: decimal.Decimal
    od_axis: int
    od_prism: str
    od_base: str

    os_sph: decimal.Decimal
    os_cyl: decimal.Decimal
    os_axis: int
    os_prism: int
    os_base: str

    pd: str

    doctor: str
    remarks: str


class StandardRecipeCreate(StandardRecipeBase):
    pass


class StandardRecipe(StandardRecipeBase):
    id: int
    added: datetime

    class Config:
        orm_mode = True


# Bifocal recipe Pydantic model

class BifocalRecipeBase(BaseModel):
    dv_od_sph: decimal.Decimal
    dv_od_cyl: decimal.Decimal
    dv_od_axis: int
    dv_os_sph: decimal.Decimal
    dv_os_cyl: decimal.Decimal
    dv_os_axis: int

    nv_od_sph: decimal.Decimal
    nv_os_sph: decimal.Decimal

    pd: str

    doctor: str
    remarks: str


class BifocalRecipeCreate(BifocalRecipeBase):
    pass


class BifocalRecipe(BifocalRecipeBase):
    id: int
    added: datetime

    class Config:
        orm_mode = True


# Client Pydantic model

class ClientBase(BaseModel):
    email: str | None = None
    tel: str | None = None


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    created_at: datetime

    standard_recipes: list[StandardRecipe] = []
    bifocal_recipes: list[BifocalRecipe] = []

    class Config:
        orm_mode = True
