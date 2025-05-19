#18) Verificação de Nota - Peça ao usuário para digitar sua nota (0 a 10) e classifique:
Nota ≥ 7: Aprovado
Nota entre 5 e 6.9: Recuperação
Nota < 5: Reprovado

nota=float(input("Qual é a sua nota? de 0 a 10:"))
if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota <= 6.9:
    print("Recuperação")
else:
    print("Reprovado") 
