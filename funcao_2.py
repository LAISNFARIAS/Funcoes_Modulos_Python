def soma(n1,n2):
    return n1 + n2

def produto(n1,n2):
    return n1 * n2

def restoDivisao(n1,n2):
    return n1 % n2

def separarResultados(texto):
    print("--------------------------O resultado de "+texto+"-----------------------")

print("Olá, seja bem-vindo ao programa de cálculos!")
separarResultados("soma")
print("O resultado da soma entre os números 5 e 10 é "+str(soma(5,10)))

separarResultados("multiplicação")
print("O resultado da multiplicação entre os números 5 e 10 é "+str(produto(5,10)))

separarResultados("resto da divisão")
print("O resto da divisão entre os números 5 e 10 é "+str(restoDivisao(5,10)))