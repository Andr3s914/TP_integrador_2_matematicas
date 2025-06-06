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