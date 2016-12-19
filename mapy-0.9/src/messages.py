#!/usr/bin/env python
#-*- encoding: utf8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade

def message_info(texto,janela=None):
    msgInfo = gtk.MessageDialog(janela,
                                    gtk.DIALOG_MODAL,
                                    gtk.MESSAGE_INFO,
                                    gtk.BUTTONS_OK,
                                    texto)
    msgInfo.set_title("Informação")
    msgInfo.run()
    msgInfo.destroy()
    
def message_err(texto,janela=None):
    msgInfo = gtk.MessageDialog(janela,
                                    gtk.DIALOG_MODAL,
                                    gtk.MESSAGE_ERROR,
                                    gtk.BUTTONS_OK,
                                    texto)
    msgInfo.set_title("Erro")
    msgInfo.run()
    msgInfo.destroy()
    
def message_quest(texto,janela=None):
    msgInfo = gtk.MessageDialog(janela,
                                    gtk.DIALOG_MODAL,
                                    gtk.MESSAGE_QUESTION,
                                    gtk.BUTTONS_YES_NO,
                                    texto)
    msgInfo.set_title("Pergunta")
    resposta = msgInfo.run()
    msgInfo.destroy()
    if resposta == gtk.RESPONSE_YES:
        return True
    else:
        return False
    
def message_war(texto,janela=None):
    msgInfo = gtk.MessageDialog(janela,
                                    gtk.DIALOG_MODAL,
                                    gtk.MESSAGE_WARNING,
                                    gtk.BUTTONS_OK,
                                    texto)
    #msgInfo.set_title("")
    msgInfo.run()
    msgInfo.destroy()
    
def message_oth(texto,janela=None):
    msgInfo = gtk.MessageDialog(janela,
                                    gtk.DIALOG_MODAL,
                                    gtk.MESSAGE_OTHER,
                                    gtk.BUTTONS_OK,
                                    texto)
    #msgInfo.set_title("Erro")
    msgInfo.run()
    msgInfo.destroy()