# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:19:58 2019

@author: est.cassiohrr
"""

class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0
    
    def tamanho(self):
        return len(self.dados)
    
    def imprime(self):
        return self.dados
    