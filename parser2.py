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
		if i == '(':
			posible = 1
		if posible == 1:
			spam = spam + i
		nuevaLinea = (nuevaLinea + i)
		if i == ')':
			if 'FREE' in spam:
				print(nuevaLinea)
				nuevaLinea = nuevaLinea.strip(spam)
				print(nuevaLinea)
				print(spam)
			if 'OUT NOW' in spam:
				nuevaLinea = nuevaLinea.strip(spam)
			posible = 0
			spam = ''
	artista = linea[pos+10:len(linea)]
	nuevaLinea = (nuevaLinea + artista)
	print('+', nuevaLinea)
	nuevoListado.insert((x), nuevaLinea)
	
# Doy oportunidad a que el usuario cancele la operación si no está conforme con los nuevos cambios
print(Fore.BLUE + '[+] ¿Quieres que se produzcan los cambios? (s/n)')
if input().lower() == 'n':
	print(Fore.RED + '[+] Los archivos mantendrán los nombres originales.')
	exit()

# Cambio de nombre a los ficheros por los nuevos nombres en nuevoListado
for x in range(0, len(nuevoListado)):
	os.system('rename "' + ruta + '\\' + listado[x] + '" "' + nuevoListado[x] + '"')
print(Fore.GREEN + '\n[+] Todos los ficheros han sido cambiados de nombre con éxito.')