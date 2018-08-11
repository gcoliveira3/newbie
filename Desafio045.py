# Crie um programa que jogue paper, scissors, rock, lizzard, spock

import random
import time

print('-='*30)
print('LETS PLAY! ROCK - PAPER - SCISSORS - LIZZARD - SPOCK!')
print('-='*30)
print('')

p1 = str(input('Vamos jogar! Digite sua escolha:'))
p1 = p1.strip().lower()

if p1 == 'paper' or p1 == 'scissors' or p1 == 'rock' or p1 == 'lizzard' or p1 == 'spock':
    time.sleep(1)
    print('Minha vez de jogar!')

    time.sleep(2)
    lista = ['paper', 'scissors', 'rock', 'lizzard', 'spock']
    p2 = random.choice(lista)
    print('')
    print('<==>'*10)
    print('Você escolheu {}!\nEu escolhi {}!'.format(p1.upper(), p2.upper()))
    print('<==>' * 10)
    print('')

    time.sleep(2)

    if p1 == p2:
        print('TEMOS UM EMPATE SENHORES!')

    elif (p1 == 'paper' and (p2 == 'rock' or p2 == 'spock')) or (p1 == 'scissors' and
         (p2 == 'paper' or p2 == 'lizzard')) or p1 == 'rock' and (p2 == 'scissors' or p2 == 'lizzard') or \
         p1 == 'lizzard' and (p2 == 'spock' or p2 == 'paper') or p1 == 'spock' and (p2 == 'scissors' or p2 == 'paper'):
        print('{} ganha de {}!'.format(p1.upper(), p2.upper()))
        time.sleep(2)
        print('')
        print('****PARABÉNS, VOCÊ VENCEU!****')

    else:
        print('{} perde para {}!'.format(p2.upper(), p1.upper()))
        time.sleep(2)
        print('')
        print('****VOCÊ PERDEU!****')
        print('')
        print('         \033[4;31mGAME OVER\033[m')

else:
    print('Você não sabe jogar isso? Essa opção não existe!')
