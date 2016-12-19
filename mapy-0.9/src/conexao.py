#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sqlite3
import tkMessageBox
import tkSimpleDialog

class Conexao:
    caminho_banco = None
    conexao = None
    cursor = None
    
    def __init__(self):
        self.caminho_banco = "C:\Users\master\Documents\Projetos\mapy-0.9\data\banco.db"
        
        try:
            self.conexao = sqlite3.connect(self.caminho_banco)
        except:
            print ("Não foi possível criar conexão!")
        try:
            self.cursor = self.conexao.cursor()
        except:
            print ("Impossível criar cursor!")
            
        