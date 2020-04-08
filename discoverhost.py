#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver, argparse, sys, subprocess
from urllib import urlopen
from time import sleep
from tqdm import tqdm


opciones = argparse.ArgumentParser(description="Detector de subdominios:", epilog="https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-10000.txt",usage="Ejemplo: python discoverhost.py -t google.com -l https://raw.githubusercontent.com/sergionidis/discoverhost/master/subdominios.txt")
opciones.add_argument('-t','--target',help="Dominio principal")
opciones.add_argument('-l','--list',help="Url de la lista de subdominios")
opciones = opciones.parse_args()

#Imprimimos un Hello friend por cortesía :p
hello = "Hola amigo  "
for char in hello:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

subprocess.call('clear', shell=True)



def main():
	wordlist = urlopen(opciones.list)
	if wordlist.getcode() != 200:
		print("No ha sido posible cargar la url proporcionada!!")
		sys.exit()
	else:
		print('Esto puede llevar mucho tiempo, paciencia!')



	ListaSubdominios = wordlist.read().split('\n')
	lista = []

	for sub in tqdm(ListaSubdominios):
		
		
    	
		try:
			a = ('{}.{}'.format(sub,opciones.target))
			q = dns.resolver.query(a,'A')
			lista.append(a)
			
		except KeyboardInterrupt:
			exit()
		except:
			pass
#Listamos los subdominios encontrados.		
	if len(lista) > 0:
			print('Numero de subdominios posibles: {}'.format(len(lista)))
			for e in lista:
				print("Subdominio {}: encontrado!!".format(e))
	else:
			print("No se encontraron subdominios")				

#Llamamos a la función principal
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
