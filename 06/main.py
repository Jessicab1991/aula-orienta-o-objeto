from conta import Conta

conta = Conta(input("digite seu nome>>"),
#atributo a conta
int(input("digite o numero da sua conta>>")),
#atributo saldo conta
float(input("digite seu saldo inicial:>>")),
#atributo limite conta
float(input("digite o limite da sua conta:>>")))       
            
print(conta)

conta.set_numero(int(input("digite o novo numero >> ")))
conta.set_saldo(float(input("digite o novo saldo >> ")))
conta.set_titular(input("digite o novo nome >> "))
conta.set_limite(float(input("digite o novo limite>> ")))
                

print("o numero da conta agora é {}".format(conta.get_numero()))
print("o numero do saldo agora é {}".format(conta.get_saldo()))
print("o nome digitado agora é {}".format(conta.get_titular()))
print("o novo limite é {}".format(conta.get_limite()))

