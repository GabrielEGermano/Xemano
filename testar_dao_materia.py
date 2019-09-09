from dao_estatico_materia import *

daom = Dao_materia()

print("\n==>teste listagem de materia")
for i in range(1,11):
    print(i,":",daom.retornar_materia(i))

print("\n==>teste de inclusão de dados")
daom.incluir_materia(Materia("Quimica","6"))

print("\n==>teste de listagem de materia específica")
buscado = daom.localizar_materia_por_nome("Quimica")
print(buscado)
