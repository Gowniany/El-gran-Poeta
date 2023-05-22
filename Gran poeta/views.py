from flet import *
from Login import *  
from Menu import *
from Product_create import *


def views_handler(page):
  return {
    '/':View(bgcolor ="#1f262f", horizontal_alignment = 'center' ,vertical_alignment = 'center',
        route='/',
        controls=[
          Login(page)  
        ]
      ),
    '/menu':View(bgcolor ="#1f262f", horizontal_alignment = 'center' ,vertical_alignment = 'center',
        route='/menu',
        controls=[
          Menu(page)
        ]
      ),
      '/menu/product_create':View(bgcolor ="#1f262f", horizontal_alignment = 'center' ,vertical_alignment = 'center',
        route='/product_create',
        controls=[
          Product_create(page)
        ]
      )
  }