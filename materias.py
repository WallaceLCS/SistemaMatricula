class Disciplinas:
    def _init_(self, nome: str, pre_requisitos: list, horario: list):
        self.nome = nome
        self.pre_requisitos = pre_requisitos
        self.horario = horario
        self.limite = 10
        self.ocupado = 0 #quantos estão atualmente matriculados


grade_curricular = {
    #1º periodo
    "COMP359": Disciplinas("Programação 1", [], ['SX07300910', 'SX09201100']),
    "COMP360": Disciplinas("Lógica para Computação", [], ['SG11101250', 'QA11101250']),
    "COMP361": Disciplinas("Computação, Sociedade e Ética", [], ['SE09201100', 'QA09201100']),
    "COMP362": Disciplinas("Matemática Discreta", [], ['SG07300910', 'QI07300910']),
    "COMP363": Disciplinas("Cálculo Diferencial e Integral", [], ['TE07201110', 'QI07201110']),
    #2º periodo
    "COMP364": Disciplinas("Estrutura de Dados", ["COMP359"], ['SE13301510', 'QA13301510']),
    "COMP365": Disciplinas("Banco de Dados", [], ['TE15201700', 'QI15201700']),
    "COMP366": Disciplinas("Organização e Arquitetura de Computadores", [], ['SE17101850', 'QA17101850']),
    "COMP367": Disciplinas("Geometria Analítica", [], ['SE15201700', 'QA15201700']),
    #3º periodo
    "COMP368": Disciplinas("Redes de Computadores", ["COMP359"], []),
    "COMP369": Disciplinas("Teoria dos Grafos", ["COMP364", "COMP362"], []),
    "COMP370": Disciplinas("Probabilidade e Estatística", ["COMP363"], []),
    "COMP371": Disciplinas("Álgebra Linear", ["COMP367"], []),
    
    #4º periodo
    "COMP372": Disciplinas("Programação 2", ["COMP364", "COMP365", "COMP368"], []),
    "COMP373": Disciplinas("Programação 3", ["COMP364", "COMP365", "COMP368"], []),
    "COMP374": Disciplinas("Projeto e Análise de Algorítimos", ["COMP364", "COMP369"], []),
    "COMP376": Disciplinas("Teoria da Computação", [], []),
    "COMP378": Disciplinas("Sistemas Operacionais", ["COMP366"], []),
    "COMP379": Disciplinas("Compiladores", ["COMP364", "COMP376"], []),
    "COMP380": Disciplinas("Inteligencia Artificial", ["COMP360", "COMP364"], []),
    "COMP381": Disciplinas("Computação Gráfica", [], []),
    "COMP382": Disciplinas("Projeto e Desenvolvimento de Sistemas", ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP367", "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380", "COMP381"], []),
    "COMP386": Disciplinas("Metodologia de Pesquisa e Trabalho Individual", [], ['SX07300910']),
    "COMP387": Disciplinas("Noções de Direito", [], []),
    "COMP389": Disciplinas("Conceitos de Linguagem de Programação", [], []),
    "COMP390": Disciplinas("Aprendizagem de Máquina", ["COMP404"], []),
    "COMP391": Disciplinas("Sistemas Digitais", ["COMP404"], []),
    "COMP392": Disciplinas("Sistemas Distribuidos", [], []),
    "COMP393": Disciplinas("Redes Neurais e Aprendizado Profundo", [], []),
    "COMP394": Disciplinas("FPGA", [], []),
    "COMP395": Disciplinas("Iteração Homem-Máquina", ["COMP373"], []),
    "COMP396": Disciplinas("Processamento Digital de Imagens", ["COMP381"], []),
    "COMP397": Disciplinas("Computação Evolucionária", [], []),
    "COMP398": Disciplinas("Sistemas Embarcados", [], []),
    "COMP399": Disciplinas("Gerencia de Projeto", ["COMP382"], []),
    "COMP400": Disciplinas("Visão Computacional", [], []),
    "COMP401": Disciplinas("Ciencia de Dados", ["COMP370"], []),
    "COMP402": Disciplinas("Microcontroladores e Aplicações", [], []),
    "COMP403": Disciplinas("Segurança de Sistemas Computacionais", ["COMP368"], []),
    "COMP404": Disciplinas("Calculo 3", ["COMP363"], []),
    "COMP405": Disciplinas("Tópicos em Ciência da Computação 1 ", [], []),
    "COMP406": Disciplinas("Tópicos em Ciência da Computação 2", [], []),
    "COMP407": Disciplinas("Tópicos em Ciência da Computação 3 ", [], []),
    "COMP409": Disciplinas("Tópicos em Matemática para Computação 1 ", [], []),
    "COMP410": Disciplinas("Tópicos em Matemática para Computação 2 ", [], []),
    "COMP411": Disciplinas("Tópicos em Matemática para Computação 3 ", [], []),
    "COMP412": Disciplinas("Tópicos em Física para Computação 1 ", [], []),
    "COMP413": Disciplinas("Tópicos em Física para Computação 2 ", [], []),
    "COMP414": Disciplinas("Tópicos em Física para Computação 3", [], []),

    "CC1941": Disciplinas("Cálculo 4", [], []),
    "CC1942": Disciplinas("Cálculo Numérico", [], []),
    "CC1943": Disciplinas("Circuitos Digitais", [], []),
    "CC1944": Disciplinas("Circuitos Impressos", [], []),
    "CC1945": Disciplinas("Fundamentos de Libras", [], []),
    "CC1946": Disciplinas("Geometria Computacional", [], []),
    "CC1947": Disciplinas("Pesquisa Operacional", [], []),
    "CC1948": Disciplinas("Programação para Sistemas Embarcados ", [], []),
    "CC1949": Disciplinas("Projeto de Sistemas Embarcados", [], []),
    "CC1950": Disciplinas("Tópicos em Arquitetura de Computadores ", [], []),
    "CC1951": Disciplinas("Tópicos em Banco de Dados", [], []),
    "CC1952": Disciplinas("Tópicos em Computação Científica ", [], []),
    "CC1953": Disciplinas("Tópicos em Computação Paralela", [], []),
    "CC1954": Disciplinas("Tópicos em Computação Visual", [], []),
    "CC1955": Disciplinas("Tópicos em Comunicação de Dados ", [], []),
    "CC1956": Disciplinas("Tópicos em Desenvolvimento de Sistemas ", [], []),
    "CC1957": Disciplinas("Tópicos em Engenharia de Software", [], []),
    "CC1958": Disciplinas("Tópicos em Humanidades ", [], []),
    "CC1959": Disciplinas("Tópicos em Informática na Educação", [], []),
    "CC1960": Disciplinas("Tópicos em Inteligência Artificial", [], []),
    "CC1961": Disciplinas("Tópicos em Linguagens de Programação ", [], []),
    "CC1962": Disciplinas("Tópicos em Programação ", [], []),
    "CC1963": Disciplinas("Tópicos em Redes de Computadores ", [], []),
    "CC1964": Disciplinas("Tópicos em Sistemas de Computação", [], []),
    "CC1965": Disciplinas("Tópicos em Sistemas de Informação", [], []),
    "CC1966": Disciplinas("Tópicos em Sistemas Distribuídos ", [], []),
    "CC1967": Disciplinas("Tópicos em Sistemas Inteligentes", [], []),
    "CC1968": Disciplinas("Tópicos em Software Básico ", [], []),
}


horarios = ['SG07300910', 'SG09201100', 'SG11101250', 'SG13301510',
            'SG15201700', 'SG17101850', 'SG09201200']
['TE07201110', 'TE07300910', 'TE09201200', 'TE09201100', 'TE11101250', 'TE13301510',
    'TE15201700', 'TE17101850']
['QA07300910', 'QA09201200', 'QA09201100', 'QA11101250', 'QA13301510',
    'QA15201700', 'QA17101850']
['QI07300910', 'QI09201200', 'QI09201100', 'QI11101250', 'QI13301510',
    'QI15201700', 'QI17101850']
['SX09201100', 'SX11101250', 'SX13301510',
    'SX15201700', 'SX17101850']
