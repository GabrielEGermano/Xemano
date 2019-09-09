class Materia:

    def __init__(self, nome=None, nota=None):
        if nome:
            self.nome = nome
        if nota:
            self.nota = nota

    def __str__(self):
        return "Nome: "+self.nome + \
               ", Notas: " + self.nota

