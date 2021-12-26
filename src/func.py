from os import system, name, remove
from datetime import date


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
            total["price"] += v["total"]
        
        print()
        for k,v1 in total.items():
            v2 = f'R$ {intToDecimal(v1)}' if k=='price' else v1
            print( f'\033[47;30m {k} \033[42m {v2} \033[m', end=' ')
        print()

    else:
        print( '\n' +'NADA ADICIONADO AINDA'.center(60))
    
    print('\n' +'-'*60)

    try:
        return total
    except:
        return None


def saveDetails(arr, total):
    with open('index.html', 'w') as index:

        index.write('''<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            * { font-family: Arial; padding: 0;
                margin: 0; font-size: .9rem; }
            main { padding: 35px 20px; }
            h1 { font-weight: normal; }
            h1 span { font-size: 1.5rem; }
            table { text-align: left; margin-top: 1.5rem; }
            table, table * { border-collapse: collapse; }
            table tr td, table tr th { padding: 5px 20px; }           
            #final tr th { text-align: center; }
            .head { background-color: #112d79; color: white; }
            .gray { background-color: #eeeeee; }
            .blue { color: #112d79; }
            .bold { font-weight: bold; }
        </style>
    </head>
    <body>
        <main>
        \t''')

        index.write(f'<h1> <span class="bold blue">Planilha registrada em:</span> <span>{date.today()}</span> </h1>')
        index.write('''
            <table id="list">
                <tr class="head">
                    <th> Nome </th>
                    <th> Preço </th>
                    <th> Quantidade </th>
                    <th> Total </th>
                </tr>''')
        
        for k,v in enumerate(arr):
            if k%2==0:
                color = 'normal'
            else:
                color = 'gray'
            
            index.write( f'<tr class="{color}"> <td> {v["name"]} </td> <td> {intToDecimal(v["price"])} </td> <td> {int(v["amount"])} </td> <td> {intToDecimal(v["total"])} </td> </tr>')
        
        index.write( f'''</table>
            <table id="final">
                <tr class="head">
                    <th colspan="2"> Dados finais </th>
                </tr>
                <tr class="normal">
                    <td class="bold blue"> Produtos </td>
                    <td> {total["products"]} </td>
                </tr>
                <tr class="gray">
                    <td class="bold blue"> Itens </td>
                    <td> {total["items"]} </td>
                </tr>
                <tr class="normal">
                    <td class="bold blue"> Preço </td>
                    <td> {intToDecimal( total["price"])} </td>
                </tr>
            </table>
        </main>
    </body>
</html>
        ''')
        

# add Arroz 24,84 3