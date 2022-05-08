from materias import grade_curricular


id=0 
class Aluno:

    def __init__(self, matricula, nome, periodo, fluxo, coeficiente , n_materias):
        self.matricula = matricula
        self.nome = nome  # Geralt of Rivia, James Howlett...
        # 1st period (1), 2nd period (2), 3rd period (3)...
        self.periodo = periodo
        self.fluxo = fluxo  # continuum (c), individual (i)
        self.coeficiente = coeficiente
        self.horarios = []
        self.materias_pagas = []
        self.n_materias_atuais = n_materias


def matricula():
    print("Processo de matrícula iniciado.")

    w = 0
    while w < 10:
        if w == 4:
            print(
                "Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
            return

        n = input("Insira o nome: ").strip()
        n = n[0].upper() + n[1:]

        if len(n) == 0 or n.isspace():
            print("Entrada inválida!")
            w += 1
        elif all(i.isalpha() or i.isspace() for i in n):
            print("Seu nome é: %s" % n)
            w += 10
        else:
            print("Entrada inválida!")
            w += 1

    x = 0
    while x < 10:
        if x == 4:
            print(
                "Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
            return

        if x == 0:
            q = input("É calouro? (s = sim / n = não): ").lower()
        if q == 's':
            p = '0'
            break

        elif q == 'n':
            ps = ['1', '2', '3', '4', '5', '6', '7', '8']
            p = input("Insira o péríodo: ")
            if p in ps:
                print("Seu período é o: %sº" % p)
                x += 10
            else:
                print("Entrada inválida!")
                x += 1
        else:
            print("Entrada inválida!")
            x += 1

    y = 0
    while y <= 4:
        if y == 4:
            print(
                "Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
            return

        if p == '0':
            f = 'p'
            print("Seu fluxo é padrão (%s)." % f)
            break
        elif p == '1':
            f = 'i'
            print("Seu fluxo é individual (%s)." % f)
            break

        f = input("Insira o fluxo (p = padrão; i = individual): ").lower()

        if f == 'p':
            print("Seu fluxo é: %s" % f)
            y += 10
        elif f == 'i':
            print("Seu fluxo é: %s" % f)
            y += 10
        else:
            print("Entrada inválida!")
            y += 1

    z = 0
    while z <= 4:
        if z == 4:
            print(
                "Limite de entradas inválidas atingido. Processo de matrícula encerrado.")
            return

        try:
            c = float(input("Insira o coeficiente de rendimento (ex.: 8.5): ").replace(
                ',', '.').replace(';', '.'))
            if c < 0 or c > 10:
                print("Entrada inválida!")
                z += 1
            else:
                print("Seu coeficiente de rendimento é: %.2f" % c)
                z += 10
                break
        except ValueError:
            z += 1
            print("Entrada inválida!")
    global id 
    id+=11
    print("Os dados são: %s, %s, %s, %.2f." % (n, p, f, c))
    Cadastrados.append(Aluno(id,n,p,f,c))

Cadastrados=[]
counter = 0
while True:
    if counter == 4:
        print("Limite de entradas inválidas atingido. Programa encerrado.")
        exit()
    x = input("\nBem-vindo ao sistema de matrícula, ajuste e reajuste.\n1 - Matrícula;\n2 - Ajuste;\n3 - Reajuste;\n4 - Encerrar programa.\nSelecione uma opção: ")
    if x == '1':
        matricula()
        print(Cadastrados)
    elif x == '4':
        print("Programa encerrado.")
        exit()
    else:
        print("Entrada inválida!")
        counter += 1
