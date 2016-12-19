# -*- coding: UTF-8 -*-

### Programa de cadastro de computadore para venda ###
### Elaborado de forma semelhante a um anuncio na internet ###
### Rodrigo Attique Santana ###
### tecrodrigo.blogspot.com ###
### rodrigoatique@gmail.com ###

import tkSimpleDialog
import tkMessageBox

import os
import commands
import sqlite3
import string
import conexao
from comandos import Comandos
	
### AQUI COMEÇA O PROGRAMA PRINCIPAL
### EU TENTEI SER O MAIS SIMPLES POSSIVEL		

class Shell:
	mapy_ver = 'mapy-0.9x$'
	comando = Comandos()
	
	def __init__(self, so):
	
		if so.lower() == 'windows':
			cmd_clear = 'cls'
		else:
			cmd_clear = 'clear'
	
		os.system(cmd_clear)
		while True:
			op = str(raw_input(self.mapy_ver+' '))
			if op == 'help':
				self.comando.help()
			elif op == 'exit':
				break
			elif op == 'sobre':
				self.comando.Sobre()
			elif op == 'clear':
				os.system(cmd_clear)
		
			elif 'new' in op:
				if op == 'new chamado':
					self.comando.new_chamado()
				if op == 'new cliente':
					self.comando.new_cliente()
				else:
					print 'Use [ cadastro ; chamado ; cliente ]'
				
			elif 'edit' in op:
				print 'Use [ cadastros ; chamados ; clientes ]'
				
			elif 'update' in op:
				print 'Use [ cadastros ; chamados ; clientes ]'
				
			elif 'show' in op:
				if op == 'show chamados':
					self.comando.show_chamado()
				if op == 'show clientes':
					self.comando.show_clientes()
				else:
					print 'Use [ cadastros ; chamados ; clientes ]'
				
			else:
				print 'Nao reconhecido como comando interno'
				
				
if __name__ == '__main__':
	import platform
	# verifica a versão do sistema operacional
	app = Shell(platform.system())				