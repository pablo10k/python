import random


def run():
    """
    0: piedra
    1: papel
    2: tijera
    """
    player = 0
    bot = 0
    play = True
    ans = 0
    while play:
        player_election = int(input('0: piedra, 1: papel, 2: tijeras '))
        bot_election = random.randint(0, 2)
        print(player_election)
        print(bot_election)
        if player_election == 0 and bot_election == 1:
            print('Human: Piedra')
            print('Bot: Papel')
            print('Bot wins!')
            bot += 1
        elif player_election == 1and bot_election == 0:
            print('Human: Papel')
            print('Bot: Piedra')
            print('Human wins')
            player += 1
        elif player_election == 0and bot_election == 2:
            print('Human: Piedra')
            print('Bot: Tijeras')
            print('Human wins')
            player += 1
        elif player_election == 2and bot_election == 0:
            print('Human: Tijeras')
            print('Bot: Piedra')
            print('Bot wins')
            bot += 1
        elif player_election == 1and bot_election == 2:
            print('Human: Papel')
            print('Bot: Tijeras')
            print('Bot wins')
            bot += 1
        elif player_election == 2and bot_election == 1:
            print('Human: Tijeras')
            print('Bot: Papel')
            print('Human wins')
            player += 1
        else:
            print("Empate")


        print('------ Score -----')
        print('Human player: {}'.format(player))
        print('Bot player: {}'.format(bot))
        ans = input('Presione 1 para volver a jugar o cualquier otra tecla para salir ')
        if ans != "1":
            play = False


if __name__ == '__main__':
    run()
