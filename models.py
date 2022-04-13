import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import relationship

from .database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, index=True)
    tel = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    standard_recipes = relationship("StandardRecipe", back_populates="client")
    bifocal_recipes = relationship("BifocalRecipe", back_populates="client")


class StandardRecipe(Base):
    __tablename__ = "standard_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    added = Column(DateTime, default=datetime.datetime.utcnow)

    od_sph = Column(DECIMAL(4, 2))
    od_cyl = Column(DECIMAL(4, 2))
    od_axis = Column(Integer)
    od_prism = Column(String)
    od_base = Column(String)

    os_sph = Column(DECIMAL(4, 2))
    os_cyl = Column(DECIMAL(4, 2))
    os_axis = Column(Integer)
    os_prism = Column(String)
    os_base = Column(String)

    pd = Column(String)

    doctor = Column(String)
    remarks = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="standard_recipes")


class BifocalRecipe(Base):
    __tablename__ = "bifocal_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    added = Column(DateTime, default=datetime.datetime.utcnow)

    dv_od_sph = Column(DECIMAL(4, 2))
    dv_od_cyl = Column(DECIMAL(4, 2))
    dv_od_axis = Column(Integer)
    dv_os_sph = Column(DECIMAL(4, 2))
    dv_os_cyl = Column(DECIMAL(4, 2))
    dv_os_axis = Column(Integer)

    nv_od_sph = Column(DECIMAL(4, 2))
    nv_os_sph = Column(DECIMAL(4, 2))

    pd = Column(String)

    doctor = Column(String)
    remarks = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="bifocal_recipes")
