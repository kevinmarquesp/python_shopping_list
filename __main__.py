from func import *


exitCode = 1
helpVar = 0

mainList = list()


def help():
    print('''\033[33m
    > add "NOME" PRECO QUANTIDADE
        O preço será convertido para reais, portanto, não use
        "R$" ou espaços quando escrever.\n
    > edit INDICE new "NOME" PRECO QUANTIDADE
    > remove INDICE\n
    > help
        Use para exibir a ajuda, e "help -hide" para ocultá-la.
    > save
        Use para salvar a lista em um documento "index.html",
        você pode usá-lo no final de qualquer comando.
    > exit
        Para encerrar a execução do programa.
    \033[m''')


def appendToMain(e):
    dictnoray = {
        'name': user[e],
        'price': int(user[e+1]*100),
        'amount': int(user[e+2]),
    }
    dictnoray['total'] = dictnoray['price'] * dictnoray['amount']
    return dictnoray


while exitCode:
    tableWrite(mainList)
    if helpVar: help()

    try:
        user = myInput( '\ninput> ')

        if 'save' in user: pass ###
        if user[0]=='exit':
            break
        
        if user[0]=='add':
            mainList.append(appendToMain(1))
        elif user[0]=='edit':
            mainList[ int(user[1])] = appendToMain(3)
        elif user[0]=='remove':
            del mainList[ int(user[1])]
        
    except:
        helpVar = 1

print()
