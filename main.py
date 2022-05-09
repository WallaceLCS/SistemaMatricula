from materias import grade_curricular

id:int=0 
class Aluno:

    def __init__(self, matricula:int, nome:str, periodo:str, fluxo:str, coeficiente:float, status:str):
        self.matricula = matricula
        self.nome = nome  # Geralt of Rivia, James Howlett...
        self.periodo = periodo # 1,2,3,4,5,6,7,8
        self.fluxo = fluxo  # continuum (c), individual (i)
        self.coeficiente = coeficiente
        self.status = status #calouro, None, formando
        self.materias_atuais = []
        self.materias_pagas = []

#TALVEZ SEJA MELHOR PEDIR PRIMEIRO O NUMERO DA MATRÍCULA PARA O ALUNO CASO ELE NÃO SEJA CALOURO
#DESSA FORMA É POSSIVEL JÁ 'PUXAR' OS DADOS DELE
Cadastrados:Aluno=[]

def matricula():
    print("Processo de matrícula iniciado.")
    q = input("É calouro? (s = sim / n = não): ").lower()
    #caso 1 : Calouro
    if (q == "s"):
        global id
        id+=1
        w = 0
        while True:
            if w == 4:
                print("Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
                return

            n = input("Insira o nome: ").strip()
            n = n[0].upper() + n[1:]

            if len(n) == 0 or n.isspace() or not all(i.isalpha() or i.isspace() for i in n):
                print("Entrada inválida!")
                w += 1
            else:
                print("Sua matricula é: %d" % id)
                print("Seu nome é: %s" % n)
                break
        aluno = Aluno(id, n, '1', 'c', 10.0,'Calouro')
        aluno.materias_atuais = ["COMP359","COMP360","COMP361","COMP362","COMP363"]
        Cadastrados.append(aluno)
    #caso 2: Normal
    elif(q == 'n'):
        mat = int(input("informe a sua matricula: "))
        check= 0
        for i in range(len(Cadastrados)):
            if Cadastrados[i].matricula == mat:
                aluno = Cadastrados[i]
                check = 1
                break
        if check == 0:
            print("matricula inexistente")
            return
        else:
            if (len(aluno.materias_atuais) == 10):
                print("não é permitido se matricular em +10 matérias ao mesmo tempo!!")
                return
            print("liste quais matérias das atuais já foram pagas:\n")
            print(aluno.materias_atuais)
            pagas = list(map(str, input("").split()))
            for i in range(len(pagas)):
                if pagas[i] in aluno.materias_atuais:
                    aluno.materias_atuais.remove(pagas[i])
                    print(aluno.materias_atuais)
                    aluno.materias_pagas.append(pagas[i])
                print(aluno.materias_pagas)
            x = 0
            while True:
                if x == 4:
                    print("Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
                    return
                ps = ['1', '2', '3', '4', '5', '6', '7', '8']
                p = input("Insira o péríodo: ")
                if p in ps:
                    print("Seu período é o: %sº" % p)
                    aluno.período = p
                    break
                else:
                    print("Entrada inválida!")
                    x += 1
                if p == '8':
                    aluno.status = 'formando'
                else:
                    aluno.status = None    
                    
            f = str(input("informe seu fluxo: c - continuo / i - individual\n"))
            #fluxo esta inválido por algum motivo
            if(f!="c" or f!="i"):
                print("fluxo inválido!!")
                return
            else:
                aluno.fluxo = f
            z = 0
            while z <= 4:
                if z == 4:
                    print("Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
                    return
                try:
                    c = float(input("Insira o coeficiente de rendimento (ex.: 8.5): ").replace(
                        ',', '.').replace(';', '.'))
                    if c < 0 or c > 10:
                        print("Entrada inválida!")
                        z += 1
                    else:
                        print("Seu coeficiente de rendimento é: %.2f" % c)
                        aluno.coeficiente = c
                        return
                except ValueError:
                    z += 1
                    print("Entrada inválida!")
            print("Selecione as matérias que deseja pagar:")
            #!!!!!!
            #metodo de apresentação das matérias
            #possivel função de filtragem dos dados de acordo com o fluxo??
            #!!!!!!!
            while True:
                materia_selecionada = input("informe o codigo da matéria")
                if materia_selecionada in grade_curricular:
                    aluno.materias_atuais.append(materia_selecionada)
                if(len(aluno.materias_atuais)+1 > 10):
                    print("numero maximo de matérias atingido!\nconcluindo matricula")
                    break
                pronto = input('deseja concluir o processo? (s - sim , n - não)')
                if(pronto == 's'):
                    if (len(aluno.materias_atuais) < 3):
                        print('você não selecionou o minimo de matérias por matrícula\n escolha mais matérias\n')
                    else:
                        break
                elif(pronto != 'n'):
                    print("entrada inválida!")
                    return
    print("Matricula concluida!")
    return
counter = 0
while True:
    if counter == 4:
        print("Limite de entradas inválidas atingido. Programa encerrado.")
        exit()
    x = input("\nBem-vindo ao sistema de matrícula, ajuste e reajuste.\n1 - Matrícula;\n2 - Ajuste;\n3 - Reajuste;\n4 - Encerrar programa.\nSelecione uma opção: ")
    if x == '1':
        matricula()
        print('\nLista cadastrados:')
        for i in range(len(Cadastrados)):
            print('#'+Cadastrados[i].nome)
    elif x == '4':
        print("Programa encerrado.")
        exit()
    else:
        print("Entrada inválida!")
        counter += 1
