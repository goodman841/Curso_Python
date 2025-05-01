nombre = input("Por favor escribe tu nombre: ")
ventas=input("Ventas totales del mes: ")

ventas =int(ventas)

comision= ventas*0.13

comision=round(comision)

print(f"hola {nombre}, tus comisiones de este mes son de ${comision}")