while True:
    user = input('usuario: ')
    senha = input('senha: ')
    if user != senha:
        print('usuario e senha cadastrados')
        break
    else:
        print('usuario e senha iguais, reescreva uma senha mais forte')
    