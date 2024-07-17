def ler_resposta(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ["S", "N"]:
            return resposta
        else:
            print("Erro: Por favor, responda com 'S' para sim ou 'N' para não.")

def ler_genero(mensagem):
    generos_validos = ["CLASSICO", "FANTASIA", "POEMA", "ROMANCE", "TERROR", "BIOGRAFIA"]
    while True:
        genero = input(mensagem).strip().upper()
        if genero in generos_validos:
            return genero
        else:
            print("Erro: Por favor, escolha um gênero válido (CLASSICO, FANTASIA, POEMA, ROMANCE, TERROR, BIOGRAFIA).")

def ler_numero_livros(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if 1 <= numero <= 10:
                return numero
            else:
                print("Erro: Por favor, insira um número entre 1 e 10.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def ler_selecoes(mensagem, max_opcoes):
    while True:
        selecoes = input(mensagem).strip().split()
        if len(selecoes) <= 10 and all(selecao.isdigit() and 1 <= int(selecao) <= max_opcoes for selecao in selecoes):
            return [int(selecao) for selecao in selecoes]
        else:
            print(f"Erro: Por favor, escolha até 10 números entre 1 e {max_opcoes}.")

def ler_informacao(mensagem, validacao=None):
    while True:
        informacao = input(mensagem).strip()
        if validacao:
            if validacao(informacao):
                return informacao
            else:
                print("Informações invalidas.")
        else:
            return informacao

# Dicionários de livros

classicos = {
    '1': 'Dom Quixote - Miguel de Cervantes',
    '2': 'Os três mosqueteiros - Alexandre Dumas', 
    '3': 'Moby Dick - Herman Melville',
    '4': 'Crime e Castigo - Fiódor Dostoiévski',
    '5': 'O Grande Gatsby - F. Scott Fitzgerald',
    '6': '1984 - George Orwell',
    '7': 'A Odisséia - Homero',
    '8': 'Guerra e Paz - Liev Tolstói',
    '9': 'Retrato de Dorian Gray - Oscar Wilde',
    '10': 'Os Miseráveis - Victor Hugo'
}

fantasia = {
    '1': 'O Senhor dos Anéis - J.R.R. Tolkien',
    '2': 'Harry Potter - J.K. Rowling',
    '3': 'As Crônicas de Nárnia - C.S. Lewis',
    '4': 'O Hobbit - J.R.R. Tolkien',
    '5': 'A Roda do Tempo - Robert Jordan',
    '6': 'O Nome do Vento - Patrick Rothfuss',
    '7': 'A Canção do Gelo e Fogo - George R.R. Martin',
    '8': 'Mistborn: Nascidos da Bruma - Brandon Sanderson',
    '9': 'American Gods - Neil Gaiman',
    '10': 'Percy Jackson - Rick Riordan'
}

poema = {
    '1': 'Divina Comédia - Dante Alighieri',
    '2': 'Ilíada - Homero',
    '3': 'O Corvo e Outros Poemas - Edgar Allan Poe',
    '4': 'As Flores do Mal - Charles Baudelaire',
    '5': 'Folhas de Relva - Walt Whitman',
    '6': 'Cantos de Maldoror - Comte de Lautréamont',
    '7': 'A Eneida - Virgílio',
    '8': 'Paraíso Perdido - John Milton',
    '9': 'Cem Sonetos de Amor - Pablo Neruda',
    '10': 'Odes - Horácio'
}

romance = {
    '1': 'Orgulho e Preconceito - Jane Austen',
    '2': 'Anna Karenina - Liev Tolstói',
    '3': 'Jane Eyre - Charlotte Brontë',
    '4': 'O Morro dos Ventos Uivantes - Emily Brontë',
    '5': 'Madame Bovary - Gustave Flaubert',
    '6': 'Cem Anos de Solidão - Gabriel García Márquez',
    '7': 'A Montanha Mágica - Thomas Mann',
    '8': 'Grandes Esperanças - Charles Dickens',
    '9': 'O Amor nos Tempos do Cólera - Gabriel García Márquez',
    '10': 'Doutor Jivago - Boris Pasternak'
}

terror = {
    '1': 'Drácula - Bram Stoker',
    '2': 'Frankenstein - Mary Shelley',
    '3': 'O Iluminado - Stephen King',
    '4': 'It: A Coisa - Stephen King',
    '5': 'O Exorcista - William Peter Blatty',
    '6': 'A Assombração da Casa da Colina - Shirley Jackson',
    '7': 'O Chamado de Cthulhu - H.P. Lovecraft',
    '8': 'O Médico e o Monstro - Robert Louis Stevenson',
    '9': 'O Bebê de Rosemary - Ira Levin',
    '10': 'Hell House - Richard Matheson'
}

biografia = {
    '1': 'Steve Jobs - Walter Isaacson',
    '2': 'Longa Caminhada até a Liberdade - Nelson Mandela',
    '3': 'A História de Minha Vida - Helen Keller',
    '4': 'O Diário de Anne Frank - Anne Frank',
    '5': 'Eu Sei Por Que o Pássaro Canta na Gaiola - Maya Angelou',
    '6': 'Churchill: Uma Vida - Martin Gilbert',
    '7': 'Alexander Hamilton - Ron Chernow',
    '8': 'Gandhi: A Autobiografia - Mahatma Gandhi',
    '9': 'A Vida Imortal de Henrietta Lacks - Rebecca Skloot',
    '10': 'Albert Einstein: Uma Biografia - Walter Isaacson'
}

# Preços dos gêneros
precos = {
    "CLASSICO": 22.40,
    "FANTASIA": 18.00,
    "POEMA": 10.90,
    "ROMANCE": 12.30,
    "TERROR": 15.00,
    "BIOGRAFIA": 20.00
}

# Chamada das funções
resposta = ler_resposta("Deseja ter acesso ao menu de livros disponíveis? (S/N): ")

if resposta == "S":
    genero = ler_genero("Escolha o gênero do livro (CLASSICO, FANTASIA, POEMA, ROMANCE, TERROR, BIOGRAFIA): ")

    if genero == "CLASSICO":
        livros = classicos
    elif genero == "FANTASIA":
        livros = fantasia
    elif genero == "POEMA":
        livros = poema
    elif genero == "ROMANCE":
        livros = romance
    elif genero == "TERROR":
        livros = terror
    elif genero == "BIOGRAFIA":
        livros = biografia
    else:
        livros = {}

    numero_livros = ler_numero_livros("Quantos livros desse gênero você deseja? (Escolha até 10) ")

    while True:
        print("Livros disponíveis:")
        for chave, livro in livros.items():
            print(f'{chave}: {livro}')

        selecoes = ler_selecoes(f"Escolha os {numero_livros} livros desejados (digite os números separados por espaço): ", len(livros))

        if len(selecoes) > numero_livros:
            resposta_mais = ler_resposta("Você escolheu mais livros do que o desejado. Deseja adquirir mais livros? (S/N): ")
            if resposta_mais == "N":
                print(f"Por favor, escolha exatamente {numero_livros} livros.")
                continue
        break

    total = 0
    print("\nVocê escolheu os seguintes livros:")
    for selecao in selecoes:
        print(f'{selecao}: {livros[str(selecao)]}')
        total += precos[genero]

    print(f"\nO total a pagar é: R${total:.2f}")

 print("\nPor favor, forneça suas informações para cadastro.")
    nome = ler_informacao("Nome completo: ")
    email = ler_informacao("Email: ")
    cpf = ler_informacao("CPF (formato XXX.XXX.XXX-XX): ")
    telefone = ler_informacao("Telefone (formato (XX) XXXXX-XXXX): ")

    print("\nCadastro realizado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"CPF: {cpf}")
    print(f"Telefone: {telefone}")

else:
    print("Acesso ao menu de livros disponíveis negado.")
