from flet import *
import mysql.connector
from time import sleep


class Product_create(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.conectiondb = self.conex()

        self.nameproducto = TextField(label="Nombre del producto", color="white")
        self.tipoproducto = TextField(label="Libro,Revista,Enciclopedia", color="white")
        self.autor = TextField(label="Autor del prducto", color="white")
        self.editorial = TextField(label="Editorial", color="white")   
        self.descripcion = TextField(label="Descripcion producto", color="white")
        self.estadoinsert = Text(color="white") 

        self.insertbutton = ElevatedButton(
            bgcolor="blue900",
            on_click=self.insertbt,
            content=Container(content=Column([Text(value="Entrar", size=30, color="white")]))) 
          

        self.menu =    ElevatedButton(
            bgcolor="blue900",
            on_click=self.page.go("/menu"),
            content=Container(content=Column([Text(value="Entrar", size=30, color="white")])))              

    def conex(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="ADM",
                password="123",
                database="app_da"
            )
            return mydb
        except Exception as ex:
            print("Error de conexión:", ex)
    

    
    def build(self):
    
        return Card(
            width=600,
            height=700,
            elevation=15,
            content=Container(
                bgcolor="#23262a",
                border_radius=6,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Divider(height=25, color="transparent"),
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=2,
                            controls=[ 
                                Text("Ingresar productos", size=40, weight="bold", color="white"),
                            ],
                        ),           
                        Column(
                            width=350,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=25,
                            controls=[ 
                                self.nameproducto,
                                self.tipoproducto,
                                self.autor,
                                self.editorial,
                                self.descripcion,

                            ],
                        ),
                        self.insertbutton,
                        self.menu,     
                        self.estadoinsert
                    ]           
                ),
            )
        )


    def insertbt(self,conectiondb):
        try:
            conectiondb=self.conex()
            cursor = conectiondb.cursor()
            query = "INSERT INTO Productos (nombre_producto ,tipo, descripcion) VALUES('%s','%s', '%s'); INSERT INTO autores (nombre) VALUES('%s'); INSERT INTO editoriales (nombre) VALUES('%s');"
            cursor.execute(query, (self.nameproducto, self.tipoproducto.value,self.nameproducto,self.autor,self.editorial))
            result = cursor.fetchall()
            cursor.close()
            if result:
                self.estadoinsert.value = ("Se pudo ingresar este producto correctamente!")
                sleep(1)
            else:
                self.estadoinsert.value = ("No se pudo ingresar este producto!")        
        except Exception as ex:
            print("Error de conexión:", ex)