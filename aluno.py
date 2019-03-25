#coding: utf-8
class Aluno:
    nome = ""
    ra = 0
    curso = ""
    
    def __init__(self, nome="", ra=0, curso=""):
        self.nome = nome
        self.ra = ra
<<<<<<< HEAD
        self.ra = curso
=======
        self.curso= curso
>>>>>>> master
    
    def __del__(self):
        print("Finalizando")
    
    def mostraAluno(self):
        print("Nome: %s" % self.nome)
        print("R.A.: %d" % self.ra)
<<<<<<< HEAD
	print("curso: %s" % self.curso)
=======
<<<<<<< HEAD
        print("Curso: %s" % self.curso)
=======
	print("Curso: %s" % self.curso)
>>>>>>> master
>>>>>>> master
        
        
        
