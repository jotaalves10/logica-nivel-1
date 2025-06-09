#24) Pedir senha até que seja digitada a correta

senha_usuario=123
senha = int(input("digite a senha:"))
while senha != senha_usuario:
     print("Senha incorreta.")
     senha = int(input("digite a senha novamente: "))
print("Senha correta.")
