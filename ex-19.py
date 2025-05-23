#19) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

num1=int(input("digite um numero:"))
num2=int(input("digite outro numero:"))
num3=int(input("digite mais um numero:"))
if num1 < num3 and num2 < num3:
    print(num3,"e o maior")
elif num1 < num2 and num3 < num2:
    print(num2,"e o maior")
elif num3 < num1 and num2 < num1:
    print(num1,"e o maior")
