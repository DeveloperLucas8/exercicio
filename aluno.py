#coding: utf-8
class Aluno:
    nome = ""
    ra = 0
    curso = ""
    
    def __init__(self, nome="", ra=0, curso=""):
        self.nome = nome
        self.ra = ra
        self.ra = curso
    
    def __del__(self):
        print("Finalizando")
    
    def mostraAluno(self):
        print("Nome: %s" % self.nome)
        print("R.A.: %d" % self.ra)
        print("Curso: %s" % self.curso)
        
        
        
