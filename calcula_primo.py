num = int(input("Informe um numero: "))
i = 0 
aux = True

if (num!=2):
    i = num//2
    while i > 1:
        if num%i == 0:
            aux = False
            print('O número {} não é primo.'.format(num))
            break
        else :
            i = i - 1       
elif num == 2:
    print('O número {} não é primo.'.format(num))

if aux == True:
    print('O número {} é primo.'.format(num))
