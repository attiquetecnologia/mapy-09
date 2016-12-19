
class Pessoa(object):
    def __init__(self):
        self.codigo         = 0
        self.nome           = ''
        self.email          = ''
        self.site           = ''
        self.telefone       = ''
        self.celular        = ''
        self.cpf            = ''
        self.rg             = ''
        self.aniversario    = 0
        self.data_cadastro  = 0
        self.observacoes    = ''
        
class Cliente(Pessoa):
    def __init__(self):
        super(Cliente,self).__init__()
        self.n_chamado      = 0
        self.status         = 0

class Funcionario(Pessoa):
    def __init__(self):
        super(Funcionario,self).__init__()
        self.faltas         = 0
        self.salario        = 0.0
        self.status         = 0
        
class Usuario(Funcionario):
    def __init__(self):
        super(Usuario,self).__init__()
        self.senha          = ''
        
class Endereco(object):
    def __init__(self):
        self.endereco       = ''
        self.bairro         = ''
        self.cep            = ''
        self.cidade         = ''
        self.estado         = ''
        self.funcionario    = Funcionario
        self.cliente        = Cliente
        
class Chamado(object):
    def __init__(self):
        self.numero         = 0
        self.data_chamado   = 0
        self.valor          = 0.0
        self.descricao      = ''
        self.data_pagto     = 0
        self.status         = 0
        self.pago           = 0
        self.cliente        = Cliente()
        self.endereco       = Endereco()
        
class Hardware(object):
    def __init__(self):
        self.processador    = ''
        self.memoria        = ''
        self.hd             = ''
        self.restante       = ''
        self.cliente        = Cliente