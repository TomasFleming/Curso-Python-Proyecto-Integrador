import sqlite3 as sql
#METODO PARA crear la base de datos
def createDB():
    conn = sql.connect ("Mercado.db")
    conn.commit()
    conn.close()
#METODO PARA CREAR LA TABLA
#def createTable():
#    conn = sql.connect("Mercado.db")
#    cursor = conn.cursor()
#    cursor.execute(
#       """CREATE TABLE Productos(
#            producto_id integer primary key AUTOINCREMENT,
#            NOMBRE_PRODUCTO TEXT,
#           CANTIDAD_PRODUCTO int,
#            PRECIO_PRODUCTO float,
#            CATEGORIA_PRODUCTO char
#        )"""
#    )
    #commit realiza los cambios
#    conn.commit()
#   conn.close()

#createDB()
#createTable()

#conec = sql.connect("Productos.db")
#cur = conec.cursor()

#cur.execute(
#        """Select* from Productos"""
#    )

#cambiarlo para que le de los datos
def insertarProducto(NombProd,Cantidad,Precio,Categoria):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = "INSERT INTO Productos(PRODUCTO_nom,CANTIDAD,PRECIO_PRODUCTO,CAT_ID,Estado) VALUES('"+str(NombProd)+"',"+str(Cantidad)+","+str(Precio)+","+str(Categoria)+",'habilitado')"
    cursor.execute(consulta)
    conn.commit()
    conn.close()
def ConstProdID(ID_producto):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """select P.ID,PRODUCTO_nom,Cat_nom,CANTIDAD,PRECIO_PRODUCTO  from Productos P inner join Categorias C on P.CAT_ID=C.ID where P.ID='"""+str(ID_producto)+"' or PRODUCTO_nom like '%"+str(ID_producto)+"%' or Cat_nom like '%"+str(ID_producto)+"%'"
    cursor.execute(consulta)
    product= cursor.fetchall()
    print()
    print("(ID-NOMBRE-CATEGORIA-CANTIDAD-PRECIO)")
    for i in product:
        print("("+str(i[0])+") "+str(i[1])+" - "+str(i[2])+" - "+str(i[3])+" - $"+str(i[4]))
    conn.commit()
    conn.close()
def VerifProd(ID_producto):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    Verf=False
    consulta = """select P.ID,PRODUCTO_nom,Cat_nom,CANTIDAD,PRECIO_PRODUCTO  from Productos P inner join Categorias C on P.CAT_ID=C.ID where Estado='habilitado' and P.ID='""" + str(
        ID_producto) + "' or PRODUCTO_nom like '%" + str(ID_producto) + "%' or Cat_nom like '%" + str(
        ID_producto) + "%'"
    cursor.execute(consulta)
    product = cursor.fetchall()
    for i in product:
        Verf=True
    if(Verf==True):
        print()
        print("(ID-NOMBRE-CATEGORIA-CANTIDAD-PRECIO)")
        for i in product:
            print("(" + str(i[0]) + ") " + str(i[1]) + " - " + str(i[2]) + " - " + str(i[3]) + " - $" + str(i[4]))
    else:
        print()
        print("No Existe un producto con ID igual a "+str(ID_producto)+" o no se encuentra disponible para comprar....")
    conn.commit()
    conn.close()
    return Verf
def EditarProd(ID):
    ConstProdID(ID)
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = ""
    print("""Que dato desea editar del producto: 
1.Nombre
2.Cantidad
3.Precio
4.Categoria
5.Eliminar
    """)
    Respuesta=int(input("Ingresar respuesta"))
    if (Respuesta==2):
        a=int(input("Ingrese la cantidad nueva:"))
        consulta="update Productos set CANTIDAD="+str(a)+" where ID="+str(ID)
    elif(Respuesta==3):
        a = float(input("Ingrese el precio nuevo:"))
        consulta = "update Productos set PRECIO_PRODUCTO=" + str(a)+" where ID="+str(ID)
    elif(Respuesta==4):
        a = int(input("Ingrese la id de la nueva categoria:"))
        consulta = "update Productos set CAT_ID=" + str(a)+" where ID="+str(ID)
    elif(Respuesta==1):
        a = str(input("Ingrese el nuevo nombre: "))
        consulta = "update Productos set PRODUCTO_nom='" + str(a)+"' where ID="+str(ID)
    elif (Respuesta == 5):
        consulta = "update Productos set Estado='deshab' where ID=" + str(ID)
    cursor.execute(consulta)
    conn.commit()
    conn.close()
    print("Datos Cambiados Correctamente")
import sqlite3 as sql

def TablaCategorias():
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Categorias(
            ID integer primary key AUTOINCREMENT,
            Cat_nom varchar(30) not null,
            Descripcion varchar(200) not null
        )"""
    )
    conn.commit()
    conn.close()
def Insert_Cat(Nombre):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    Descripcion=str(input("Ingrese una descripcion de la categoria:"))
    consulta = """INSERT INTO Categorias(Cat_nom,Descripcion)
    VALUES('"""+str(Nombre)+"','"+Descripcion+"')"
    cursor.execute(consulta)
    conn.commit()
    conn.close()
def Edit_Cat(ID):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    Busc_Cat(ID)
    consulta = ""
    print("""Que Dato desea cambiar de la categoria:
    1.Nombre
    2.Descripcion
    3.Eliminar
    """)
    a=int(input("Ingrese su respuesta :"))
    if(a==1):
        consulta = "update Categorias set Cat_nom='"+str(input("Ingrese el nuevo nombre: "))+"' where ID="+str(ID)
    elif(a==2):
        consulta = "update Categorias set Descripcion='"+str(input("Ingrese la nueva descripcion: "))+"' where ID="+str(ID)
    elif(a==3):
        consulta = "delete from Categorias where ID="+str(ID)
    cursor.execute(consulta)
    conn.commit()
    conn.close()
    print("Datos Cambiados Correctamente")
def Busc_Cat(ID):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """select* from Categorias where Cat_nom like '%""" + str(ID) + "%' or ID='" + str(
        ID)+"'"
    cursor.execute(consulta)
    product = cursor.fetchall()
    print()
    print("(ID-NOMBRE-Descripcion)")
    for I in product:
        print("("+str(I[0])+") - "+str(I[1])+" - "+str(I[2]))
    conn.commit()
    conn.close()

def TablaProductos():
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Productos(
            ID integer primary key AUTOINCREMENT,
            PRODUCTO_nom varchar(30) not null,
            CAT_ID int not null,
            CANTIDAD int not null,
            Estado varchar(20) not null,
            PRECIO_PRODUCTO float not null
        )"""
        #alter table Productos add constraint fkID_cats foreign key(CAT_ID) references Categorias(ID)
        #"""
    )
    #commit realiza los cambios
    conn.commit()
    conn.close()

def TablaUsuario():
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Usuarios(
            ID integer primary key AUTOINCREMENT,
            Usuario_nom varchar(20) not null,
            Contraseña varchar(20) not null,
            Correo varchar(30) not null,
            Fecha_naci date,
            Estado varchar(20) not null,
            Categoria varchar(20) not null
        )"""
    )
    #commit realiza los cambios
    conn.commit()
    conn.close()
def InsertUsuario(Nombre,Contraseña,Correo):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """INSERT INTO Usuarios(Usuario_nom,Contraseña,Correo,Categoria,Estado)
    VALUES('"""+Nombre+"','"+Contraseña+"','"+Correo+"','Admin','Habilitado')"
    cursor.execute(consulta)
    conn.commit()
    conn.close()
def InsertUsuarioNomal(Nombre,Contraseña,Correo):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """INSERT INTO Usuarios(Usuario_nom,Contraseña,Correo,Categoria,Estado)
    VALUES('"""+Nombre+"','"+Contraseña+"','"+Correo+"','normal','Habilitado')"
    cursor.execute(consulta)
    conn.commit()
    conn.close()
def busc_Usu(Nombre):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """select Usuario_nom,Correo from Usuarios where Correo='""" + str(Nombre) + "'"
    cursor.execute(consulta)
    product = cursor.fetchall()
    #print("ID-NOMBRE-Correo")
    #print(product)
    conn.commit()
    conn.close()
    rt=True
    for i in product:
        rt=False
    if(rt==True):
        return True#esta bien por que no hay nadie con ese mail
    else:
        return False#ya existe el mail
def bus_usuariobien(ID):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """select ID,Usuario_nom,Correo,Estado,Categoria from Usuarios where Correo='""" + str(ID) + "' or ID='"+str(ID)+"' or Usuario_nom like'%"+str(ID)+"%' "
    cursor.execute(consulta)
    product = cursor.fetchall()
    print()
    print("(ID-NOMBRE-Correo-Estado-Categoria)")
    for i in product:
        print("("+str(i[0])+") - "+str(i[1])+" - "+str(i[2])+" - "+str(i[3])+" - "+str(i[4])+" - ")
    conn.commit()
    conn.close()
def Edit_usu():
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    ID=(input("Ingrese la id del usuario a cambiar:"))
    bus_usuariobien(ID)
    consulta = ""
    print("""Que Dato desea cambiar del usuario 
        1.Nombre
        2.Correo
        3.Eliminar
Ingrese su respuesta:""")
    a = int(input())
    if (a == 1):
        consulta = "update Usuarios set Usuario_nom='" + str(input("Ingrese el nuevo nombre: ")) + "' where ID=" + str(ID)
    elif (a == 2):
        Correo=str(input("Ingrese el nuevo correo: "))
        while (VerifiCorreo(Correo) != True):
            Correo = str(input("Ingrese el correo del usuario: "))
        consulta = "update Usuarios set Correo='" + Correo + "' where ID=" + str(ID)
    elif (a == 3):
        consulta = "update Usuarios set Estado='desabah' where ID=" + str(ID)
    cursor.execute(consulta)
    conn.commit()
    conn.close()
    print("Datos Cambiados Correctamente")
def VerifiCorreo(Correo):
    arroba=False
    punto=False
    valido=False
    Nuevo=False
    for i in range (len(Correo)):
        if(Correo[i]=="@" and i!=0):
            arroba=True
        if(arroba==True):
            if(Correo[i]=="."):
                punto=True
        if(arroba==True and punto==True):
            valido=True
    if(valido==True):
        Verif=busc_Usu(Correo)
        if(Verif!=True):
            Nuevo=False
            print("Ya hay un usuario registrado con ese correo")
        else:
            Nuevo=True
    else:
        print("El correo no es Valido")
    return Nuevo

def PrecioProd(ID,Cant):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    cursor.execute("Select PRECIO_PRODUCTO from Productos where ID="+str(ID))
    Precio = float(float((cursor.fetchone())[0])*int(Cant))
    conn.commit()
    conn.close()
    return Precio
def GuardarVenta(Usuario,Total):
    from datetime import datetime
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta ="insert into Ventas(Usuario,Total,Fecha) values("+str(Usuario)+","+str(Total)+",'"+str(datetime.now())+"')"
    cursor.execute(consulta)
    cursor.execute("select MAX(ID) from Ventas")
    ID_venta=int(cursor.fetchone()[0])
    conn.commit()
    conn.close()
    return  ID_venta
def TablaVentas():
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    cursor.execute(
        """create table Ventas(
            ID integer primary key AUTOINCREMENT,
            Usuario int not null,
            Total float not null,
            Fecha datetime not null
            )"""
    )
    # commit realiza los cambios
    conn.commit()
    conn.close()

def GuardarDetalle(Venta,Producto,Cantidad,Precio):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = "insert into DetalleV(ID_Venta,ID_Prod,Cant_comp,Precio_momento) values("+str(Venta)+","+str(Producto)+","+str(Cantidad)+","+str(Precio)+")"
    cursor.execute(consulta)
    conn.commit()
    conn.close()
def tb_detalleVenta():
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    cursor.execute(
        """create table DetalleV(
            ID integer primary key AUTOINCREMENT,
            ID_Venta int not null,
            ID_Prod int not null,
            Cant_comp int not null,
            Precio_momento float not null
            )"""
    )
    # commit realiza los cambios
    conn.commit()
    conn.close()

def VerCompras(UsuID):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = "select V.ID,Usuario_nom,Total,DATE(Fecha) from Ventas V inner join Usuarios U on V.Usuario=U.ID where Usuario="+str(UsuID)+" order by 4 DESC"
    cursor.execute(consulta)
    product = cursor.fetchall()
    print()
    print("(ID-Usuario-Total-Fecha)")
    for i in product:
        print(i)
    conn.commit()
    conn.close()
def VerDetalle(VentaID):
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = """select P.PRODUCTO_nom,DT.Cant_comp,Precio_momento from DetalleV DT inner join Ventas V on DT.ID_Venta=V.ID
     inner join Productos P on DT.ID_Prod=P.ID where V.ID=""" + str(VentaID)
    cursor.execute(consulta)
    product = cursor.fetchall()
    print("(Producto-Cantidad-PrecioTotal)")
    for i in product:
        print(str(i[0])+" - "+str(i[1])+" - $"+str(i[2]))
    conn.commit()
    conn.close()

def ActuaStock(ID,Cantidad):
    print()
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta = "update Productos set CANTIDAD=(CANTIDAD-"+str(Cantidad)+") where ID="+str(ID)
    cursor.execute(consulta)
    conn.commit()
    conn.close()
def VerifCant(ID,Cantidad):
    print()
    conn = sql.connect("Mercado.db")
    cursor = conn.cursor()
    consulta="Select CANTIDAD from Productos where ID="+str(ID)
    cursor.execute(consulta)
    product = cursor.fetchall()
    V=""
    C=int(Cantidad)
    a=int(product[0][0])
    if(a>=C):
        V=True
    else:
        V=False
    conn.commit()
    conn.close()
    return V


ListaCompra=[]
band= False
print("¡Bienvenido a nuestra Tienda!")
while(band==False):
    try:
        print("""
¿A que menu quiere acceder?
1.Productos
2.Datos de Usuarios
3.Registrar Compra
4.Salir (o cualquier otro numero)

Ingrese su respuesta:
            """)
        R = int(input())
        if (R == 1):  # -------------------------------------------MENU PRODUCTO-------------------------------------------------
            print("""MENU PRODUCTOS---------------------------------------
1.Agregar Producto Nuevo
2.Ver Producto
3.Editar Producto
4.Categorias
5.Volver

Ingrese su respuesta:
                    """)
            ProdResp = int(input())
            if (ProdResp == 1):  # INSERTAR PRODUCTO
                print()
                print("AGREGAR PRODUCTO....")
                Nombre = str(input("Ingrese el nombre del producto nuevo: "))
                Cantidad = int(input("Ingrese la cantidad a guardar del nuevo producto: "))
                Precio = float(input("Ingrese el precio del nuevo producto: "))
                print("""A continuacion, las Categorias que se encuentran disponibles para asignar:""")
                Busc_Cat("")
                Cat = int(input("Ingrese la ID de Categoria del producto: "))
                insertarProducto(Nombre, Cantidad, Precio, Cat)
                print("Se ha registrado el Producto " + str(Nombre) + " correctamente")
            elif (ProdResp == 2):  # BUSCAR PRODUCTO
                print()
                print("BUSCAR PRODUCTO....")
                Nombre = str(input("Ingrese la ID o nombre del Producto :"))
                ConstProdID(Nombre)
            elif (ProdResp == 3):  # EDITAR PRODUCTO
                print()
                print("EDITAR PRODUCTO....")
                ID = int(input("Ingrese la ID del producto a editar: "))
                EditarProd(ID)
            elif (ProdResp == 4):  # -------------------------------------------MENU CATEGORIAS-----------------------
                print("""Menu Categorias----------------------------------------------------------
1.Insertar Categoria
2.Ver Categoria
3.Editar Categoria
4.Volver""")
                print("Ingrese su respuesta:")
                RC = int(input())
                if (RC == 1):
                    print()
                    print("AGREGAR CATEGORIA....")
                    Nomb_cat = str(input("Ingrese el nombre de la nueva categoria: "))
                    Insert_Cat(Nomb_cat)
                elif (RC == 2):
                    print()
                    print("BUSCAR CATEGORIA....")
                    nc = str(input("Ingrse el nombre o ID de la cetegoria:"))
                    Busc_Cat(nc)
                elif (RC == 3):
                    print()
                    print("EDITAR CATEGORIA EXISTENTE....")
                    Edit_Cat(int(input("Ingrese la id de la categoria a cambiar:")))

        elif (R == 2):  # -------------------MENU USUARIOS-----------------------------------------------------
            print("""MENU Usuarios---------------------------------------
1.Agregar Nuevo Usuario
2.Ver Datos de usuarios
3.Ver compras de usuarios
4.Editar datos de usuario
5.Volver

Ingrese su respuesta:
                    """)
            UsuResp = int(input())
            if (UsuResp == 1):
                print()
                print("AGREGAR NUEVO USUARIO....")
                Nombre = str(input("Ingrese el nombre completo del usuario: "))
                Correo = str(input("Ingrese el correo del usuario: "))
                while (VerifiCorreo(Correo) != True):
                    Correo = str(input("Ingrese el correo del usuario: "))
                Contra = str(input("Ingrese una contraseña: "))
                InsertUsuario(Nombre, Contra, Correo)
                print("Usuario creado exitosamente...")
            elif (UsuResp == 2):
                print()
                print("VER DATOS DE USUARIO....")
                bus_usuariobien(input("Ingrese el nombre o Correo del usuario:"))
            elif (UsuResp == 3):
                print()
                print("VER COMPRAS DE USUARIO USUARIO....")
                VerCompras(int(input("Ingrese la ID del ususario:")))
                print()
                VerDetalle(int(input("Ingrese la ID de venta para ver detalle :")))
            elif (UsuResp == 4):
                print()
                print("EDITAR USUARIO....")
                Edit_usu()

        elif (R == 3):  # ---------------------------------------MENU PARA COMPRAS-----------------------------------------------
            Lista_Detalle = []
            ID_usu = input("""
USTED ESTA A PUNTO DE REALIZAR UNA COMPRA, POR FAVOR INGRESE LOS DATOS SOLICITADOS....


Ingrese la ID del usuario:""")
            AO = False
            Total = 0
            while (AO == False):
                print("""
1.Agregar un articulo a la lista
2.Ver Lista de compra
3.Terminar compra
""")
                respuesta = int(input("Seleccione una opcion:"))
                if (respuesta == 1):
                    print()
                    print("INGRESAR UN PRODUCTO....")
                    print()
                    LineaDetalle = {}
                    NumLinea = 0
                    ID_prod = int(input("Ingrese la ID del producto a comprar:"))
                    while(VerifProd(ID_prod)==False):
                        ID_prod = int(input("Ingrese la ID del producto a comprar:"))
                    Cantidad = int(input("Ingrese la candidad a comprar:"))
                    while(VerifCant(ID_prod,Cantidad)==False):
                        print("La cantidad que ingreso es superior a la cantidad disponible")
                        Cantidad = int(input("Por favor, reingrese la candidad a comprar:"))
                    LineaDetalle["ID"] = ID_prod
                    LineaDetalle["Cantidad"] = Cantidad
                    LineaDetalle["Precio Tot"] = PrecioProd(ID_prod, Cantidad)
                    Lista_Detalle.append(LineaDetalle)
                elif(respuesta==2):
                    print()
                    conect = sql.connect("Mercado.db")
                    cur=conect.cursor()
                    print("(Producto-CantidadComprar-PrecioTotal)")
                    for j in range(0,len(Lista_Detalle)):
                        consultDeta="select PRODUCTO_nom from Productos P inner join Categorias C on P.CAT_ID=C.ID where P.ID="+str(Lista_Detalle[j]["ID"])
                        cur.execute(consultDeta)
                        print()
                        T=cur.fetchall()
                        #print(T)
                        print(str(T[0][0])+" - "+str(Lista_Detalle[j]["Cantidad"])+" - $"+str(Lista_Detalle[j]["Precio Tot"]))
#                    print()
#                    print("Precio Total de la lista: $"+str(Total))
                    conect.close()
                elif(respuesta==3):
                    AO = True
            for i in range(len(Lista_Detalle)):
                Total = Total + (Lista_Detalle[i]["Precio Tot"])

            ID_Venta = GuardarVenta(ID_usu, Total)
            for i in range(len(Lista_Detalle)):
                Prd = Lista_Detalle[i]["ID"]
                Cant = Lista_Detalle[i]["Cantidad"]
                Pre = Lista_Detalle[i]["Precio Tot"]
                GuardarDetalle(ID_Venta, Prd, Cant, Pre)
                ActuaStock(Prd,Cant)

            print("La compra se ha guardado exitosamente")

        elif (R != 1 and R != 2 and R != 3):
            print("Codigo terminado...¡Gracias por usar nuestra pagina!")
            band = True
    except ValueError:
        print("Debe ingresar un valor numerico como respuesta, por favor vuelva a intententarlo....")


