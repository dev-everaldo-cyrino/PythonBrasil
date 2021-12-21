print('coloque valores, -1 encerra o programa.')
n1 = {"200 - 299: ":0 ,"300 - 399: ":0 ,"400 - 499: ":0 ,"500 - 599: ":0 ,"600 - 699: ":0 
        ,"700 - 799: ":0 ,"800 - 899: ":0,"900 - 999: ":0 ,"1000 em diante":0}
while True:
    num = float(input('diga seu salario: '))
    if num == -1:
        print('---------------------')
        for x,y in n1.items():
            print(x, y)
        break
    num *= 0.09
    num +=200
    print('comissão: R${:.2f}'.format(num))
    n = {"200 - 299: ":num >= 200 and num <=299, "300 - 399: ":num >= 300 and num <=399, "400 - 499: ":num >= 400 and num <=499
        , "500 - 599: ":num >= 500 and num <=599, "600 - 699: ":num >= 600 and num <=699, "700 - 799: ":num >= 700 and num <=799
        , "800 - 899: ":num >= 800 and num <=899, "900 - 999: ":num >= 900 and num <=999, "1000 em diante":num >= 1000}
    for x,y in n.items():
        if y == True:
            n1[x] +=1
