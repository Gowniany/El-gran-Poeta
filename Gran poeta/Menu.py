from flet import *

class Menu(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    



  def build(self):

    volver=ElevatedButton(
              bgcolor="blue900",
              on_click=(lambda _: self.page.go("/")),
              content=Container(
              content=Column([Text(value="volver al inicio", size=40,color="white")])
              ))
    
    insertarproductos=ElevatedButton(
              bgcolor="blue900",
              on_click=lambda _: self.page.go("/productos_create"),
              content=Container(
              content=Column([Text(value="Ingresar libros", size=40,color="white")])
              ))
    
    ingresarbodega=ElevatedButton(
              bgcolor="blue900",
              on_click=(),
              content=Container(
              content=Column([Text(value="Ingresar bodega", size=40,color="white")])
              ))
    generarinforme=ElevatedButton(
              bgcolor="blue900",
              on_click=(),
              content=Container(
              content=Column([Text(value="Generar informe", size=40,color="white")])
              ))
    
    return Card(
           width=400,
           height=600,
           elevation=15,
           content=Container(
              bgcolor="#23262a",
              border_radius=6,
              content=Column(
                 horizontal_alignment=CrossAxisAlignment.CENTER,
                 controls=[
                    Divider(height=25,color="transparent"),
                    Column(
                       alignment=MainAxisAlignment.CENTER,
                       horizontal_alignment=CrossAxisAlignment.CENTER,
                       spacing=40,
                       controls=[ 
                         Text("Bienvenido al Menu",size=40,
                         weight="bold",color="white"),
                        Column(
                         alignment=MainAxisAlignment.CENTER,
                         horizontal_alignment=CrossAxisAlignment.CENTER,
                         spacing=60,
                         controls=[ 
                         volver,
                         insertarproductos,
                         ingresarbodega,
                         generarinforme,
                        
                         ]
                        )
                        ]
                        ),
                ]
              )
           )
        )
    