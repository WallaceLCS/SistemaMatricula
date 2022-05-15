class Disciplina:
    def __init__(self, nome: str, pre_requisitos: list, horario: list, tipo: int):
        self.nome = nome
        self.pre_requisitos = pre_requisitos
        self.horario = horario
        self.limite = 10
        self.ocupado = 0 #quantos estão atualmente matriculados
        self.tipo = tipo


grade_CC = {
    #1º periodo
    "COMP359": Disciplina("Programação 1", [], ['SX07300910', 'SX09201100'], 0),
    "COMP360": Disciplina("Lógica para Computação", [], ['SG11101250', 'QA11101250'], 0),
    "COMP361": Disciplina("Computação, Sociedade e Ética", [], ['SE09201100', 'QA09201100'], 0),
    "COMP362": Disciplina("Matemática Discreta", [], ['SG07300910', 'QI07300910'], 0),
    "COMP363": Disciplina("Cálculo Diferencial e Integral", [], ['TE07201110', 'QI07201110'], 0),
    #2º periodo
    "COMP364": Disciplina("Estrutura de Dados", ["COMP359"], ['SE13301510', 'QA13301510'], 0),
    "COMP365": Disciplina("Banco de Dados", [], ['TE15201700', 'QI15201700'], 0),
    "COMP366": Disciplina("Organização e Arquitetura de Computadores", [], ['SE17101850', 'QA17101850'], 0),
    "COMP367": Disciplina("Geometria Analítica", [], ['SE15201700', 'QA15201700'], 0),
    #3º periodo
    "COMP368": Disciplina("Redes de Computadores", ["COMP359"], ['TE07201110', 'QI07201110'], 0),
    "COMP369": Disciplina("Teoria dos Grafos", ["COMP364", "COMP362"], ['SE09201100', 'TE09201100'], 0),
    "COMP370": Disciplina("Probabilidade e Estatística", ["COMP363"], ['SE07300910', 'QA07300910'], 0),
    "COMP371": Disciplina("Álgebra Linear", ["COMP367"], ["SE11101250", "QA09201100"], 0),
    
    #4º periodo
    "COMP372": Disciplina("Programação 2", ["COMP364", "COMP365", "COMP368"], ['QA13301510', 'QA15201700'], 0),
    "COMP373": Disciplina("Programação 3", ["COMP364", "COMP365", "COMP368"], ['TE15201700', 'QI15201700'], 0),
    "COMP374": Disciplina("Projeto e Análise de Algorítimos", ["COMP364", "COMP369"], ['SE13301510', 'QA17101850'], 1),
    "COMP376": Disciplina("Teoria da Computação", [], ['TE13301510', 'QI13301510'], 0),
    #5º periodo
    "COMP378": Disciplina("Sistemas Operacionais", ["COMP366"], ['SE0730910', 'QA0730910'], 0),
    "COMP379": Disciplina("Compiladores", ["COMP364", "COMP376"], ['SE11101250', 'QA11101250'], 0),
    "COMP380": Disciplina("Inteligencia Artificial", ["COMP360", "COMP364"], ['SE09201100', 'QA09201100'], 0),
    "COMP381": Disciplina("Computação Gráfica", [], ['TE07200910', 'QI07200910'], 0),
    #6º periodo
    "COMP382": Disciplina("Projeto e Desenvolvimento de Sistemas", ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP367", "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380", "COMP381"], ['SE07201110','TE07201110', 'QA07201110', 'QI07201110'], 0),
    #7º periodo
    "COMP386": Disciplina("Metodologia de Pesquisa e Trabalho Individual", [], ['SX07300910', 'QA07300910'], 0),
    "COMP387": Disciplina("Noções de Direito", [], ['SX09201100', 'SX11101250'], 0),
    
    #ENFASES
    "COMP389": Disciplina("Conceitos de Linguagem de Programação", [], ['TE13301510', 'QI13301510'], 1),
    "COMP390": Disciplina("Aprendizagem de Máquina", ["COMP404"], ['TE17101850', 'QI17101850'], 1),
    "COMP391": Disciplina("Sistemas Digitais", ["COMP404"], ['TE15201700','SX15201700'], 1),
    "COMP392": Disciplina("Sistemas Distribuidos", [], ['TE15201700','QI15201700'], 1),
    "COMP393": Disciplina("Redes Neurais e Aprendizado Profundo", [], ["SE09201100",'SE11101250'], 1),
    "COMP394": Disciplina("FPGA", [], [], 1),###
    "COMP395": Disciplina("Iteração Homem-Máquina", ["COMP373"], ['TE07200910','QI07200910'], 1),
    "COMP396": Disciplina("Processamento Digital de Imagens", ["COMP381"], ['SE09201100','QA09201100'], 1),
    "COMP397": Disciplina("Computação Evolucionária", [], ['SE09201100','QA09201100'], 1),
    "COMP398": Disciplina("Sistemas Embarcados", [], [], 1),###
    "COMP399": Disciplina("Gerencia de Projeto", ["COMP382"], ['TE17101850','QI17101850'], 1),
    "COMP400": Disciplina("Visão Computacional", [], ['SE15201700','QA15201700'], 1),
    "COMP401": Disciplina("Ciencia de Dados", ["COMP370"], ['SE15201700','QA15201700'], 1),
    "COMP402": Disciplina("Microcontroladores e Aplicações", [], ['QA13301510','SX13301510'], 1),
    "COMP403": Disciplina("Segurança de Sistemas Computacionais", ["COMP368"], ['QA09201100','SX09201100'], 1),
    "COMP404": Disciplina("Calculo 3", ["COMP363"], ['TE13301510','QI13301510'], 1),
    "COMP405": Disciplina("Tópicos em Ciência da Computação 1 ", [], [], 1),
    "COMP406": Disciplina("Tópicos em Ciência da Computação 2", [], [], 1),
    "COMP407": Disciplina("Tópicos em Ciência da Computação 3 ", [], [], 1),
    "COMP409": Disciplina("Tópicos em Matemática para Computação 1 ", [], [], 1),
    "COMP410": Disciplina("Tópicos em Matemática para Computação 2 ", [], [], 1),
    "COMP411": Disciplina("Tópicos em Matemática para Computação 3 ", [], [], 1),
    "COMP412": Disciplina("Tópicos em Física para Computação 1 ", [], [], 1),
    "COMP413": Disciplina("Tópicos em Física para Computação 2 ", [], [], 1),
    "COMP414": Disciplina("Tópicos em Física para Computação 3", [], [], 1),

    #ELETIVAS
    "CC1941": Disciplina("Cálculo 4", [], [], 1),
    "CC1942": Disciplina("Cálculo Numérico", [], [], 1),
    "CC1943": Disciplina("Circuitos Digitais", [], [], 1),
    "CC1944": Disciplina("Circuitos Impressos", [], [], 1),
    "CC1945": Disciplina("Fundamentos de Libras", [], [], 1),
    "CC1946": Disciplina("Geometria Computacional", [], [], 1),
    "CC1947": Disciplina("Pesquisa Operacional", [], [], 1),
    "CC1948": Disciplina("Programação para Sistemas Embarcados ", [], [], 1),
    "CC1949": Disciplina("Projeto de Sistemas Embarcados", [], [], 1),
    "CC1950": Disciplina("Tópicos em Arquitetura de Computadores ", [], [], 1),
    "CC1951": Disciplina("Tópicos em Banco de Dados", [], [], 1),
    "CC1952": Disciplina("Tópicos em Computação Científica ", [], [], 1),
    "CC1953": Disciplina("Tópicos em Computação Paralela", [], [], 1),
    "CC1954": Disciplina("Tópicos em Computação Visual", [], [], 1),
    "CC1955": Disciplina("Tópicos em Comunicação de Dados ", [], [], 1),
    "CC1956": Disciplina("Tópicos em Desenvolvimento de Sistemas ", [], [], 1),
    "CC1957": Disciplina("Tópicos em Engenharia de Software", [], [], 1),
    "CC1958": Disciplina("Tópicos em Humanidades ", [], [], 1),
    "CC1959": Disciplina("Tópicos em Informática na Educação", [], [], 1),
    "CC1960": Disciplina("Tópicos em Inteligência Artificial", [], [], 1),
    "CC1961": Disciplina("Tópicos em Linguagens de Programação ", [], [], 1),
    "CC1962": Disciplina("Tópicos em Programação ", [], [], 1),
    "CC1963": Disciplina("Tópicos em Redes de Computadores ", [], [], 1),
    "CC1964": Disciplina("Tópicos em Sistemas de Computação", [], [], 1),
    "CC1965": Disciplina("Tópicos em Sistemas de Informação", [], [], 1),
    "CC1966": Disciplina("Tópicos em Sistemas Distribuídos ", [], [], 1),
    "CC1967": Disciplina("Tópicos em Sistemas Inteligentes", [], [], 1),
    "CC1968": Disciplina("Tópicos em Software Básico ", [], [], 1),
    
    
}

grade_TCC={
    "TCC1": Disciplina("TCC", [], [], 1),
    "TCC2": Disciplina("TCC", [], [], 1),
    "TCC3": Disciplina("TCC", [], [], 1),
}


grade_externa = {
    #Grade de EC
    "ECOM001": Disciplina("Ingles Instrumental",[],['QI13301510', 'QI15201700'],0),
    "ECOM002": Disciplina("Programação 1",[],['SX13301420', 'SX15201700'],0),
    "ECOM003": Disciplina("Matemática Discreta",[],['SE13301510', 'QA13301510'],0),
    "ECOM004": Disciplina("Cálculo 1",[],['TE13301420','QA17101850'],0),
    "ECOM005": Disciplina("Geometria Analítica",[],['SE15201700', 'QA15201700'],0),
    "ECOM006": Disciplina("Introdução à Eng. da Computação",[],['SE17101850', 'TE17101850'],0),
    "ECOM007": Disciplina("Lógica Aplicada à Computação",[],['TE09201100','QA09201100'],0),
    "ECOM008": Disciplina("Estrutura de Dados",[],['SE11101250','QA11101250'],0),
    "ECOM009": Disciplina("Física 1",[],['SE07300910','QA07300910'], 0),
    "ECOM010": Disciplina("Cálculo 2",[],['TE13301510','QI13301510'], 0),
    "ECOM011": Disciplina("Álgebra Linear",[],['SE09201100','QA09201100'], 0),
    "ECOM012": Disciplina("Circuitos Digitais",[],['SX15201700'], 0),
    "ECOM013": Disciplina("Desenho",[],['SX09201100','SX11101250'], 0),
    "ECOM014": Disciplina("Linguagens Formais, Autômatos  e Computibilidade",[],['SE15201700','QI15201700'],0),
    "ECOM015": Disciplina("Projeto de Software",[],['QA15201700','QA17101850'], 0),
    "ECOM016": Disciplina("Física 2",[],['SE13301510','QA13301510'],0),
    "ECOM017": Disciplina("Cálculo 3",[],['TE13301510','QU13301510'],0),
    "ECOM018": Disciplina("Metodologia da Pesquisa e do Trabalho Científico",[],['SX11101250'],0),
    "ECOM019": Disciplina("Sistemas Digitais",[],['TE15201700','QI15201700'],0),
    "ECOM057": Disciplina("Química Tecnológica",[],['TE17101850','QI17101850'],0),
    "ECOM020": Disciplina("Probabilidade e Estatística",[],['SE19002040','QA19002040'],0),
    "ECOM021": Disciplina("Engenharia de Software",[],['TE15201700','QI15201700'],0),
    "ECOM022": Disciplina("Física 3",[],['TE09201100','QI09201100'],0),
    "ECOM023": Disciplina("Cálculo 4",[],['SE09201100','QA09201100'],0),
    "ECOM024": Disciplina("Variáveis Complexas",[],['TE11101250','QI11101250'],0),
    "ECOM025": Disciplina("Organização e Arquitetura de Computadores",[],['QA11101250','SX11101250'],0),
    "ECOM026": Disciplina("Física Experimental",[],['QI07300910'],0),
    "ECOM027": Disciplina("Projeto e Análise de Algorítmos",['SE17101850','TE17101850'],[],0),
    "ECOM028": Disciplina("Circuitos Elétricos",[],['SX13301420','SX15201700'],0),
    "ECOM029": Disciplina("Redes de Computadores",[],['TE09201100','QI09201100'],0),
    "ECOM030": Disciplina("Sinais e Sistemas",[],['TE15201700','QI15201700','SX17101850'],0),
    "ECOM031": Disciplina("Inteligência Artificial",[],['SE15201700','QA15201700'],0),
    "ECOM032": Disciplina("Sistemas Operacionais",[],['SE13301510','QA13301510'],0),
    "ECOM033": Disciplina("Teoria dos Grafos",[],['QA17101850'],0),
    "ECOM034": Disciplina("Princípios de Comunicação",[],['QI09201100','SX1101250'],0),
    "ECOM035": Disciplina("Eletrônica",[],['QI1101250','SX09201100'],0),
    "ECOM036": Disciplina("Métodos Numéricos",[],['SE11101250','QA1101250'],0),
    "ECOM037": Disciplina("Sistemas de Controle 1",[],['SE09201100','QA09201100'],0),
    "ECOM048": Disciplina("Computador Sociedade e Ética",[],['TE13301510'],0),
    "ECOM040": Disciplina("Empreendedorismo",[],['SE15201700','TE15201700'],0),
    "ECOM0118": Disciplina("Fenômenos de Transporte",[],['TE07300910','QI07300910'],0),
    "ECOM041": Disciplina("Bancos de Dados",[],['TE15201700','QI15201700'],0),
    "ECOM046": Disciplina("Noções de Direito",[],['SX15201700','SX17101850'],0),
    "ECOM058": Disciplina("Sistemas de Controle 2",[],['TE13301510','QI13301510'],0),
    "ECOM059": Disciplina("Microcontroladores e Aplicações",[],['QA13301510','SX13301510'],0),
    "ECOM060": Disciplina("Instrumentação Eletrônica",[],['TE17101850','QI17101850'],0),
    "ECOM063": Disciplina("Processamento Digital de Sinais",[],['SE15201700','QA15201700'],0),
    "ECOM039": Disciplina("Computação Gráfica e Processamento de Imagens",[],[''],0),
    "ECOM042": Disciplina("Sistemas Embarcados",[],['QA1101250','SX1101250'],0),
    "ECOM044": Disciplina("Sistemas Distribuídos",[],['TE15201700','QU15201700'],0),
    "ECOM061": Disciplina("Automação Industrial",[],['QI07300910','SX07300910'],0),
    "ECOM062": Disciplina("Robótica",[],['SE07300910','QA07300910'],0),
    "ECOM0119": Disciplina("Mecânica dos Sólidos",[],['SE13301510','SX13301510'],0),

    #ELETIVAS EC
    "ECOM038": Disciplina("Conceitos de Linguagem de Programação",[],['TE13301510','QI13301510'],0),
    "ECOM043": Disciplina("Sistemas de Evento Discretos",[],[],0),
    "ECOM045": Disciplina("Compiladores",[],['SE17101850','QA17101850'],0),
    "ECOM047": Disciplina("Paradigmas de Linguagem de Programação",[],[],0),
    "ECOM049": Disciplina("Gerência de Projetos",[],['TE17101850','QI17101850'],0),
    "ECOM050": Disciplina("Laboratório de Programação",[],[''],0),
    "ECOM052": Disciplina("Fundamentos de Libras",[],[],0),
    "ECOM053": Disciplina("Desenvolvimento Baseado em Ontologias",[],[],0),
    "ECOM054": Disciplina("Processamento Digital de Sinais",[],[],0),
    "ECOM055": Disciplina("Tópicos Especiais em Circuitos Elétricos",[],[],0),
    "ECOM056": Disciplina("Laboratório de Estrutura de Dados",[],[],0),
    "ECOM065": Disciplina("Tópicos em Sistemas Distribuídos: Paradigmas Modernos",[],[],0),
    "ECOM066": Disciplina("Laboratório de Eletrônica",[],[],0),
    "ECOMO67": Disciplina("Laboratório de Circuitos Eletrônicos",[],[],0),
    "ECOM068": Disciplina("Laboratório de Eletrônica",[],[],0),
    "ECOM069": Disciplina("Tópicos em Sistemas Distribuídos: Algoritmos Distribuídos I",[],[],0),
    "ECOM070": Disciplina("Tópicos em Sistemas Distribuídos: Algoritmos Distribuídos II",[],[],0),
    "ECOM071": Disciplina("Redes de Petri",[],['SE13301510','QA13301510'],0),
    "ECOM072": Disciplina("Introdução a Teoria da Informação",[],[],0),
    "ECOM073": Disciplina("Inteligência Artificial 2",[],['SE17101850','QA17101850'],0),
    "ECOM074": Disciplina("Desenvolvimento com QT/C++",[],[],0),
    
    #GRADE DO IM
    "MATB001": Disciplina("Geometria Analítica", [], ['SE13301510', 'QA13301510'], 0),
    "MATB006": Disciplina("Álgebra Linear 1", [], ['SE15201700', 'QA15201700'], 0),
    "MATB008": Disciplina("Cálculo 1", [], ['TE13301510', 'QI13301510'], 0),
    "MATB013": Disciplina("Cálculo 2", [], ['TE19002040', 'QI20502230'], 0),
    "MATB015": Disciplina("Cálculo 3", [], ['TE13301510', 'QI13301510'], 0),
    "MATB019": Disciplina("Cálculo 4", [], ['SE13301510', 'QA13301510'], 0),
    
    #GRADE DO IF
    "FISB085": Disciplina("Cálculo 1", [], ['TE07300910', 'QI07300910'], 0),
    "FISB086": Disciplina("Geometria Analítica", [], ['SE09201100', 'QA09201100'], 0),
    "FISB090": Disciplina("Cálculo 2", [], ['TE09201100', 'QI909201100'], 0),
    "FISB091": Disciplina("Álgebra Linear", [], ['SE09201100', 'QA09201100'], 0),
    "FISB095": Disciplina("Cálculo 3", [], ['TE07300910', 'QI07300910'], 0),
    "FISB100": Disciplina("Cálculo 4", [], ['SE09201100', 'QA09201100'], 0),
}

#Para a checagem de entradas.
mat_lista = ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP368", "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380", "COMP381", "COMP382", "COMP386", "COMP387", "COMP389", "COMP390", "COMP391", "COMP392", "COMP393", "COMP394", "COMP395", "COMP396", "COMP397", "COMP398", "COMP399", "COMP400", "COMP401", "COMP402", "COMP403", "COMP404", "COMP405", "COMP406", "COMP407","COMP409", "COMP410", "COMP411", "COMP412", "COMP413", "COMP414", "CC1941", "CC1942", "CC1943", "CC1944", "CC1945", "CC1946", "CC1947", "CC1948", "CC1949", "CC1950", "CC1951", "CC1952", "CC1953", "CC1954", "CC1955", "CC1956", "CC1957", "CC1958", "CC1959", "CC1960", "CC1961", "CC1962", "CC1963", "CC1964", "CC1965", "CC1966", "CC1967", "CC1968","TCC1","TCC2","TCC3"]

mat_lista_externa = ['ECOM001', 'ECOM002', 'ECOM003', 'ECOM004', 'ECOM005', 'ECOM006', 'ECOM007', 'ECOM008', 'ECOM009', 'ECOM010', 'ECOM011', 'ECOM012', 'ECOM013', 'ECOM014', 'ECOM015', 'ECOM016', 'ECOM017', 'ECOM018', 'ECOM019', 'ECOM057', 'ECOM020', 'ECOM021', 'ECOM022', 'ECOM023', 'ECOM024', 'ECOM025', 'ECOM026', 'ECOM027', 'ECOM028', 'ECOM029', 'ECOM030', 'ECOM031', 'ECOM032', 'ECOM033', 'ECOM034', 'ECOM035', 'ECOM036', 'ECOM037', 'ECOM048', 'ECOM040', 'ECOM0118', 'ECOM041', 'ECOM046', 'ECOM058', 'ECOM059', 'ECOM060', 'ECOM063', 'ECOM039', 'ECOM042', 'ECOM044', 'ECOM061', 'ECOM062', 'ECOM0119', 'ECOM038', 'ECOM043', 'ECOM045', 'ECOM047', 'ECOM049', 'ECOM050', 'ECOM052', 'ECOM053', 'ECOM054', 'ECOM055', 'ECOM056', 'ECOM065', 'ECOM066', 'ECOMO67', 'ECOM068', 'ECOM069', 'ECOM070', 'ECOM071', 'ECOM072', 'ECOM073', 'ECOM074',"MATB001","MATB006","MATB008","MATB013","MATB015","MATB019","FISB085","FISB086","FISB090","FISB091","FISB095","FISB100"]