from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Menu(Base):
    """
    Модель меню
    """
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)  # Первичный ключ
    title = Column(String, nullable=False)  # Название
    description = Column(String, nullable=False)  # Описание


class Submenu(Base):
    """
    Модель подменю
    """
    __tablename__ = 'submenu'
    id = Column(Integer, primary_key=True)  # Первичный ключ
    title = Column(String, nullable=False)  # Название
    description = Column(String, nullable=False)  # Описание
    menu = Column(Integer, ForeignKey("menu.id", ondelete='cascade'))  # Связь с меню


class Dish(Base):
    """
    Модель блюда
    """
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True)  # Первичный ключ
    title = Column(String, nullable=False)  # Название
    description = Column(String, nullable=False)  # Описание
    price = Column(Float, nullable=False)  # Стоимость
    submenu = Column(Integer, ForeignKey("submenu.id", ondelete='cascade'))  # Связь с подменю
