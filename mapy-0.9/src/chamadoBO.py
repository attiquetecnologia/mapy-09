#!/usr/bin/env python
#-*- encoding: utf8 -*-

import string
from conexao import Conexao
from classes import Chamado, Cliente


class ChamadoBO:
    def __init__(self):
        self.conexao = Conexao()
        
    def inserir(self,ch=Chamado()):
        insert = ("insert into chamado2(data,cliente,telefone,celular,email,\
                 endereco,bairro,descricao,valor,status,pago,data_pagto) values(\
                 '" + str(ch.data_chamado) + "',\
                 '" + ch.cliente.nome + "',\
                 '" + ch.cliente.telefone + "',\
                 '" + ch.cliente.celular + "',\
                 '" + ch.cliente.email + "',\
                 '" + ch.endereco.endereco + "',\
                 '" + ch.endereco.bairro + "',\
                 '" + ch.descricao + "',\
                 '" + str(ch.valor) + "',\
                 '" + str(ch.status) + "',\
                 '" + str(ch.pago) + "',\
                 '" + str(ch.data_pagto) + "'\
                 )")
        try:
            self.conexao.cursor.execute(insert)
            self.conexao.conexao.commit()
            print("Inserido com sucesso!")
        except:
            print("Não inserido!")
    
    def select(self,p):
        if p == 'n':
            select = ("select * from chamado2")
            try:
                self.conexao.cursor.execute(select)
                print 'Numero - Data - Cliente'
                for linha in self.conexao.cursor:                
                    print '%d | %d | %s' % (linha[0],linha[1],linha[2])
            except: 
                raise 'void'
        else:
            select = ("select * from chamado2 where status=1")
            try:
                self.conexao.cursor.execute(select)
                print 'Numero - Data - Cliente'
                for linha in self.conexao.cursor:                
                    print '%d | %d | %s' % (linha[0],linha[1],linha[2])
            except: 
                raise 'void'
        
        
    