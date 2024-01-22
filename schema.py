from pydantic import BaseModel


class Menu(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class Submenu(BaseModel):
    title: str
    description: str
    menu: int

    class Config:
        orm_mode = True


class Dish(BaseModel):
    title: str
    description: str
    price: float
    submenu: int

    class Config:
        orm_mode = True
