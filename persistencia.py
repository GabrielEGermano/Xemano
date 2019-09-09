from peewee import *

arq = 'web-com-peewee-pessoas.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Materia(BaseModel):
    nome = CharField()
    nota = FloatField()

if __name__ == "__main__":


    
    db.connect()
    db.create_tables([Materia])
    prog = Materia.create(nome="Programaçao", nota= 9.5)
    print(prog.nome, ",", prog.nota)