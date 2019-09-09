from materia import *

class Dao_materia:

    def retornar_materia(self, n):
        if n == 1:
            return Materia("odm", "2")
        elif n == 2:
            return Materia("Sociologia", "8,5")
        else:
            return Materia("Fisica", "9")

    def incluir_materia(self, m):
        m= Materia("Matematica", "10")

    def localizar_materia_por_nome(self, nome):
        return Materia("Filosofia","5")

