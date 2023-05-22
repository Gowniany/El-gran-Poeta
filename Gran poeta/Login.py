from flet import *
import mysql.connector
from time import sleep


class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.conectiondb = self.conex()

        self.nametxt = TextField(label="Nombre", color="white")
        self.contraseñatxt = TextField(label="Contraseña", color="white", password=True, can_reveal_password=True)
        self.loginbutton = ElevatedButton(
            bgcolor="blue900",
            on_click=self.login_con,
            content=Container(content=Column([Text(value="Entrar", size=30, color="white")]))) 
        self.estadoconect = Text(color="white")   

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
        bonelord = Image(src="https://github.com/Gowniany/El-gran-Poeta/blob/main/Bonelord_Tome_2(1).gif?raw=true")
    
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
                        Divider(height=25, color="transparent"),
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=2,
                            controls=[ 
                                Text("El gran Poeta", size=40, weight="bold", color="white"),
                                Text("Aplicacion de Bodega", size=16, weight="bold", color="grey"),
                                bonelord
                            ],
                        ),           
                        Column(
                            width=350,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=25,
                            controls=[ 
                                self.nametxt,
                                self.contraseñatxt
                            ],
                        ),
                        self.loginbutton,     
                        self.estadoconect
                    ]           
                ),
            )
        )


    def login_con(self,conectiondb):
        try:
            conectiondb=self.conex()
            cursor = conectiondb.cursor()
            query = "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s"
            cursor.execute(query, (self.nametxt.value, self.contraseñatxt.value))
            result = cursor.fetchall()
            cursor.close()
            if result:
                sleep(1)
                self.page.go("/menu")
            else:
                self.estadoconect.value = ("Esa cuenta no existe!")        
        except Exception as ex:
            print("Error de conexión:", ex)