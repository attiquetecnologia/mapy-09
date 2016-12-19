#!/usr/bin/env python
#-*- encoding: utf8 -*-

# import messages # considere importar se o pygtk estiver instalado, em ambientes windows isto será trabalhoso
import string

from conexao import Conexao

from classes import Cliente, Endereco

class ClienteBO:
    def __init__(self):
        self.conexao = Conexao()

    ### inserindo dados no banco
    def inserir(self,p = Cliente(),e = Endereco()):
        insert_pessoa = "insert into pessoa(nome,email,site,telefone,celular,\
                                    cpf,rg,aniversario,data_cadastro,observacoes)\
                                values('" + p.nome + "',\
                                '" + p.email + "',\
                                '" + p.site + "',\
                                '" + p.telefone + "',\
                                '" + p.celular + "',\
                                '" + p.cpf + "',\
                                '" + p.rg + "',\
                                '" + str(p.aniversario) + "',\
                                '" + str(p.data_cadastro) + "',\
                                '" + p.observacoes + "'\
                                )"
        
        
        ### BEGIN INSERTS ON PESSOA
        try:
            self.conexao.cursor.execute(insert_pessoa)
            self.conexao.conexao.commit()
        
        
            self.conexao.cursor.execute("select * from pessoa")
            for row in self.conexao.cursor:
                p.codigo = row[0]
                
        ### BEGIN INSERTS ON CLIENTE
        
            self.conexao.cursor.execute("insert into cliente(cli_codigo,status) values(\
                                '" + str(p.codigo) + "',\
                                '" + str(p.status) + "'\
                                )")
            self.conexao.conexao.commit()
            
        ### BEGIN INSERTS ON ENDERECO
            self.conexao.cursor.execute("insert into endereco(end_codigo,endereco,bairro,cep,cidade,estado) values(\
                                '" + str(p.codigo) + "',\
                                '" + e.endereco + "',\
                                '" + e.bairro + "',\
                                '" + e.cep + "',\
                                '" + e.cidade + "',\
                                '" + e.estado + "'\
                                )")
        
            self.conexao.conexao.commit()
            print("Gravado com sucesso!")
        except:
            print("Erro na insersão dos dados!")
        
    def select(self):
        print 'Codigo Nome'    
        self.conexao.cursor.execute("select pes_codigo,nome from pessoa")
        for row in self.conexao.cursor:
            print '%4d, %s' % (row[0],row[1])
                   
#    
    def cod_select(self,codigo):
        c = Cliente()    
        self.conexao.cursor.execute("select * from pessoa where pes_codigo='" + str(codigo) + "'")
        for row in self.conexao.cursor:
            c.codigo        = row[0]
            c.nome          = row[1]
            c.email         = row[2]
            c.site          = row[3]
            c.telefone      = row[4]
            c.celular       = row[5]
            c.cpf           = row[6]
            c.rg            = row[7]
            c.aniversario   = row[8]
            c.data_cadastro = row[9]
        return c
    
#    
    def name_select(self,nome):
        c = Cliente()    
        print 'Codigo Nome'
        self.conexao.cursor.execute("select * from pessoa where nome='" + str(nome) + "'")
        for row in self.conexao.cursor:
            print '%4d,%s' % (row[0],row[1])
            
    #    
    def status_select(self,status):
        c = Cliente()    
        print 'Codigo Nome'
        self.conexao.cursor.execute("select pes_codigo,nome from pessoa,cliente where status='" + str(status) + "'")
        for row in self.conexao.cursor:
            print '%4d,%s' % (row[0],row[1])
            