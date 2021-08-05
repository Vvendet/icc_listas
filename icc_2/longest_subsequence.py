"""Uma subsequência de uma string é uma sequência de caracteres que aparece na mesma ordem da string. As ocorrências não precisam ser consecutivas, por exemplo, "ac", "bc", "abc" e "a" são subsequências da string "abc", enquanto as strings "abbc" e "acb" não são. A string vazia é subsequência de qualquer string. Qualquer string é subsequência dela mesmo.

A maior subsequência incomum entre duas strings é a maior string que é subsequência de uma das duas e não é subsequência da outra. 

Dada duas strings x e y, encontre o tamanho da maior subsequência incomum. """

x = input()
y = input()
maior = -1
if len(y) > len(x):
    for i in range(0,len(x)+1):
        if y[::i] != x[::i]:
            if len(y[::i]) > len(x[::i]):
                maior = len(y[::i])
            else:
                maior = len(x[::i])
    if y[::-1] != x[::-1] and len(y[::-1]) > len(x[::-1]):
        maior = len(y[::-1])
    elif y[::-1] != x[::-1] and len(y[::-1]) < len(x[::-1]):
        maior = len(x[::-1])