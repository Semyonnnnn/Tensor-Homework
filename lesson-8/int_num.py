def int_number():
    while True:
        a = input('Введите целое число:\n')
        try: 
            a = int(a)
            break
        except:
            print('Число не целое')
    return a
