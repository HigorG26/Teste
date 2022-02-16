from time import sleep

def relogio():
    m = int(input('Digite quantos minutos você deseja regredir: '))
    if m < 60:
        while m > 0:
            s = 60
            m -=1
            while s > 0:
                sleep(1)
                print (f'00:{m:02}:{s:02}')
                s -=1
            m -=1
            continue
    else:
        print ('Valor ultrapassa os minutos permitidos!/n')

