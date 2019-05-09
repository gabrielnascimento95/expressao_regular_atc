# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:04:29 2019

@author: est.cassiohrr
"""
import os
import time
import pickle

from include.Pilha import Pilha
from include.Linguagem import Linguagem
    


#Funcao utilizada para controlar a pilha, recebemos como parametro
#a tag.
def define_linguagem(tag):
    p= Pilha()
    content = tag.split(': ')
   
    i=0
    #estrutura de repetição usada para percorrer a tag.
    while (i < len(content[1])):
        
        #ninho de if para controlar os caracteres de escape
        if(content[1][i]==chr(92)):
            if(content[1][i+1]=='n'):
                p.empilha("\n")
                i=i+1
            elif(content[1][i+1]==chr(92)):
                p.empilha(chr(92))
                i=i+1
            elif(content[1][i+1]=='*'):
                p.empilha("*")
                i=i+1
            elif(content[1][i+1]=='.'):
                p.empilha(".")
                i=i+1
            elif(content[1][i+1]=='+'):
                p.empilha("+")
                i=i+1
            elif(content[1][i+1]=='1'):
                p.empilha("1")    
                i=i+1
            else:
                return False
        #if para controlar o operador OR    
        elif(content[1][i]=='+'):
            if(p.tamanho()>1):
                
                a = p.desempilha()
                b = p.desempilha()
                p.empilha(a + "+" + b)
            else:
                return False
        #if para controlar o operador AND    
        elif(content[1][i]=='.'):
             if(p.tamanho()>1):
                
                a = p.desempilha()
                b = p.desempilha()
                p.empilha(a + "." + b)
             else:
                 return False
        #if para controlar operador fecho de klein     
        elif(content[1][i]=='*'):
            if(p.tamanho()>= 1):
                
                a = p.desempilha()
                p.empilha(a + "*")
            else:
                 return False
            
        else:
            p.empilha(content[1][i])
        i=i+1
    #verifica se a pilha ta vazia ou não
    if(p.tamanho()!=1):
        return False
    else:
        return True


#funcao que controla se a linguagem é regular, se a tag é repetida e a insersção no buffer
def sintaxe(linguagem,tag):
    
      l = linguagem
      regular= define_linguagem(tag)
      
      #VERIFICA SE A TAG É REGULAR E SE ELA JA EXISTE NA LISTA DE TAGLS
      if(regular and tag.split(": ")[0] not in l.tags):
          print("[INFO] Linguagem  regular!")
          l.save(tag)
          l.add_tag(tag.split(": ")[0])
          print("[INFO] Salvando em nosso Buffer...")
          time.sleep(3)
          main(linguagem)
      elif(regular==False):
          print("[WARNING] Tag inválida! \nPreparando o ambiente para uma nova entrada de dados")
          time.sleep(3)
          main(linguagem)
      else:
          print("[WARNING] Tag repetida! \nPreparando o ambiente para uma nova entrada de dados")
          time.sleep(3)
          main(linguagem)

#inicio da aplicação, criação dos parametros, recebe como parametro a persistencia na instancia da linguagem      
def main(linguagem):
      menu = input(">")
    
      #CHAMADA DA FUNCAO QUE CONTROLA A PILHA PARA UMA NOVA TAG  
      if(len(menu.split(': ')) !=1):
          sintaxe(linguagem,menu)
          
      #FUNCAO QUE CARREGA UMA LISTA DE UM ARQUIVO EXTERNO    
      elif(menu==':l'):
          file=input("[INFO] Digite o nome do arquivo: ")
          input("\n[INFO] Aperte qualquer tecla para continuar...")
          decisao=input("\n[WARNING] Deseja realmente carregar o arquivo? S ou N")
          vetor_aux=[]
          if(decisao in ['S','s']):

              with open(file, 'r') as filehandle:  
                  for line in filehandle:
                    currentPlace = line[:-1]
            
                    vetor_aux.append(currentPlace)
              print("[INFO] Arquivo lido com sucesso..")
              print("[INFO] Verificando erros..")
              time.sleep(3)
              
              for i in range(len(vetor_aux)):
                      a = define_linguagem(vetor_aux[i])
                      if(a==False):
                          text_files = open(file + "Log", "a+")
                          text_files.write("[WARNING] Linha " +str(i+1) + " : " + str(vetor_aux[i]) +"\t-> Nao eh regular\n")
                          print(str(vetor_aux[i]) +"\t->[WARNING] Nao eh regular")
 
                      else:
                          
                          if(vetor_aux[i].split(': ')[0] not in linguagem.tags):
                              print("[INFO] Linguagem Regular")
                              linguagem.save(vetor_aux[i])
                              linguagem.add_tag(vetor_aux[i].split(': ')[0])
                          else:
                              print(str(vetor_aux[i]) +"\t->[WARNING] Tag repetida")
                              text_files = open(file + "Log", "a+")
                              text_files.write("[WARNING] Linha " +str(i+1) + " : " + str(vetor_aux[i]) +"\t->[WARNING] Tag repetida\n")
                        
                          
              input("\n[INFO] Aperte qualquer tecla para continuar...")

              main(linguagem)    

          else:
              main(linguagem)    

    #FMENU QUE IMPRIME O VETOR DO BUFFER
      elif(menu==':i'):
          print(linguagem.imprime())
          input("[INFO] Aperte qualquer letra para continuar...")
          main(linguagem)
     
     #MENU QUE SALVA EM UM ARQUIVO EXTERNO   
      elif(menu in [':S',':s']):
          file=input("[INFO] Digite o nome do arquivo: ")

          input("\n[INFO] Aperte qualquer tecla para continuar...")

          decisao=input("\n[WARNING] Deseja realmente salvar no arquivo? S ou N")
          if(decisao in ['S','s']):
              text_file = open(file, "w+")
              for i in range (linguagem.tamanho()):
                  text_file.write(str(linguagem.dados[i]) +"\n")
              print("[INFO] Arquivo salvo com sucesso..")
              input("\n[INFO] Aperte qualquer letra para continuar...")

              main(linguagem)    

          else:
              main(linguagem)    
          text_file.close()    
      
      #MENU QUE FECHA A APLICAÇÃO  
      elif(menu in [':q',':Q']):
          ipt = input("[WARNING] O programa sera finalizado, deseja realmente sair?(S) or (N) ")
          if(ipt in ('S','s')):
              exit()
          else:
              main(linguagem)  
      
      else:
          print("[WARNING] Tag criada inválida, digite outra tag.")
          main(linguagem)

  
if __name__== "__main__":
  l = Linguagem()
  main(l)
