# Reto #41
# LA LEY DE OHM
# Fecha publicación enunciado: 10/10/22
# Fecha publicación resolución: 17/10/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
# - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
# - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
# 
# Statement: Create a function that calculates the value of the missing parameter corresponding to Ohm's law.
# - We will send to the function 2 of the 3 parameters (V, R, I), and it will return the value of the third one (rounded to 2 decimal places).
# - If the parameters are incorrect or insufficient, the function will return the string "Invalid values".
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def ohm(v=None, i=None, r=None):
	try:
		if v==None and i!=None and r!=None: return f"V = {(i * r):.2f} V"
		elif v!=None and i==None and r!=None: return f"V = {(v / r):.2f} A"
		elif v!=None and i!=None and r==None: return f"V = {(v / i):.2f} Ohm"
	except ZeroDivisionError:
		return "ERROR: number divided by 0!"
	return "ERROR: Invalid values!"

print(ohm()) # ERROR: Invalid values!
print(ohm(v = 5.0)) # ERROR: Invalid values!
print(ohm(v = 5.0, r = 4.0)) # I = 1.25 A
print(ohm(v = 5.0, i = 4.0)) # R = 1.25 Ohm
print(ohm(r = 5.0, i = 4.0)) # V = 20.05 V
print(ohm(v = 5.125, r = 4.0)) # I = 1.28 A
print(ohm(v = 5.0, i = 4.125)) # R = 1.21 Ohm
print(ohm(r = 5.0, i = 4.125)) # V = 20.63 V
print(ohm(v = 5.0, r = 0.0)) # I = 500.00 A
print(ohm(v = 5.0, i = 0.0)) # R = 500.00 Ohm
print(ohm(r = 5.0, i = 0.0)) # V = 0.05 V
print(ohm(v = 5.0, r = 4.0, i = 3.0)) # ERROR: Invalid values!