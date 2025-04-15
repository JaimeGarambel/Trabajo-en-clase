import numpy as np

# Ejercicio 1
a = np.array([2, 3])
b = np.array([4, -1])
k = 2
 
print(f'1. ({a} + {b}) * {k} = {(a+b)*k}\n')
# Ejercicio 2
v1 = np.array([5, -2])
v2 = np.array([1, 3])
m = -1
resultado2 = v1 - m * v2
print(f'2. ({v1} - ({m})) * {v2} = {resultado2}\n')
 
# Ejercicio 3
x = np.array([2, 5])
y = np.array([7, 1])
z = np.array([1, 0])
 
suma_x_y = x + y
producto_escalar = np.dot(suma_x_y, z)
print(f'3. {a} + {b} = {suma_x_y} / Producto escalar entre {suma_x_y} y {z} es {producto_escalar}\n')
 
# Ejercicio 4
a = np.array([1, 2])
b = np.array([2, 1])
 
producto_escalar_a_b = np.dot(a, b)
c = a + b
resultado3 = np.dot(c, a)
 
print(f'4. Producto escalar entre {a} y {b} es {producto_escalar} / Producto escalar entre {producto_escalar_a_b} y {c} es {resultado3}\n')

# Ejercicio 5
w = np.array([4, 2])
resultado_5_1 = 3 * w
resultado_5_2 = w + np.array([-1, -4])
 
print("Ejercicio 5:")
print("1) w * 3 =", resultado_5_1)
print("2) w + [-1, -4] =", resultado_5_2)
 
# Ejercicio 6
v1 = np.array([3, 4])
v2 = np.array([-1, 5])
escalar = 2
resultado_6 = escalar * (v1 - v2)
 
print("\nEjercicio 6:")
print("Resultado =", resultado_6)
 
# Ejercicio 7
u = np.array([6, 1])
v = np.array([2, 3])
resultado_7 = (u + v) - 2 * v
 
print("\nEjercicio 7:")
print("Resultado =", resultado_7)

#Ejercicio 8
vec1 = np.random.randint(-10,11, size=2)
vec2 = np.random.randint(-10,11, size=2)
suma= vec1+vec2
resta = vec1-vec2
producto_escalar= np.dot(vec1,vec2)
print (f"los vectores son {vec1} y {vec2}")
print (f"la suma es {suma}", f"la resta es {resta}", f"el producto escalar es {producto_escalar}")
if producto_escalar==0:
    print("los vectores son ortogonales")
else:
    print("los vectores no son ortogonales")

#Ejercicio 9
a = np.array([3, 2])
b = np.array([6, 4])
escalar = b[0] / a[0] if a[0] != 0 else None
es_multiplo = np.allclose(b, escalar * a) if escalar is not None else False
print("Ejercicio 9: ¿b es múltiplo escalar de a?", es_multiplo)
if es_multiplo:
    print("Escalar:", escalar)

#Ejercicio 10
v= np.array([1,2])
u = np.array([2,-1])
producto_escalar1 = np.dot(v,u)
print("Ejercicio 10: Producto escalar de los vectores v y u:", producto_escalar1)   
print ("Funciona porque v y u son ortogonales")