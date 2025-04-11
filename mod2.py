nome = input("Digite seu nome: ")

print(f"Olá {nome}! \nDigite a opção desejada:\n")

while True:
    print("1) Verificar triângulo.")
    print("2) Calcular equação do segundo grau.")
    print("3) Conferir data.")
    print("4) Verificar tamanho do texto.")
    print("5) Analisar CPF.")
    print("6) Contar caracteres.")
    print("7) Sair.")
    
    menu = int(input("Digite o número da opção desejada: "))


    if menu == 1:
        print("\nOpção selecionada: Verificar triângulo.")
        lado1 = int(input("Informe o lado A: "))
        lado2 = int(input("Informe o lado B: "))
        lado3 = int(input("Informe o lado C: "))

        if abs(lado2 - lado3) < lado1 < (lado2 + lado3) and \
           abs(lado1 - lado3) < lado2 < (lado1 + lado3) and \
           abs(lado1 - lado2) < lado3 < (lado1 + lado2):
            if lado1 == lado2 == lado3:
                print("É um triângulo equilátero.")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("É um triângulo isósceles.")
            else:
                print("É um triângulo escaleno.")
        else:
            print("Os valores informados não formam um triângulo.")

    elif menu == 2:
        print("\nOpção selecionada: Calcular equação do segundo grau.")
        a = int(input("Digite o coeficiente a: "))
        b = int(input("Digite o coeficiente b: "))
        c = int(input("Digite o coeficiente c: "))

        if a == 0:
            print("Isso não caracteriza uma equação do segundo grau.")
        else:
            delta = (b ** 2) - (4 * a * c)
            if delta > 0:
                raiz1 = (-b + delta ** 0.5) / (2 * a)
                raiz2 = (-b - delta ** 0.5) / (2 * a)
                print(f"A equação possui duias raizes reais: {raiz1} e {raiz2}")
            elif delta == 0:
                raiz = -b / (2 * a)
                print(f"A equação possui uma raiz real: {raiz}")
            else:
                print("A equação não possui nenhuma raíze real.")

    elif menu == 3:
        print("\nOpção selecionada: Conferir data")
        try:
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
        except ValueError:
            print("Formato de data inválido. Certifique-se de digitar números inteiros para dia e mês.")
            continue

        if mes < 1 or mes > 12:
            print("Mês inválido. Deve estar entre 1 e 12.")
        elif mes == 2:
            if dia < 1 or dia > 28:
                print("Data inválida: fevereiro tem no máximo 28 dias (não considerando anos bissextos).")
            else:
                print("Data válida.")
        elif mes in [4, 6, 9, 11]:
            if dia < 1 or dia > 30:
                print(f"Data inválida: o mês {mes} tem no máximo 30 dias.")
            else:
                print("Data válida.")
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia < 1 or dia > 31:
                print(f"Data inválida: o mês {mes} tem no máximo 31 dias.")
            else:
                print("Data válida.")

    elif menu == 4:
        print("\nOpção selecionada: Verificar tamanho do texto.")
        texto = input("Insira um texto: ")
        tamanho = len(texto)

        if tamanho < 5:
            print("O texto é muito curto. Tamanho menor que 5.")
        elif 5 <= tamanho < 15:
            print("O texto tem tamanho médio. Tamanho menor que 15.")
        elif 15 <= tamanho < 20:
            print("O texto é longo. Tamanho menor que 20.")
        else:
            print("O texto é inválido.")

    elif menu == 5:
        print("\nOpção selecionada: Analisar CPF.")
        cpf = input("Digite o CPF (apenas números, sem espaços ou caracteres especiais): ")

        if cpf.isdigit() and len(cpf) == 11:
            print("CPF válido.")
        else:
            print("CPF inválido.")

    elif menu == 6:
        print("\nOpção selecionada: Contar caracteres.")
        texto = input("Digite um texto: ")
        vogais = sum(texto.lower().count(v) for v in "aeiou")
        espacos = texto.count(" ")
        outros = len(texto) - vogais - espacos

        print(f"Número de vogais é {vogais}")
        print(f"Número de espaços é {espacos}")
        print(f"Número de outros caracteres é {outros}")

    elif menu == 7:
        print("Estamos encerrando o programa. Obrigada!")
        break

    else:
        print("Número digitado não corresponde ao menu. O programa será fechado.")
        break

    repetir = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
    if repetir != "s":

        print("Estamos encerrando o programa. Obrigada!")
        break