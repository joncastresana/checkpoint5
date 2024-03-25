# Cree un bucle For de Python.

nums = [1, 2, 3]

for num in nums:
    print(num)

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(arg1, arg2, arg3):
    total = arg1 + arg2 + arg3
    return total

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

total = lambda arg1, arg2, arg3: arg1 + arg2 + arg3
resultado = total(1, 2, 3)
print(resultado)

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print("el valor de la variable coincide con un valor de la lista")

else:
    print("el valor de la variable no coincide con un valor de la lista")
     
     
        
  






           


