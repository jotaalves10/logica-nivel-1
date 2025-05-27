#21) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

n1=int(input("digite um numero:"))
n2=int(input("digite outro numero:"))
n3=int(input("digite mais um numero:"))
if n1 < n2 and n2 < n3:
    print(n1,n2,n3)
elif n1 < n3 and n3 < n2:
    print(n1,n3,n2)
elif n2 < n1 and n1 < n3:
    print(n2,n1,n3)
elif n2 < n3 and n3 < n1:
    print(n2,n3,n1)
elif n3 < n2 and n2 < n1:
    print(n3,n2,n1)
elif n3 < n1 and n1 < n2:
    print(n3,n1,n2)
else:
    print("os valores são iguais")
