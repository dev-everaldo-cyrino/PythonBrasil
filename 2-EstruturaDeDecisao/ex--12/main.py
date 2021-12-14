while True:
    print('-----calculadora de equação do segundo gral-----')
    a = int(input('valor de A: '))
    if a == 0:
        print('valor de A não pode ser nulo')
        break 
    b = int(input('valor de B: '))
    c = int(input('valor de C: '))

    raiz = (b * b) - (4 * a * c)
    p2 = 0
    p3 = 0
    p5 = 0
    p7 = 0
    n1= []
    total = 1
    if raiz == 0:
        print('raiz igual a 0, apenas uma solução')
        x1 = ((-1 * b) - raiz) / (2*a)
        print('o x1 = {}'.format(x1))
        break
    elif raiz < 0:
        print('raiz negativa, sem solução')
        break
    else:
        while raiz > 1:
            if raiz % 2 == 0:
                raiz /= 2
                p2 +=1
                if p2 == 2:
                    p2= 0
                    n1.append(2)
                    
            elif raiz % 3 == 0:
                raiz /=3
                p3 +=1
                if p3 == 2:
                    p3= 0
                    n1.append(3)
                    
            elif raiz % 5 == 0:
                raiz /=5
                p5 +=1
                if p5 == 2:
                    p5= 0
                    n1.append(5)
            elif raiz % 7 == 0:
                raiz /=7
                p7 +=1
                if p7 == 2:
                    p7= 0
                    n1.append(7)
            else:
                break

        if p2 == 1 or p3 ==1 or p5 ==1 or p7 ==1:
            print('esta raiz não é interia ')
        else:
            for x in range(len(n1)):
                total *= n1[x]
            x1 = ((-1 * b) + total) / (2*a)
            x2 = ((-1 * b) - total) / (2*a)
            print('o x1 = {}'.format(x1))
            print('o x2 = {}'.format(x2))