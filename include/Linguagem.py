# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:20:27 2019

@author: est.cassiohrr
"""



class Linguagem(object):
    def __init__(self):
        self.dados = []
        self.tags=[]

    def save(self, elemento):
        self.dados.append(elemento)
    
    def add_tag(self, elemento):
        self.tags.append(elemento)
    
    def tamanho(self):
        return len(self.dados)
    
    def imprime(self):
        return self.dados
    