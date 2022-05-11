from materias import *


class Aluno:
    def __init__(self, id: int, nome: str, fluxo: int, coeficiente: float, materias_atuais: list, materias_pagas: list, pendencias: list):
        self.id = id
        self.nome = nome  # Geralt of Rivia, James Howlett...
        self.fluxo = fluxo  # padrão (4), calouro(3), formando(2), individual (1)
        self.coeficiente = coeficiente  # 8.5
        self.materias_atuais = materias_atuais  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.materias_pagas = materias_pagas  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.pendencias = pendencias


id = 0
cadastrados = [
    Aluno(111, 'jose', 1, 6.0, [], ["COMP359", "COMP360","COMP361", "COMP362", "COMP363", "COMP365", "COMP366","COMP364", "COMP367"], [])
]


def matricula():
    print("Processo de matrícula iniciado.")

    w = 0
    while w < 10:
        if w == 4:
            print(
                "Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
            return
        q = input("É calouro? (s = sim / n = não): ").lower()
        if q == 's':
            nome = input("Insira o nome: ").strip()
            nome = nome[0].upper() + nome[1:]
            if len(nome) == 0 or nome.isspace() or not all(i.isalpha() or i.isspace() for i in nome):
                print("Entrada inválida!")
                w += 1
            else:
                global id
                id += 1
                calouro = Aluno(id, nome, 3, 10.0, ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363"], [[]], [])
                matriculados.append(calouro)
                print("matricula efetuada!!")
                return
        elif q == 'n':
            num = int(input("Insira o número da sua matrícula: "))
            for i in range(len(cadastrados)):
                if cadastrados[i].id == num:
                    aluno = cadastrados[i]
                    while True:
                        if(len(aluno.materias_atuais) == 10):
                            matriculados.append(aluno)
                            cadastrados.remove(aluno)
                            print("limite de materias atingido")
                            print("matricula efetuada!!")
                            return
                        

                        if(len(aluno.materias_atuais) <3):
                            sel = input("selecione uma materia para se matrícular: ").upper()
                        else:
                            while True:
                                sel = input("selecione uma materia para se matrícular (para encerrar digite 'e')):").upper() #DEPOIS TRATAR O CASO DO CARA ESCREVER ERRADO!!!!
                                if sel == 'E':
                                    matriculados.append(aluno)
                                    cadastrados.remove(aluno)
                                    print("matricula efetuada!!")
                                    return
                                else:
                                    break
                        if sel in aluno.materias_pagas:  # JÁ PAGOU!?
                            print("você já pagou essa matéria")
                        elif sel in grade_curricular:
                            print(grade_curricular[sel].nome)
                            if(grade_curricular[sel].pre_requisitos != []):
                                for i in range(len(grade_curricular[sel].pre_requisitos)):
                                    if not grade_curricular[sel].pre_requisitos[i] in aluno.materias_pagas:
                                        print("não cumpriu os pré-requisitos para ingressar na matéria!!")
                                        return
                            if sel in aluno.pendencias:
                                aluno.pendencias.remove(sel)
                            aluno.materias_atuais.append(sel)
                            print(len(aluno.materias_atuais))
                        else:
                            print("essa matéria não existe!!")

                else:
                    for j in range(len(matriculados)):
                        if matriculados[j].id == num:
                            print("\n\nvocê já está matriculado!")
                            if matriculados[j].fluxo == 3:
                                print("e você é calouro sim!!\n\n")
                            return
                    print("\n\no aluno não consta no sistema!\n\n")
                    return
        else:
            print("Entrada inválida!")
            w += 1


matriculados = []
counter = 0
while True:
    if counter == 4:
        print("Limite de entradas inválidas atingido. Programa encerrado.")
        exit()
    x = input("\nBem-vindo ao sistema de matrícula, ajuste e reajuste.\n(1) - Matrícula;\n(2) - Ajuste;\n(3) - Reajuste;\n(4) - Encerrar programa.\nSelecione uma opção: ")
    if x == '1':
        matricula()
        for i in range(len(matriculados)):
            print("\n# ", str(matriculados[i].id)+' - '+matriculados[i].nome+' atuais:'+str(matriculados[i].materias_atuais)+' coef:'+str(
                matriculados[i].coeficiente)+' fluxo:'+str(matriculados[i].fluxo)+' pagas'+str(matriculados[i].materias_pagas)+' pendencias'+str(matriculados[i].pendencias))
    elif x == '4':
        print("Programa encerrado.")
        exit()
    else:
        print("Entrada inválida!")
        counter += 1
