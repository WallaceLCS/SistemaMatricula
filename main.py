from materias import *

class Aluno:
    def __init__(self, id: int, nome: str, fluxo: int, coeficiente: float, materias_atuais: list, materias_pagas: list, pendencias: list):
        self.id = id
        self.nome = nome  # Geralt of Rivia, James Howlett...
        self.fluxo = fluxo  # padrão (4), calouro (3), formando (2), individual (1)
        self.coeficiente = coeficiente  # 8.5
        self.materias_atuais = materias_atuais  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.materias_pagas = materias_pagas  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.pendencias = pendencias # ["COMP359","COMP360","COMP361","COMP362","COMP363"]


id = 0
cadastrados = [
    Aluno(111, 'José Henrique da Silva', 1, 6.0, [], ["COMP359", "COMP360","COMP361", "COMP362", "COMP363", "COMP365", "COMP366","COMP364", "COMP367"], []),
    #Aluno(222, 'Maria Carla de Andrade', 3, 7.5, [], ["COMP359", "COMP360","COMP361", "COMP362", "COMP363", "COMP365", "COMP366","COMP364", "COMP367"], []),
    Aluno(666, 'Lucifer Morningstar', 2, 9.0, [], mat_lista, [])
]

def matricula():
    print("Processo de matrícula iniciado.")

    w = 0
    while w < 10:
        if w == 4: print("Limite de entradas inválidas atingido. Processo de matrícula encerrado."); return

        q = input("É calouro? (s = sim / n = não): ").lower()
        if q == 's':
            nome = input("Insira o nome: ").strip()
            nome = nome[0].upper() + nome[1:]

            if len(nome) == 0 or nome.isspace() or not all(i.isalpha() or i.isspace() for i in nome): print("Entrada inválida."); w += 1
            else:
                global id
                id += 1
                calouro = Aluno(id, nome, 3, 10.0, ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363"], [[]], [])

                for i in range(len(calouro.materias_atuais)):
                    if calouro.materias_atuais[i] in grade_curricular:
                        if (grade_curricular[calouro.materias_atuais[i]].ocupado == grade_curricular[calouro.materias_atuais[i]].limite):
                             print("A matéria inserida está cheia.")
                             return
                        else:
                            grade_curricular[calouro.materias_atuais[i]].ocupado+=1             
                matriculados.append(calouro)
                print("Matrícula efetuada.")
                return
        elif q == 'n':
            num = int(input("Insira o número da sua matrícula: "))

            check = 0
            for i in range(len(cadastrados)):
                if cadastrados[i].id == num:
                    aluno = cadastrados[i]
                    check = 1
                    break
            if check == 0:
                if matriculados != []:
                    for j in range(len(matriculados)):
                        if matriculados[j].id == num:
                            print("\n\nVocê já está matriculado!")
                            if matriculados[j].fluxo == 3:
                                print("Você é calouro e foi leviano para com o sistema.\n\n")
                            return
                print("\n\nO aluno não consta no sistema.\n\n")
            else:
                for j in cadastrados:
                    if (aluno.fluxo < j.fluxo):
                        print("\nAguarde os alunos de prioridade maior fazerem a matrícula.")
                        return
            
                if aluno.fluxo == 2:
                    print("Você é formando.")
                    aluno.materias_atuais = ["TCC1", "TCC2", "TCC3"]
                    matriculados.append(aluno)
                    cadastrados.remove(aluno)
                    print("Matrícula efetuada.")
                    return

                x = 0
                y = 0
                while True:
                    if x == 4 or y == 4: print("Limite de entradas inválidas atingido. Processo de matrícula encerrado."); break
                    if len(aluno.materias_atuais) == 10:
                        matriculados.append(aluno)
                        cadastrados.remove(aluno)
                        print("Limite de materias atingido.")
                        print("Matrícula efetuada.")
                        return

                    if len(aluno.materias_atuais) < 3:
                        sel = input("Selecione uma matéria para se matricular: ").upper()
                    else:
                        while True:
                            sel = input("Selecione uma matéria para se matrícular (para encerrar, insira 'e'): ").upper()
                            if sel == 'E':
                                matriculados.append(aluno)
                                cadastrados.remove(aluno)
                                print("Matrícula efetuada.")
                                return
                            else:
                                break
                    
                    if sel not in mat_lista: print("A matéria informada não se encontra no sistema."); y += 1
                    else:
                        if sel in aluno.materias_pagas: #Checa se o aluno já pagou a matéria.
                            print("Você já pagou essa matéria.")
                        elif sel in grade_curricular:
                            for i in range(len(aluno.materias_atuais)):
                                for j in range(len(grade_curricular[aluno.materias_atuais[i]].horario)):
                                    for k in range(len( grade_curricular[sel].horario)):
                                        if grade_curricular[aluno.materias_atuais[i]].horario[j] == grade_curricular[sel].horario[k]:
                                            print("Horários conflitantes.")
                                            return 
                            print(grade_curricular[sel].nome)
                            if grade_curricular[sel].ocupado == grade_curricular[sel].limite:
                                print("Matéria cheia.")
                                return
                            if grade_curricular[sel].pre_requisitos != []:
                                for i in range(len(grade_curricular[sel].pre_requisitos)):
                                    if not grade_curricular[sel].pre_requisitos[i] in aluno.materias_pagas:
                                        print("Não cumpre os pré-requisitos para ingressar na matéria.")
                                        return
                            if sel in aluno.pendencias:
                                aluno.pendencias.remove(sel)
                            aluno.materias_atuais.append(sel)
                            grade_curricular[sel].ocupado+=1
                            print(len(aluno.materias_atuais))
                        else:
                            print("A matéria informada não se encontra no sistema.")
                            x += 1
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
            print("\n#", str(matriculados[i].id)+' nome: '+matriculados[i].nome+' m_atuais:'+str(matriculados[i].materias_atuais)+' coef:'+str(
                matriculados[i].coeficiente)+' fluxo:'+str(matriculados[i].fluxo)+' m_pagas'+str(matriculados[i].materias_pagas)+' pendencias'+str(matriculados[i].pendencias))
    elif x == '4':
        print("Programa encerrado.")
        exit()
    else:
        print("Entrada inválida!")
        counter += 1
