# parser4Vic.py
# Version actualizada del parser2Vic.py

import os, shutil
from colorama import *

def listar(ruta, listado):
	"""Exporta a un archivo los nombres de los ficheros en la ruta especificada y los guarda línea a línea en una lista."""
	allFiles = os.listdir(ruta)

	for item in allFiles:
		listado.append(item)

def cambiarNombres(listado, nuevoListado):
	"""Guarda en una nueva lista los nombres parseados"""
	for item in listado:
		nuevaLinea = ''
		posible = 0
		spam = ''
		for i in item:
			if i == '_':
				break
			if i == '(' or i == '[':
				posible = 1
			if posible == 1:
				spam = spam + i
			nuevaLinea = (nuevaLinea + i)
			if i == ')' or i == ']':
				if 'FREE' in spam.upper() or 'OUT NOW' in spam.upper():
					nuevaLinea = nuevaLinea.strip(spam)
				posible = 0
				spam = ''
	#########################################################################
		# Estas dos nuevas lineas evitan duplicados de '.mp3' en el nombre
		nuevaLinea = nuevaLinea.rstrip('.mp3')
		nuevaLinea = nuevaLinea + '.mp3'
	#########################################################################
		print('+', nuevaLinea)
		nuevoListado.append(nuevaLinea)

def continuar():
	"""Pregunta al usuario si quiere realizar los cambios o abandonar la operación"""
	print(Fore.BLUE + '[+] ¿Quieres que se produzcan los cambios? (s/n) (Por defecto sí)')
	if input().lower() == 'n':
		print(Fore.RED + '[+] Los archivos mantendrán los nombres originales.')
		exit()

init(autoreset=True)

print(Back.YELLOW + Fore.WHITE + '┌' + format('','─^78') + '┐')
print(Back.YELLOW + Fore.WHITE + '│' + format('Bienvenid@ al Parser2.0'.title(),'^78') + '│')
print(Back.YELLOW + Fore.WHITE + '└' + format('','─^78') + '┘')

print(Fore.BLUE+'\n[+] Pega aquí la ruta de los archivos que quieres parsear: ')
ruta = input()
listado = []
nuevoListado = []

listar(ruta, listado)
print(Fore.BLUE+'\n[+] Los archivos tienen actualmente los siguientes nombres:')
for item in listado:
	print('-',item)

print(Fore.BLUE+'\n[+] Los nombres de los archivos serán cambiados por los que siguen respectivamente:')
cambiarNombres(listado, nuevoListado)

continuar()
for i, item in enumerate(nuevoListado, start=1):
	# os.system('rename "' + ruta + '\\' + listado[x] + '" "' + item + '"')
	shutil.move('ruta'+'\\'+listado[x], 'ruta'+'\\'+item) # Nuevo codigo experimental
print(Fore.GREEN + '\n[+] Todos los ficheros han sido cambiados de nombre con éxito.')
