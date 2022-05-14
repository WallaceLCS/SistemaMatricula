from materias import *

class Aluno:
    def __init__(self, id: int, nome: str, fluxo: int, coeficiente: float, materias_atuais: list, materias_pagas: list, pendencias: list):
        self.id = id
        self.nome = nome  # Geralt of Rivia, James Howlett...
        self.fluxo = fluxo  # padrão (4), calouro (3), formando (2), individual (1)
        self.coeficiente = coeficiente  # 8.5
        self.materias_atuais = materias_atuais  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.materias_pagas = materias_pagas  # ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        self.pendencias = pendencias
        
class Pedido:
    def __init__(self, aluno:Aluno, insercao:str = None, remocao:str = None):
        self.aluno = aluno
        self.insercao = insercao
        self.remocao = remocao

ajuste_lista = []
matriculados = [
    Aluno(444, 'João Pedro', 1, 8.0, ["COMP372", "CC1965", "CC1962"],["COMP359", "COMP360", "COMP361", "COMP362", "COMP363","COMP364", "COMP365", "COMP366"], ["COMP367"]),
    Aluno(333, 'Ana Clara', 4, 6.0, ["COMP368","COMP369","COMP370","COMP371"],["COMP359", "COMP360", "COMP361", "COMP362", "COMP363","COMP364", "COMP365", "COMP366", "COMP367"], [])
]
id = 0
cadastrados = [
    Aluno(111, 'José Henrique da Silva', 1, 6.0, [], ["COMP359","COMP365","COMP360","COMP361", "COMP362", "COMP363", "COMP365", "COMP366", "COMP367"], ["COMP364"]),
    Aluno(222, 'Maria Carla de Andrade', 4, 7.5, [], ["COMP359", "COMP360","COMP361", "COMP362", "COMP363", "COMP365", "COMP366","COMP364", "COMP367"], []),
    Aluno(666, 'Lucifer Morningstar', 2, 9.0, [], ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP368", "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380", "COMP381", "COMP382", "COMP386", "COMP387", "COMP389", "COMP390", "COMP391", "COMP392", "COMP393", "COMP394", "COMP395", "COMP396", "COMP397", "COMP398", "COMP399", "COMP400", "COMP401"], [])
]

def encerrar_reajuste():
    #ordernar por coeficiente
    for i in range(0, len(ajuste_lista) - 1):  # The total number of passes,bubbles: i
        for j in range(0, len(ajuste_lista) - i - 1):  # The total number of iterations: j
            if ajuste_lista[j].aluno.coeficiente > ajuste_lista[j + 1].aluno.coeficiente:
                ajuste_lista[j], ajuste_lista[j + 1] = ajuste_lista[j + 1], ajuste_lista[j]  # swap elements
 
    #printar lista
    for i in range(len(ajuste_lista)):
        print(f"{ajuste_lista[i].aluno.nome}: {ajuste_lista[i].aluno.coeficiente}")
        ajuste_lista.pop(0)
        
def ajuste_reajuste(tipo:int):
    if tipo == 1:
        print("Processo de Reajuste iniciado.")
    else:
        print("Processo de ajuste iniciado.")
    check=0
    identificacao_ajuste = int(input("Insira seu ID: "))
    for i in matriculados:
        if i.id == identificacao_ajuste:
            aluno=i
            check =1
            print(f"\nBem-vindo(a) {aluno.nome}.")
            break
    if check == 0:
        print("ID INVÁLIDO")
        return 
    
    while True:
        print("Qual operação vc quer realizar no ajuste?")
        y = int(input("\n(1): Inserção de matéria."
                      "\n(2): Remoção de matéria."
                      "\n(3): Troca de matéria.\n"
                      "(4): Voltar.\n"
                      "Selecione uma opção: "))
        if y == 1:
            insercao(aluno,tipo)
        elif y == 2:
            remocao(aluno,tipo)
        elif y == 3:
            troca(aluno,tipo)
        elif y  == 4:
            aluno.ajustado='0'
            return
            #voltar para tela inicial
        else:
            print("Opção inválida")


def insercao(aluno:Aluno,tipo:int):
    confirm_requirement = True
    #checar se o cara já nao ta no maximo

    if len(aluno.materias_atuais) >= 10:
        print("Você já esta limite máximo de disciplinas cadastradas")
        return
    
    print("\nDisciplinas de Ciência:\n")
    for materia in grade_CC:
        if materia in aluno.materias_atuais:
            continue
        print("\033[1m"+materia+"\033[0m"+":",grade_CC[materia].nome, end=" || ")
    if tipo == 1:
        print("\nDisciplinas de Engenharia da Computação e Matemática:\n")
        for materia in grade_externa:
            if materia in aluno.materias_atuais:
                continue
            print("\033[1m"+materia+"\033[0m"+":",grade_externa[materia].nome, end=" || ")
    print("")
    
    while True:
        escolha = input("Digite o código da matéria: (digite 'e' para sair) ").upper()
        print("")
        if escolha == 'E':
            return
        if tipo ==1:
            if not escolha in mat_lista or not escolha in mat_lista_externa:
                print("essa matéria não existe!")
        elif not escolha in mat_lista:
            print("essa matéria não existe!")
        elif escolha in aluno.materias_atuais:
            if escolha in grade_externa:
                print(f"Você já esta cadastrado em {grade_externa[escolha].nome}")
            else:
                print(f"Você já esta cadastrado em {grade_CC[escolha].nome}")
        else:
            #Ve se tem pré-requesito
            if tipo == 1:
                if escolha in grade_externa:
                    lista_prereq = grade_externa[escolha].pre_requisitos
                    quant_prereq = len(grade_externa[escolha].pre_requisitos)
                else:
                    lista_prereq = grade_CC[escolha].pre_requisitos
                    quant_prereq = len(grade_CC[escolha].pre_requisitos)
            else:
                lista_prereq = grade_CC[escolha].pre_requisitos
                quant_prereq = len(grade_CC[escolha].pre_requisitos)

            confirm_requirement = False
            if quant_prereq > 0:
                for pagas in aluno.materias_pagas:
                    if tipo == 1:
                        if escolha in grade_externa:
                            for pre_req in grade_externa[escolha].pre_requisitos:
                                if pre_req == pagas:
                                    quant_prereq = quant_prereq - 1
                                    lista_prereq.remove(pre_req)
                                    if quant_prereq == 0:
                                        confirm_requirement = True
                                        break
                        else:
                            for pre_req in grade_CC[escolha].pre_requisitos:
                                if pre_req == pagas:
                                    quant_prereq = quant_prereq - 1
                                    lista_prereq.remove(pre_req)
                                    if quant_prereq == 0:
                                        confirm_requirement = True
                                        break
                    else:
                        for pre_req in grade_CC[escolha].pre_requisitos:
                            if pre_req == pagas:
                                quant_prereq = quant_prereq - 1
                                lista_prereq.remove(pre_req)
                                if quant_prereq == 0:
                                    confirm_requirement = True
                                    break 
                if confirm_requirement == False:
                    print(f"Você NÃO tem o pre-requesito para pagar essa matéria, você precisa pagar:")
                    print(*lista_prereq, sep=' ')
            if escolha in aluno.materias_pagas:
                print("Você já pagou essa matéria!\n")
            else:
                #Ver se tem horario
                check =0
                for mtm in aluno.materias_atuais: #pega a string materia
                    if tipo == 1:
                        if escolha in grade_externa:
                            for horarios_atuais_materias in grade_externa[mtm].horario: #pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_externa[escolha].horario: #loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check=1
                                        print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_externa[mtm].nome} é conflitante com a que voce quer aplicar ({grade_externa[escolha].nome}).")
                                    break
                                break
                            break
                        else:
                            for horarios_atuais_materias in grade_CC[mtm].horario: #pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_CC[escolha].horario: #loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check=1
                                        print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_CC[mtm].nome} é conflitante com a que voce quer aplicar ({grade_CC[escolha].nome}).")
                                    break
                                break
                            break
                    else:
                        for horarios_atuais_materias in grade_CC[mtm].horario: #pega essa string materia e acessa seus horarios
                            for horarios_materias in grade_CC[escolha].horario: #loopa os horario da materia escolhida com a materia que possui
                                if horarios_atuais_materias == horarios_materias:
                                    check=1
                                    print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_CC[mtm].nome} é conflitante com a que voce quer aplicar ({grade_CC[escolha].nome}).")
                                break
                            break
                        break
                if check == 0:
                    break

    #ARMAZENAR INSERÇÃO
    ajuste_lista.append(Pedido(aluno,escolha))
    print("Sua inserção foi registrada.")
    choice = input("Você quer realizar outra inserção?" "s/n: ")
    if choice == 's':
        insercao(aluno,tipo)

def remocao(aluno:Aluno,tipo:int):
    if len(aluno.materias_atuais) - 1 < 3:
        print("Você deve ficar matriculado em no mínimo 3 matérias")
        return
    print("Materias atuais:")
    for materia in aluno.materias_atuais:
        print("\033[1m"+materia+"\033[0m")
    print("")
    
    while True:
        escolha = input("Qual matéria você quer ser removido?, digite o código: (digite 'e' para sair) ").upper()
        if escolha == 'E':
            return
        if not escolha in aluno.materias_atuais:
            if tipo == 1:    
                if not escolha in mat_lista or escolha not in mat_lista_externa: 
                    print ("matéria inexistente")
            elif not escolha in mat_lista:
                print ("matéria inexistente")
            else:
                print(f"Você não esta matriculado na materia {escolha},e o por isso não pode ser removido dela.")
        else:
            ajuste_lista.append(Pedido(aluno,None,escolha))
            print("Sua remoção foi registrada.")
            break




def troca(aluno:Aluno,tipo:int):
    print("Materias atuais:")
    for materia in aluno.materias_atuais:
        print("\033[1m"+materia+"\033[0m")
    print("")
    while True:
        escolha_remover = input("Digite o código da matéria(remover): (digite 'e' para sair) ").upper()
        if escolha_remover == 'E':
            return
        if not escolha_remover in aluno.materias_atuais:
            if tipo == 1:    
                if not escolha_remover in mat_lista or escolha_remover not in mat_lista_externa: 
                    print ("matéria inexistente")
            elif not escolha_remover in mat_lista:
                print ("matéria inexistente")
            else:
                print(f"Você não esta matriculado na materia {escolha_remover},e o por isso não pode ser removido dela.")
        else:
            break
    
    print("\nDisciplinas de Ciência:\n")
    for materia in grade_CC:
        if materia in aluno.materias_atuais:
            continue
        print("\033[1m"+materia+"\033[0m"+":",grade_CC[materia].nome, end=" || ")
    if tipo == 1:
        print("\nDisciplinas de Engenharia da Computação e Matemática:\n")
        for materia in grade_externa:
            if materia in aluno.materias_atuais:
                continue
            print("\033[1m"+materia+"\033[0m"+":",grade_externa[materia].nome, end=" || ")
    print("")
    print("Agora informe ")
    
    while True:
        escolha_insercao = input("Digite o código da matéria(inserir): (digite 'e' para sair) ").upper()
        print("")
        if escolha_insercao == 'E':
            return
        if tipo ==1:
            if not escolha_insercao in mat_lista or not escolha_insercao in mat_lista_externa:
                print("essa matéria não existe!")
        elif not escolha_insercao in mat_lista:
            print("essa matéria não existe!")
        elif escolha_insercao in aluno.materias_atuais:
            if escolha_insercao in grade_externa:
                print(f"Você já esta cadastrado em {grade_externa[escolha_insercao].nome}")
            else:
                print(f"Você já esta cadastrado em {grade_CC[escolha_insercao].nome}")
        else:
            #Ve se tem pré-requesito
            if tipo == 1:
                if escolha_insercao in grade_externa:
                    lista_prereq = grade_externa[escolha_insercao].pre_requisitos
                    quant_prereq = len(grade_externa[escolha_insercao].pre_requisitos)
                else:
                    lista_prereq = grade_CC[escolha_insercao].pre_requisitos
                    quant_prereq = len(grade_CC[escolha_insercao].pre_requisitos)
            else:
                lista_prereq = grade_CC[escolha_insercao].pre_requisitos
                quant_prereq = len(grade_CC[escolha_insercao].pre_requisitos)

            confirm_requirement = False
            if quant_prereq > 0:
                for pagas in aluno.materias_pagas:
                    if tipo == 1:
                        if escolha_insercao in grade_externa:
                            for pre_req in grade_externa[escolha_insercao].pre_requisitos:
                                if pre_req == pagas:
                                    quant_prereq = quant_prereq - 1
                                    lista_prereq.remove(pre_req)
                                    if quant_prereq == 0:
                                        confirm_requirement = True
                                        break
                        else:
                            for pre_req in grade_CC[escolha_insercao].pre_requisitos:
                                if pre_req == pagas:
                                    quant_prereq = quant_prereq - 1
                                    lista_prereq.remove(pre_req)
                                    if quant_prereq == 0:
                                        confirm_requirement = True
                                        break
                    else:
                        for pre_req in grade_CC[escolha_insercao].pre_requisitos:
                            if pre_req == pagas:
                                quant_prereq = quant_prereq - 1
                                lista_prereq.remove(pre_req)
                                if quant_prereq == 0:
                                    confirm_requirement = True
                                    break 
                if confirm_requirement == False:
                    print(f"Você NÃO tem o pre-requesito para pagar essa matéria, você precisa pagar:")
                    print(*lista_prereq, sep=' ')
            if escolha_insercao in aluno.materias_pagas:
                print("Você já pagou essa matéria!\n")
            else:
                #Ver se tem horario
                check=0
                for mtm in aluno.materias_atuais: #pega a string materia
                    if tipo == 1:
                        if escolha_insercao in grade_externa:
                            for horarios_atuais_materias in grade_externa[mtm].horario: #pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_externa[escolha_insercao].horario: #loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check=1
                                        print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_externa[mtm].nome} é conflitante com a que voce quer aplicar ({grade_externa[escolha_insercao].nome}).")
                                    break
                                break
                            break
                        else:
                            for horarios_atuais_materias in grade_CC[mtm].horario: #pega essa string materia e acessa seus horarios
                                for horarios_materias in grade_CC[escolha_insercao].horario: #loopa os horario da materia escolhida com a materia que possui
                                    if horarios_atuais_materias == horarios_materias:
                                        check=1
                                        print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_CC[mtm].nome} é conflitante com a que voce quer aplicar ({grade_CC[escolha_insercao].nome}).")
                                    break
                                break
                            break
                    else:
                        for horarios_atuais_materias in grade_CC[mtm].horario: #pega essa string materia e acessa seus horarios
                            for horarios_materias in grade_CC[escolha_insercao].horario: #loopa os horario da materia escolhida com a materia que possui
                                if horarios_atuais_materias == horarios_materias:
                                    check=1
                                    print(f"Você não tem horário disponível para essa matéria, o horário da diciplina {grade_CC[mtm].nome} é conflitante com a que voce quer aplicar ({grade_CC[escolha_insercao].nome}).")
                                break
                            break
                        break
                if check == 0:
                    break
    ajuste_lista.append(Pedido(aluno,escolha_insercao,escolha_remover))
    print("troca registrada")

def confirmar_ajustes(ajuste_lista):
    if ajuste_lista == []:
        print("não há ajustes para realizar!")
        return
    else:
        for pedido in ajuste_lista:
            #trocas
            if pedido.insercao != None and pedido.remocao != None:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a troca!")
                    continue
                else:
                    print("ajustando a troca: %s" %pedido.aluno.nome, end=",")
                for j in range(len(ajuste_lista)):
                    if pedido == ajuste_lista[j]:
                        continue
                    elif (ajuste_lista[j].insercao == pedido.remocao) and ajuste_lista[j].remocao==None:
                        print("que atende inserção")
                    elif (ajuste_lista[j].remocao == pedido.insercao) and ajuste_lista[j].insercao==None:
                        print("que atende remoção")
                grade_CC[pedido.remocao].ocupado-=1
                pedido.aluno.materias_atuais.remove(pedido.remocao)
                grade_CC[pedido.insercao].ocupado+=1
                pedido.aluno.materias_atuais.append(pedido.insercao)
                print("ajuste efetuado!")
            #remoções
            elif pedido.insercao == None and pedido.remocao != None:
                if not pedido.remocao in pedido.aluno.materias_atuais:
                    print("você não está nessa matéria!!")
                    continue
                grade_CC[pedido.remocao].ocupado-=1
                pedido.aluno.materias_atuais.remove(pedido.remocao)
                print("ajustando remoção %s" %pedido.aluno.nome)
                print("removendo: %s", grade_CC[pedido.remocao].nome)
            #inserções
            else:
                if grade_CC[pedido.insercao].ocupado == grade_CC[pedido.insercao].limite:
                    print("matéria cheia! não vai ser possivel fazer a inserção!")
                    continue
                else:
                    grade_CC[pedido.insercao].ocupado+=1
                    pedido.aluno.materias_atuais.append(pedido.insercao)
                print("ajustando inserção %s" %pedido.aluno.nome)
            ajuste_lista = ['*' if item == pedido else item for item in ajuste_lista]
        ajuste_lista.remove('*')
        print("ajustes efetuados!!")
        return

def matricula():
    print("Processo de matrícula iniciado.")
    w = 0
    while w < 10:
        if w == 4: print("Limite de entradas inválidas atingido. Processo de matrícula encerrado."); return

        q = input("É calouro? (s = sim / n = não): ").lower()
        if q == 's':
            nome = input("Insira o nome: ").strip()
            nome = nome[0].upper() + nome[1:]

            if len(nome) == 0 or nome.isspace() or not all(i.isalpha() or i.isspace() for i in nome):
                print("Entrada inválida.")
                w += 1
            else:
                global id
                id += 1
                calouro = Aluno(id, nome, 3, 10.0, ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363"], [[]], [])

                for i in range(len(calouro.materias_atuais)):
                    if calouro.materias_atuais[i] in grade_CC:
                        if (grade_CC[calouro.materias_atuais[i]].ocupado == grade_CC[
                            calouro.materias_atuais[i]].limite):
                            print("A matéria inserida está cheia.")
                            return
                        else:
                            grade_CC[calouro.materias_atuais[i]].ocupado += 1
                matriculados.append(calouro)
                print("Matrícula efetuada.")
                return
        elif q == 'n':
            if cadastrados == []:
                print("não há matriculas para realizar.")
                return
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
                    print("As matérias de TCC foram adicionadas.")

                x = 0
                y = 0
                count=0
                for materia in grade_CC:
                    if (materia in aluno.materias_pagas) or (materia in aluno.materias_atuais):
                        continue
                    else:
                        print("\033[1m"+materia+"\033[0m"+":",grade_CC[materia].nome, end=" || ")
                        count+=1
                        if count % 4 == 0:
                            print("")
                while True:
                    if x == 4 or y == 4: print(
                        "Limite de entradas inválidas atingido. Processo de matrícula encerrado."); break
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
                            sel = input(
                                "Selecione uma matéria para se matrícular (para encerrar, insira 'e'): ").upper()
                            if sel == 'E':
                                matriculados.append(aluno)
                                cadastrados.remove(aluno)
                                print("Matrícula efetuada.")
                                return
                            else:
                                break

                    if sel not in mat_lista:
                        print("A matéria informada não se encontra no sistema.")
                        y += 1
                    else:
                        if sel in aluno.materias_pagas:  # Checa se o aluno já pagou a matéria.
                            print("Você já pagou essa matéria.")
                        elif sel in grade_CC:
                            for i in range(len(aluno.materias_atuais)):
                                for j in range(len(grade_CC[aluno.materias_atuais[i]].horario)):
                                    for k in range(len(grade_CC[sel].horario)):
                                        if grade_CC[aluno.materias_atuais[i]].horario[j] == grade_CC[sel].horario[k]:
                                            print("Horários conflitantes.")
                                            return
                            print(grade_CC[sel].nome)
                            if grade_CC[sel].ocupado == grade_CC[sel].limite:
                                print("Matéria cheia.")
                                return
                            check = 0
                            if grade_CC[sel].pre_requisitos != []:
                                for i in range(len(grade_CC[sel].pre_requisitos)):
                                    if not grade_CC[sel].pre_requisitos[i] in aluno.materias_pagas:
                                        print("Não cumpre os pré-requisitos para ingressar na matéria.")
                                        check=1
                                        break
                            if check == 1:
                                continue
                            
                            #remover de pendencias
                            if sel in aluno.pendencias:
                                aluno.pendencias.remove(sel)

                            aluno.materias_atuais.append(sel)
                            grade_CC[sel].ocupado += 1
                            print(len(aluno.materias_atuais))
                        else:
                            print("A matéria informada não se encontra no sistema.")
                            x += 1
            return
        else:
            print("Entrada inválida!")
            w += 1
            
counter = 0
encerrado=0
while True:
    if counter == 4:
        print("Limite de entradas inválidas atingido. Programa encerrado.")
        exit()
    x = input(
        "\nBem-vindo ao sistema de matrícula, ajuste e reajuste.\n(1) - Matrícula;\n(2) - Ajuste;\n(3) - Encerrar período de ajustes;\n(4) - Reajuste;\n(5) - Confirmar reajuste;\n(6) - Encerrar programa.\nSelecione uma opção: ")
    if x == '1':
        matricula()
        for i in range(len(matriculados)):
            print("\n#", str(matriculados[i].id) + ' nome: ' + matriculados[i].nome + ' m_atuais:' + str(
                matriculados[i].materias_atuais) + ' coef:' + str(
                matriculados[i].coeficiente) + ' fluxo:' + str(matriculados[i].fluxo) + ' m_pagas' + str(
                matriculados[i].materias_pagas) + ' pendencias' + str(matriculados[i].pendencias))
    elif x == '5':
        print("Programa encerrado.")
        exit()
    elif x == '2':
        ajuste_reajuste(0)
    elif x == '3':
        confirmar_ajustes(ajuste_lista)
        encerrado=1
    elif x == '4':
        if encerrado == 1:
            ajuste_reajuste(1)
        else:
            print ("")
    elif x == '5':
        encerrar_reajuste()
    else:
        print("Entrada inválida!")
        counter += 1