import streamlit as st


def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return precio_final

def sumar_lista(numeros):
    return sum(numeros)

def producto(nombre, cantidad=1, precio_por_unidad=10):
    return cantidad * precio_por_unidad

def numeros_pares_e_impares(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    if not args:
        return 1
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def informacion_personal(**kwargs):
    info = ""
    for clave, valor in kwargs.items():
        info += f"{clave}: {valor}\n"
    return info

def calculadora_flexible(num1, num2, operacion='suma'):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicación':
        return num1 * num2
    elif operacion == 'división':
        return num1 / num2
    else:
        return "Operación no válida"

st.title("Ejercicios Interactivos de Funciones en Python")
exercise = st.sidebar.selectbox("Selecciona un ejercicio", 
                                  ["Saludo", "Suma de dos números", 
                                   "Área de un triángulo", "Calculadora de descuento",
                                   "Suma de una lista", "Funciones con valores predeterminados",
                                   "Números pares e impares", "Multiplicación con *args",
                                   "Información personal con **kwargs", "Calculadora flexible"])

if exercise == "Saludo":
    nombre = st.text_input("Ingresa tu nombre:")
    if st.button("Saludar"):
        st.write(saludar(nombre))

elif exercise == "Suma de dos números":
    num1 = st.number_input("Ingresa el primer número:", 0)
    num2 = st.number_input("Ingresa el segundo número:", 0)
    if st.button("Sumar"):
        st.write("Resultado:", sumar(num1, num2))

elif exercise == "Área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo:", 0.0)
    altura = st.number_input("Ingresa la altura del triángulo:", 0.0)
    if st.button("Calcular área"):
        st.write("Área:", calcular_area_triangulo(base, altura))

elif exercise == "Calculadora de descuento":
    precio = st.number_input("Ingresa el precio original:", 0.0)
    descuento = st.number_input("Ingresa el descuento (%) [Opcional]", 10)
    impuesto = st.number_input("Ingresa el impuesto (%) [Opcional]", 16)
    if st.button("Calcular precio final"):
        st.write("Precio final:", calcular_precio_final(precio, descuento, impuesto))

elif exercise == "Suma de una lista":
    numeros = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Sumar lista"):
        lista_numeros = list(map(float, numeros.split(',')))
        st.write("Suma total:", sumar_lista(lista_numeros))

elif exercise == "Funciones con valores predeterminados":
    nombre = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad [Opcional]", 1)
    precio = st.number_input("Precio por unidad [Opcional]", 10)
    if st.button("Calcular precio total"):
        st.write("Precio total:", producto(nombre, cantidad, precio))

elif exercise == "Números pares e impares":
    numeros = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Separar pares e impares"):
        lista_numeros = list(map(int, numeros.split(',')))
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write("Números pares:", pares)
        st.write("Números impares:", impares)

elif exercise == "Multiplicación con *args":
    numeros = st.text_input("Ingresa números separados por comas:")
    if st.button("Multiplicar"):
        lista_numeros = list(map(float, numeros.split(',')))
        st.write("Resultado de la multiplicación:", multiplicar_todos(*lista_numeros))

elif exercise == "Información personal con **kwargs":
    nombre = st.text_input("Ingresa tu nombre:")
    edad = st.number_input("Ingresa tu edad:")
    direccion = st.text_input("Ingresa tu dirección:")
    if st.button("Mostrar información"):
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
        st.write("Información personal:\n", info)

elif exercise == "Calculadora flexible":
    num1 = st.number_input("Ingresa el primer número:", 0.0)
    num2 = st.number_input("Ingresa el segundo número:", 0.0)
    operacion = st.selectbox("Selecciona una operación:", ["suma", "resta", "multiplicación", "división"])
    if st.button("Calcular"):
        st.write("Resultado:", calculadora_flexible(num1, num2, operacion))
