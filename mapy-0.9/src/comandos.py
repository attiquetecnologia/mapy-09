#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from classes import Endereco, Funcionario, Cliente, Usuario
import conexao
from chamadoBO import ChamadoBO
from pydoc import cli
from clienteBO import ClienteBO

class Comandos:
	### Função AJUDA
	def __init__(self):
		pass
	
	def help(self):
		print '''
new ......................... Nova ação a ser executada
show ........................ Visualiza informações no banco
clear ....................... Limpa a tela
exit ........................ Sai do programa
help ........................ Mostra ajuda
		'''
		
	### Funçao sobre
	def Sobre(self):
		var=open("sobre.txt","r")
		sobre=var.read()
		print str(sobre)
		var.close()
	
	### função cadastro
	def Cadastro(self):
		descricao=str(raw_input('descicao: '))
		valor=float(raw_input('valor: '))
		obs=str(raw_input('observacoes: '))
		selct = ("SELECT * FROM computer")
		insert = ("INSERT INTO computer(descricao,valor,obs) VALUES('%s','%f','%s')" %(descricao,valor,obs))
	
	def show_chamado(self):
		_c = ChamadoBO()
		_c.select('s')
	
	def new_chamado(self):
		_c = Chamado()
		print 'Novo chamado'
		
		while 1:
			try:
				_c.data_chamado				= int(raw_input('Data do chamado: '))
				break
			except: print 'Use somente numeros por exemplo: 11223333'
			
	## Este metodo é usado para pegar o codigo do cliente e levar para uma função que
	# insere os dados no banco
		while 1:
			try:
				_c.cliente.codigo			= int(raw_input('Codigo do Cliente: '))
				break
			except: print 'Use somente numeros inteiros'
			
		_c.cliente.codigo			= str(raw_input('Codigo do Cliente: '))
		
		#_c.cliente.nome				= str(raw_input('Cliente: '))
		#_c.cliente.telefone			= str(raw_input('Telefone: '))
		#_c.cliente.celular      	= str(raw_input('Celular: '))
		#_c.cliente.email           	= str(raw_input('E-mail: '))
		#_c.cliente.endereco        	= str(raw_input('Endereço: '))
		#_c.cliente.bairro          	= str(raw_input('Bairro: '))
		
		# Fazendo verificação de numeros se esta pago ou não - Tratamento de erros
		while 1:
			try:
				_c.pago						= int(raw_input('Pago: '))
				if _c.pago < 2 and _c.pago >= 0:
					break
				else:print 'Use (1-para pago e 0-para não pago)'
			except: print 'Use somente numeros(1-para pago e 0-para não pago'
		
		# Fazendo verificação de numeros do status - Tratamento de erros
		while 1:
			try:
				_c.status					= int(raw_input('Status: '))
				if _c.status < 2 and _c.status >= 0:
					break
				else:print 'Use (1-para aberto e 0-para fechado)'
			except: print 'Use somente numeros(1-chamado aberto e 0-chamaod fechado)'
		
		# Fazendo verificação de numeros do valor - Tratamento de erros
		while 1:
			try:
				_c.valor                   	= float(raw_input('Valor R$: '))
				break
			except: print 'Use somente numeros e pontos(.)'
			
		while 1:
			try:
				_c.data_pagto          		= int(raw_input('Data de pagamento: '))
				break
			except: print 'Use somente numeros'
		_c.descricao               	= str(raw_input('Descricao: '))
		
		_chBO = ChamadoBO()
		_chBO.inserir(_c)
		

	def new_cliente(self):
		_c = Cliente()
		_cBO = ClienteBO()
		_e	= Endereco()
		print 'Novo cliente'
		print
		
		_c.nome				= str(raw_input('Cliente: '))
		_c.telefone			= str(raw_input('Telefone: '))
		_c.celular      	= str(raw_input('Celular: '))
		_c.email           	= str(raw_input('E-mail: '))
		_c.site				= str(raw_input('Site: '))
		
		
		# Fazendo verificação de numeros do status - Tratamento de erros
		while 1:
			try:
				_c.status					= int(raw_input('Status: '))
				if _c.status < 2 and _c.status >= 0:
					break
				else:print 'Use (0-para intativo, 1-para ativo, 2-para passivo)'
			except: print 'Use somente numeros inteiros'
		
		_c.observacoes               	= str(raw_input('Observacoes: '))
		
		
		
		_e.endereco				= str(raw_input('Endereco: '))
		_e.bairro				= str(raw_input('Bairro: '))
		_e.cep					= str(raw_input('Cep: '))
		_e.estado				= str(raw_input('UF: '))
	
		
		_cBO.inserir(_c,_e)
	
	def show_clientes(self):
		_c = Cliente()
		_cBO = ClienteBO()
		print 'Pesquisar por: Codigo(c); Nome(n); Status(1,2,3); Geral(a)'
		resp = str(raw_input(': '))
		if resp is 'c':
			while 1:
				try:
					_c.codigo = int(raw_input('Codigo: '))
					break
				except: print 'Use somente numeros inteiros'
			
			cc = _cBO.cod_select(_c.codigo)
			print cc.codigo,cc.nome
		elif resp is 'a': 
			_cBO.select()							
			
		elif resp is 'n':
			nome = str(raw_input('nome: ')) 
			_cBO.name_select(nome)
			
		elif resp is 's':
			while 1:
				try:
					_c.status = int(raw_input('status: '))
					break
				except: print 'Use somente numeros inteiros' 
			_cBO.status_select(_c.status)	
		else: print 'problemas'