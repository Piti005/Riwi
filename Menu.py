Inventario = {}

def mostrar_menu ():
    print ("\n----- Menú Principal -----" )
    print ("1) Agrega un producto")
    print ("2) Mostrar inventario")
    print ("3) Actualizar inventario")
    print ("4) Eliminar un producto")
    print ("5) SALIR")

while True:
    mostrar_menu ()
    opcion = input ("Elige una opción: ")

    if opcion == "1":
        nombre = input ("¿Cual es el nombre del producto?: ")
        cantidad = input ("¿Que cantidad vas a ingresar?: ")
        Inventario [nombre] = cantidad
        print (f"{nombre} fue ingresado con {cantidad} unidades")
    
    elif opcion == "2":
        if not Inventario:
            print ("El inventario está vacío, ingresa un producto")
        else: 
            print ("\n----- Inventario actual -----")
            for producto, cantidad in Inventario.items():
                print (f"{producto}: {cantidad} unidades")

    elif opcion == "3":
        nombre = input("¿Que producto vas a actualizar?: ")
        if nombre in Inventario:
            nueva_cantidad = int (input("Nueva cantidad"))
            Inventario [nombre] = nueva_cantidad
            print (f"{nombre} actualizado a {nueva_cantidad} unidades")
        else:
            print ("El producto no existe, intentalo nuevamente")

    elif opcion == "4":
        nombre = input ("¿Que producto vas a eliminar?: ")
        if nombre in Inventario:
            del Inventario [nombre]
            print (f"{nombre} Fue eliminado correctamente")
        else:
            print ("El producto no existe")
    elif opcion == "5":
        print ("Vuelve pronto...")
        break
    else:
        print ("Error de acceso, vuelve a intentarlo")
