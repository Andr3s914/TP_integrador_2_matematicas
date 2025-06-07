# Función para obtener un conjunto de dígitos únicos a partir de un DNI
def obtener_conjunto_digitos(dni):
    return set(str(dni))  # Convierte el número en string y extrae los dígitos únicos

# Ingreso de los DNIs
dni_1 = input("Ingrese el primer DNI: ")
dni_2 = input("Ingrese el segundo DNI: ")

# Generación automática de conjuntos
A = obtener_conjunto_digitos(dni_1)
B = obtener_conjunto_digitos(dni_2)

# Operaciones con conjuntos
union = A | B
interseccion = A & B
diferencia_A_B = A - B
diferencia_B_A = B - A
diferencia_simetrica = A ^ B

# Conteo de frecuencia de cada dígito
frecuencia_A = {digito: dni_1.count(digito) for digito in A}
frecuencia_B = {digito: dni_2.count(digito) for digito in B}

# Suma total de los dígitos
suma_A = sum(int(digito) for digito in dni_1)
suma_B = sum(int(digito) for digito in dni_2)

# Evaluación de condiciones lógicas
if interseccion:
    print("Dígito compartido:", interseccion)

if len(A) > 6:
    print("Diversidad numérica alta en A")

if len(B) > 6:
    print("Diversidad numérica alta en B")

# Impresión de resultados
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia A - B: {diferencia_A_B}")
print(f"Diferencia B - A: {diferencia_B_A}")
print(f"Diferencia Simétrica: {diferencia_simetrica}")
print(f"Frecuencia de dígitos en A: {frecuencia_A}")
print(f"Frecuencia de dígitos en B: {frecuencia_B}")
print(f"Suma de dígitos en A: {suma_A}")
print(f"Suma de dígitos en B: {suma_B}")


# Parte2: Operaciones con años de nacimiento

# Funcion para determinar si un año es bisiesto
def es_bisiesto(anio):
    return(anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Ingreso valido de años de nacimiento
num_integrantes = 2
anios = []

for i in range(num_integrantes):
    valido = False 
    while not valido:
        anio_input = input(f"Por favor, ingrese el año de nacimiento del integrante {i+1}: ")
        if anio_input.isdigit():
            anio = int(anio_input)
            if anio in anios:
                print("Año repetido, ingrese por favor un año ficticio diferente.")
            else:
                anios.append(anio)
                valido = True
        else:
            print("Entrada inválida. Ingrese un número válido.")

# Contar cuántos nacieron en años pares e impares
pares = 0
impares = 0
for anio in anios:
    if anio % 2 == 0:
        pares += 1
    else: 
        impares +=1

print(f"Años pares: {pares}")
print(f"Años impares: {impares}")

# Ver si nacieron después del 2000
if all(anio > 2000 for anio in anios):
  print("Grupo Z")

# Ver si alguno nació en año bisiesto
if any(es_bisiesto(anio) for anio in anios):
  print("Tenemos un año especial")

# Ingreso de edades
edades = []
for i in range(num_integrantes):
  valido = False 
  while not valido:
    edad_input = input(f"Por favor, ingrese la edad actual del integrante {i+1}: ")
    if edad_input.isdigit():
      edades.append(int(edad_input))
      valido = True
    else:
      print("Entrada inválida. Por favor. ingrese un número válido.")

# Producto cartesiano
producto_cartesiano = [(anio, edad) for anio in anios for edad in edades]

print("Producto cartesiano: ")
for par in producto_cartesiano:
  print(par)