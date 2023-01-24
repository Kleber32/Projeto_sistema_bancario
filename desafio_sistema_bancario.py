saldo = 0.0
limite_saque = 500.0
saques_diarios = 0
extrato = ''



while True:

    operacao1 = f'''
    ########MENU########
    Saques realizados hoje {saques_diarios}
    Seu saldo é de: R${saldo:.2f}
    1. Sacar
    2. Depositar
    3. Extrato
    0. Sair
    ####################'''

    msg_extrato = f''''''

    operacao = int(input(f'{operacao1}\n''Insira o número da operação que deseja: '))

    if operacao == 1:

        if saques_diarios <=2:
            saque = float(input('Digite a quanto deseja sacar: '))
            if saque >=0:
                if saque <= 500.0:
                    if saque <= saldo:
                        saldo -= saque
                        saques_diarios += 1
                        print(f'Saque de R$ {saque:.2f} realizado.\nSeu novo saldo é de R$ {saldo:.2f}')
                        extrato += f'Saque: R${saque:.2f}\n'
                    else:
                        print('Saldo insuficiente.')
                else:
                    print('O limite por saque é de R$ 500,00')
            else:
                print('Número invalido.')
        else:
            print('Limite diario de saques atingido.')

    elif operacao == 0:
        break

    elif operacao == 2:
        deposito = float(input('Quanto deseja depositar?'))
        if deposito >= 0:
            saldo += deposito
            extrato += f'Deposito: R${deposito:.2f}\n'
        else:
            print('Número invalido.')

    elif operacao == 3:
        print('\n####### Extrato #######')
        print('Não foram realizadas movimentações'if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print('#######################')
    else:
        print('Escolha uma opção valida.')
