plazas = int(input("Ingrese el número de asientos\n"))
plazas_vendidas = 0
plazas_max = int(plazas)
valor_texto = 0

vender = True

def venta_billete(plazas, plazas_vendidas):
    tickets = int(input())
    if tickets <= plazas:
        plazas_vendidas += tickets
        plazas -= plazas_vendidas
    else:
        print("Error")
    return plazas, plazas_vendidas

def devolucion(plazas, plazas_vendidas):
    tickets = int(input())
    if tickets <= plazas_vendidas:
        plazas_vendidas -= tickets
        plazas += tickets
    else:
       plazas=plazas 
    return plazas, plazas_vendidas


print("1.- Venta de billetes.")
print("2.- Devolución de billetes.")
print("3.- Estado de la venta.")
print("0.- Salir.")

while vender:
    opcion = input()
    if opcion == "1":
        plazas, plazas_vendidas = venta_billete(plazas, plazas_vendidas)
        print("Venta realizada")
        print(f"Se vendieron: {plazas_vendidas}")
    elif opcion == "2":
        plazas, plazas_vendidas = devolucion(plazas, plazas_vendidas)
        print("Devolución realizada")
        print(f"Se devolvieron: {plazas}")
    elif opcion == "3":
        print("Estado de la venta")
        print(f"Total: {plazas_max}")
        print(f"Libre: {plazas}")
        print(f"Vendido: {plazas_vendidas}")
    elif opcion == "0":
        vender = False


    