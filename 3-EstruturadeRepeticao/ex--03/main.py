while True:
    nome = input('Nome: maior que 3 caracteres; ')
    if len(nome) > 3:
        idade = int(input('Idade: entre 0 e 150; '))
        if idade > 0 and idade < 150:
            salario = float(input('Salário: maior que zero; '))
            if salario > 0:
                sexo = input("Sexo: 'f' ou 'm'; ")
                if sexo in ['f','m']:
                    civil = input("Estado Civil: 's', 'c', 'v', 'd'; ")
                    if civil in ['s','c','v','d']:
                        print('-------cadastro feito com sucesso-------')
                        print('''
                        Nome: {} ;
                        Idade: {} ;
                        Salário: {} ;
                        Sexo: {} ;
                        Estado Civil: {} ;
                        '''.format(nome,idade,salario,sexo,civil))
                        break
    print('informação errada !')