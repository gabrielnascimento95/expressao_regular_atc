# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:04:29 2019

@author: est.cassiohrr
"""
import os
import time
import pickle

from Pilha import Pilha
from Linguagem import Linguagem
    



def define_linguagem(tag):
    p= Pilha()
    content = tag.split(':')
    
    for c in content[1]:
        
        if(c=='+'):
            if(p.tamanho()>1):
                
                a = p.desempilha()
                b = p.desempilha()
                p.empilha(a + "+" + b)
            else:
                return False
        elif(c==' '):
            p.empilha(c)
            p.desempilha()
        elif(c=='.'):
             if(p.tamanho()>1):
                
                a = p.desempilha()
                b = p.desempilha()
                p.empilha(a + "." + b)
             else:
                 return False
        elif(c=='*'):
            a = p.desempilha()
            p.empilha(a + "*")
            
        else:
            p.empilha(c)
    if(p.tamanho()!=1):
        return False
    else:
        return True
    
def sintaxe(linguagem,tag):
    
      l = linguagem
      if(tag==':..'):
          main(l)
      elif(tag==':q'):
           exit()
      elif(tag[0] == ':'):
          print("[ERROR] Valor de Tag inválido, favor inserir uma nova tag")
          main(linguagem)
      elif(tag.find(":") == -1):
          print("[ERROR] Não apresenta dois pontos, sintaxe inválida para tag, favor digitar novamente")
          main(linguagem)
      else:
          regular= define_linguagem(tag)
          if(regular):
              print("[INFO] Linguagem  regular!")
              l.save(tag)
              print("[INFO] Salvando em nosso Buffer...")
              time.sleep(3)
          #    os.system('cls' if os.name == 'nt' else 'clear')
              main(linguagem)
          else:
              print("[WARNING] Linguagem não regular! \nPreparando o ambiente para uma nova entrada de dados")
              time.sleep(3)
          #    os.system('cls' if os.name == 'nt' else 'clear')
              main(linguagem)
               
      
def main(linguagem):
      os.system('cls' if os.name == 'nt' else 'clear')
      menu = input("")
      if(len(menu.split(':')) !=1):
          sintaxe(linguagem,menu)

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
                          text_files.close()

                      else:
                          linguagem.save(vetor_aux[i])
                          print("[INFO] Linguagem Regular")
                          
                          
              input("\n[INFO] Aperte qualquer tecla para continuar...")

              main(linguagem)    

          else:
              main(linguagem)    

      elif(menu==':i'):
          print(linguagem.imprime())
          input("[INFO] Aperte qualquer letra para continuar...")
          main(linguagem)
      elif(menu==':s'):
          file=input("[INFO] Digite o nome do arquivo: ")

          input("\n[INFO] Aperte qualquer tecla para continuar...")

          decisao=input("\n[WARNING] Deseja realmente salvar no arquivo? S ou N")
          if(decisao in ['S','s']):
              text_file = open(file, "w")
              for i in range (linguagem.tamanho()):
                  text_file.write(str(linguagem.dados[i]) +"\n")
              print("[INFO] Arquivo salvo com sucesso..")
              input("\n[INFO] Aperte qualquer letra para continuar...")

              main(linguagem)    

          else:
              main(linguagem)    

      
      elif(menu==':q'):
          ipt = input("[WARNING] O programa sera finalizado, deseja realmente sair?(S) or (N) ")
          if(ipt in ('S','s')):
              exit()
          else:
              main(linguagem)  
      else:
          print("[WARNING] O programa será abortado, opção inválida")
          exit()

  
if __name__== "__main__":
  l = Linguagem()
  main(l)
