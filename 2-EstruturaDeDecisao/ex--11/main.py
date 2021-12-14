l1= float(input('primeiro lado do triangulo: '))
l2= float(input('segundo lado do triangulo : '))
l3= float(input('terceiro lado do triangulo: '))

if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    if l1 == l2 and l1 == l3:
        tipo = 'triangulo Escaleno'
   
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = 'triangulo Isósceles'      
    
    else:
       tipo = 'triangulo Equilátero' 
        
else: 
    tipo = 'não é um triangulo'

print('INFO: ',tipo)
