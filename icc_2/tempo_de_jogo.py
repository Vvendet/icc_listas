tudo = input().split()

tempo_inicial = tudo[:2]
tempo_final = tudo[2::]


tempo =  ((int(tempo_final[0]) - int(tempo_inicial[0]))**2  + (int(tempo_final[1]) - int(tempo_inicial[1]))**2)**0.5
if tempo <= 1:
    tempo = 1440 - tempo
    print(f'O jogo durou {int(tempo//60)} hora(s) e {int(tempo%60)} minuto(s).')
else:
    tempo = 1440 + tempo 
    print(f'O jogo durou {int(24 - tempo//60)} hora(s) e {int(60 - int(tempo%60))} minuto(s).')