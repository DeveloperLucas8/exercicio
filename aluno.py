#coding: utf-8
class Aluno:
    nome = ""
    ra = 0
    
    def __init__(self, nome="", ra=0):
        self.nome = nome
        self.ra = ra
    
    def __del__(self):
        print("Finalizando")
    
    def mostraAluno(self):
        print("Nome: %s" % self.nome)
        print("R.A.: %d" % self.ra)
        
        
        
