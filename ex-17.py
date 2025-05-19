#17) Classificação de Idade - Peça ao usuário sua idade e classifique da seguinte forma:
Menor de 12 anos: Criança
Entre 12 e 17 anos: Adolescente
Entre 18 e 59 anos: Adulto
60 anos ou mais: Idoso

idade=int(input("Qual é a sua idade?"))
if idade < 12:
    print("Você é criança")
elif idade >= 12 and idade <= 17:
    print("Você é adolescente")
elif idade >= 18 and idade <= 59:
    print("Você é adulto")
else:  
    print("Você é idoso") 
