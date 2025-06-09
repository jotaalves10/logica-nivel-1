#25) Somar números positivos digitados pelo usuário até que ele digite um número negativo

soma = 0
while True:
    num=int(input("Digite um numero(digite um número negativo pra sair):"))
    if num < 0:
        break
    soma += num
print(f"a soma dos números positivos é igual a: {soma}")
