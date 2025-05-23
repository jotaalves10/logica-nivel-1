#20) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.


num1=int(input("digite um numero:"))
num2=int(input("digite outro numero:"))
num3=int(input("digite mais um numero:"))
if num1 < num3 and num1 < num2:
    print(num3,"e",num2,"são os maiores")
elif num3 < num1 and num3 < num2:
    print(num1,"e",num2,"são os maiores")
elif num2 < num1 and num2 < num3:
    print(num1,"e",num3,"são os maiores")
