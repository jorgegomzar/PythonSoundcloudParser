import os
from colorama import *
init(autoreset=True)

print(Back.YELLOW + Fore.WHITE + '┌' + format('','─^78') + '┐')
print( Back.YELLOW + Fore.WHITE + '│' + format('Bienvenid@ al Parser2.0'.title(),'^78') + '│')
print(Back.YELLOW + Fore.WHITE + '└' + format('','─^78') + '┘')

print(Fore.BLUE+'\n[+] Pega aquí la ruta de los archivos que quieres parsear: ')
ruta = input()
listado = []
nuevoListado = []

# Exporto a un archivo los nombres de los ficheros y los guardo linea a linea en una cadena
os.system('dir /b "' + ruta + '" > archivos.txt')
archivo = open('archivos.txt', 'r')
for x in range(1, 100):
	linea = archivo.readline()
	if linea == '':
		break
	listado.insert((x-1), linea.rstrip('\n'))
archivo.close()
os.system('del archivos.txt')
numero = len(listado)
print(Fore.BLUE+'\n[+] Los archivos tienen actualmente los siguientes nombres:')
for item in listado:
	print('-',item)

# Guardo en una nueva lista los nombres parseados	
print(Fore.BLUE+'\n[+] Los nombres de los archivos serán cambiados por los que siguen respectivamente:')
for x in range(0, len(listado)):
	nuevaLinea = ''
	pos = 0
	linea = listado[x]
	for i in linea:
		if i == '_':
			break
		pos = pos + 1
		nuevaLinea = (nuevaLinea + i)
	nuevaLinea = (nuevaLinea + '.mp3')
	print('+', nuevaLinea)
	nuevoListado.insert((x), nuevaLinea)

# Cambio de nombre a los ficheros por los nuevos nombres en nuevoListado
for x in range(0, len(nuevoListado)):
	print('rename "' + ruta + '\\' + listado[x] + '" "' + nuevoListado[x] + '"')
print(Fore.GREEN + '\n[+] Todos los ficheros han sido cambiados de nombre con éxito.')

# Para proxima version eliminar FREE DOWNLOAD FREE DL Y OUT NOW