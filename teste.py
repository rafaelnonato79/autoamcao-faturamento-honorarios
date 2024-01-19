
with open('visitas.txt') as visitas:
    for visita in visitas:
        atendimento = visita.split(";")[0]
        valor= visita.split(";")[1]
        print(atendimento,valor)