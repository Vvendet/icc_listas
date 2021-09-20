"""
Seu sobrinho Joberto está aprendendo a escrever e está tendo 
dificuldade de lembrar que deve usar letra maiúscula no início da frase.

Como um bom tio que é, e um exímio 
programador, você decide que a melhor 
abordagem é escrever um programa que faça as correções automaticamente."""

texto = input().split('.')
texto = [list(texto[0]),list(texto[1])]
formated_text = []
for i in range(0,len(texto)):
    for j in texto[i]:
        if (j != ''):
            print(j)
            formated_text.append(j.upper())
            texto[i].remove(j)
            break
        else:
            formated_text.append(j)
            texto[i].remove(j)
