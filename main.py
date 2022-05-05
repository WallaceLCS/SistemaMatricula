from materias import grade_curricular


class Alunos:

    def __init__(self, nome, periodo, fluxo, coeficiente):
        self.nome = nome  # Geralt of Rivia, James Howlett...
        # 1st period (1), 2nd period (2), 3rd period (3)...
        self.periodo = periodo
        self.fluxo = fluxo  # continuum (c), individual (i)
        self.coeficiente = coeficiente
        self.horarios = []
        self.materias_pagas = []


def Matricula():
    nome = input("informe o nome")
    periodo = input("informe o período")
    fluxoo = input("informe o fluxoo")
    coef = input("informe o coeficiente atual")
    return Alunos(nome, periodo, fluxoo, coef)


def ajuste():
    pass


op = ['1', '2', '3']
alunos = []

print("Olá bem-vindo ao sistema de matrícula, ajuste e reajuste de alunos")
while True:
    print("selecione uma das seguintes opções:")
    print(" 1 - Matrícula")
    print(" 2 - Ajuste")
    print(" 3 - Reajuste")
    opcao = input("")
    if not (opcao in op):
        print("opção inválida!!")
    else:
        if(opcao == '1'):
            aluno = Matricula()
            print(aluno.nome)
