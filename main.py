import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Dish as DishModel
from models import Menu as MenuModel
from models import Submenu as SubmenuModel
from schema import Dish as DishSchema
from schema import Menu as MenuSchema
from schema import Submenu as SubmenuSchema

load_dotenv('.env')
app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def root():
    return {"message": "hello world"}


"""
Реализация CRUD для каждой из моделей
"""


# Создание меню
@app.post("/api/v1/menus/", response_model=MenuSchema)
async def menu_create(menu: MenuSchema):
    db_menu = MenuModel(title=menu.title, description=menu.description)
    db.session.add(db_menu)
    db.session.commit()
    return db_menu


# Просмотр всего списка меню
@app.get("/api/v1/menus/")
async def menu_list():
    menu = db.session.query(MenuModel).all()
    return menu


# Просмотр конкретного элемента меню
@app.get('/api/v1/menus/{menu_id}', response_model=MenuSchema)
async def menu_get(menu_id: int):
    menu_item = db.session.query(MenuModel).filter(MenuModel.id == menu_id).first()
    return menu_item


# Изменение меню
@app.patch('/api/v1/menus/{menu_id}', response_model=MenuSchema)
async def menu_update(menu_id: int, title: str, description: str):
    menu_item = db.session.query(MenuModel).filter(MenuModel.id == menu_id).first()
    menu_item.title = title
    menu_item.description = description
    db.session.commit()
    return menu_item


# удаление меню
@app.delete('/api/v1/menus/{menu_id}')
async def menu_delete(menu_id: int):
    menu_item = db.session.query(MenuModel).filter(MenuModel.id == menu_id).first()
    db.session.delete(menu_item)
    db.session.commit()
    return {"message": "Item deleted successfully"}


# Создание подменю
@app.post("/submenu/", response_model=SubmenuSchema)
async def submenu_create(submenu: SubmenuSchema):
    db_submenu = SubmenuModel(title=submenu.title, description=submenu.description, menu=submenu.menu)
    db.session.add(db_submenu)
    db.session.commit()
    return db_submenu


# Просмотр всех подменю
@app.get('/submenu/')
async def submenu_list():
    submenu = db.session.query(SubmenuModel).all()
    return submenu


# Просмотр конкретного подменю
@app.get('/submenu/{submenu_id}', response_model=SubmenuSchema)
async def submenu_get(submenu_id: int):
    submenu_item = db.session.query(SubmenuModel).filter(SubmenuModel.id == submenu_id).first()
    return submenu_item


# Изменение подменю
@app.patch('/submenu/{submenu_id}', response_model=SubmenuSchema)
async def submenu_update(submenu_id: int, title: str, description: str, menu: int):
    submenu_item = db.session.query(SubmenuModel).filter(SubmenuModel.id == submenu_id).first()
    submenu_item.title = title
    submenu_item.description = description
    submenu_item.menu = menu
    db.session.commit()
    return submenu_item


# Удаление подменю
@app.delete('/submenu/{submenu_id}')
async def submenu_delete(submenu_id: int):
    submenu_item = db.session.query(SubmenuModel).filter(SubmenuModel.id == submenu_id).first()
    db.session.delete(submenu_item)
    db.session.commit()
    return {"message": "Item deleted successfully"}


# Создание блюда
@app.post("/dish/", response_model=DishSchema)
async def dish_create(dish: DishSchema):
    db_dish = DishModel(title=dish.title, description=dish.description, price=dish.price, submenu=dish.submenu)
    db.session.add(db_dish)
    db.session.commit()
    return db_dish


# Просмотр всех блюд
@app.get('/dish/')
async def dish_list():
    dish = db.session.query(DishModel).all()
    return dish


# Просмотр конкретного блюда
@app.get('/dish/{dish_id}', response_model=DishSchema)
async def dish_get(dish_id: int):
    dish_item = db.session.query(DishModel).filter(DishModel.id == dish_id).first()
    return dish_item


# Изменение блюда
@app.patch('/dish/{dish_id}', response_model=DishSchema)
async def dish_update(dish_id: int, title: str, description: str, price: float, submenu: int):
    dish_item = db.session.query(DishModel).filter(DishModel.id == dish_id).first()
    dish_item.title = title
    dish_item.description = description
    dish_item.price = price
    dish_item.submenu = submenu
    db.session.commit()
    return dish_item


# Удаление блюда
@app.delete('/dish/{dish_id}')
async def dish_delete(dish_id: int):
    dish_item = db.session.query(DishModel).filter(DishModel.id == dish_id).first()
    db.session.delete(dish_item)
    db.session.commit()
    return {"message": "Item deleted successfully"}
