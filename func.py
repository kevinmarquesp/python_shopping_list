from os import system, name


def intToDecimal(n):
    return  f'R$ {n/100}'.replace( '.', ',')


def tableWrite( array=list(), total=dict()):
    system( 'clear' if name!='nt' else 'cls')

    if len(array)==0:
        print()
    else:
        print( '\n\033[32m Nada adicionado ainda... \033[m\n'.center(50))
    print('-'*50)


def myInput(msg):
    user = input(msg)
    result = list()

    # Este trecho remove os espaços da string e substituí por "_", altere isso depois...
    if '"' in user:
        string = user[
            user.find('"')+1:
            user.rfind('"')
        ]
        user = user.replace( f'"{string}"', string.replace(' ', '_'))
    
    for i in user.split():
        j = i

        if '_' in j:
            j = j.replace( '_', ' ')
        elif ',' in j:
            j = j.replace( ',', '.')

        try:
            result.append(float(j))
        except:
            result.append(j)

    return result


def tableWrite(arr):
    system('clear')

    if len(arr):
        print( '\n' +'\033[32mLISTA DE COMPRAS\033[m'.center(68) +'\n')

        print(
            '\033[4m'+
            'IN.',
            f'{"Nome":<30}',
            f'{"Preço":<10}',
            'Qt.',
            f'{"Total":<10}'
            +'\033[m'
        )

        total = {
            'products': len(arr),
            'items': 0,
            'price': 0
        }
        for k,v in enumerate(arr):
            print(
                f'{k:^3}',
                f'{v["name"]:<30}',
                f'{intToDecimal(v["price"]):<10}',
                f'{int(v["amount"]):<3}',
                '\033[32m' +intToDecimal(v["total"]) +'\033[m'
            )

            total["items"] += int(v["amount"])
            total["price"] += v["price"]
        
        print()
        for k,v1 in total.items():
            v2 = f'R$ {intToDecimal(v1)}' if k=='price' else v1
            print( f'\033[47;30m {k} \033[42m {v2} \033[m', end=' ')
        print()

    else:
        print( '\n' +'NADA ADICIONADO AINDA'.center(60))
    
    print('\n' +'-'*60)

#add Arroz 24,84 3