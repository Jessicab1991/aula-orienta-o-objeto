from conta import Conta
v = "*"*20

def menu():
    menu = 1

    while menu != 2:
        
        var=int(input('''\ndigite:\n1-para criar conta 1\n2-para extrato conta 1
3-para saque conta 1\n4-para deposito conta 1\n5-para criar conta 2\n6-para extrato conta 2
7-para saque conta 2\n8-para deposito conta 2\n9-para transferencia conta 1 para conta 2
10-para transferencia conta 2 para conta 1\n>>'''))
        
        match var:
            case 1:
                print(v,"menu conta 1", v)
                conta1=Conta(input("digite o seu nome>>"),
                             int(input("digite o numero da conta>>")),
                             float(input("digite o saldo da sua conta >>")),
                             float(input("digite o limite da sua conta >>")))

            case 2 :
                print(v,"extrato conta 1", v)  
                conta1.extrato()

            case 3 :
                conta1.sacar(float(input("digite o valor do saque>>")))   
                print(v,"extrato saque conta 1", v)
                conta1.extrato()
            
            case 4 :
                conta1.depositar(float(input("digite o valor do deposito>>")))
                print(v,"extrato deposito conta 1", v)
                conta1.extrato()

            case 5 :
                print(v,"menu conta 2", v)
                conta2=Conta(input("digite o seu nome>>"),
                             int(input("digite o numero da conta>>")),
                             float(input("digite o saldo da sua conta >>")),
                             float(input("digite o limite da sua conta >>"))) 
                
            case 6:
                print(v,"extrato conta 2", v)  
                conta2.extrato()

            case 7 :
                conta2.sacar(float(input("digite o valor do saque>>")))   
                print(v,"extrato saque conta 2", v)
                conta2.extrato()  

            case 8 :
                conta2.depositar(float(input("digite o valor do deposito>>")))
                print(v,"extrato deposito conta 2", v)
                conta2.extrato()

            case 9 :
                print(v,"extrato transferencia ", v)  
                conta2.transferir(float(input("digite o valor da transferencia>>")),conta1,conta2)
                print(v,"extrato trasnferencia conta 2 ", v)
                conta2.extrato()

                print(v,"extrato trasnferencia conta 1 ", v)
                conta1.extrato()

            case 10 :
                print(v,"extrato transferencia ", v)  
                conta1.transferir(float(input("digite o valor da transferencia>>")),conta2,conta1)
                print(v,"extrato trasnferencia conta 1 ", v)
                conta1.extrato()

                print(v,"extrato trasnferencia conta 2 ", v)
                conta2.extrato()  

        menu = int(input("gostaria de realizar uma nova operação?\ndigite:\n1-sim\n2-não\n >>"))

menu()