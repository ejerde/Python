"""
Python Fundamentals
Portfolio project
By Eric Jerde
rev 1.2
10/23/2023
"""
import random

import sys

from rps_pkg.user import register

from rps_pkg.homepage import show_homepage

"""import statements"""

database = {"admin" : "password"}

authorized_user = ""

while True:
    show_homepage(authorized_user)   
    choice = input("Choose an option:") #menu selection
    if choice == "1":
        username = input("\nEnter username:")
        password = input("Enter password:")
        authorized_user = register(database, username,password)
        continue
    elif choice == "2":
        print("Game beginning...")
        break
    else:
        print("\nLeaving RPS..")
        sys.exit()
"""visual layout of game/user"""

Moves = {
        ('r', 's'): (0, 'Computer smashes scissors with a rock. You are Reckd!\n'),
        ('r', 'p'): (1, 'Player uses paper to cover the rock. Victory is yours!\n'),
        ('p', 's'): (1, 'Player cuts up the paper with scissors. Emotional Damage!\n'),
        ('p', 'r'): (0, 'Computer covers the rock with paper. You lose! How did that feel?\n'),
        ('s', 'p'): (0, 'Computer cuts up the paper with scissors. Thats got to hurt!\n'),
        ('s', 'r'): (1, 'Player smashes scissors with a rock. Hulk Smash!\n'),
    }
"""dictionary of move options and results"""

def computer_move():
    return random.choice(['r', 'p', 's'])
"""computer move options"""

def user_move():
    try: 
        while True:
            ask = input('Enter a choice (rock, paper, scissors,(c)current scores:').lower()
            if ask and ask[0] in 'rpsc':
                return ask[0]
            else:
                print("Try again with listed choice to play!\n")
    except ValueError:
        sys.exit()
"""user move random options""" 

def display_scores(games, wins, draws):
    print(f'Played {games} ({wins} wins, {games - wins - draws} defeats, {draws} draws).')
"""Display game scoring"""

def play():
    games = 0
    wins = 0
    draws = 0

    while True:
        computer = computer_move()
        user = user_move()
        if user == 'c':
            display_scores(games, wins, draws)
            continue 
        games += 1
        if computer == user:
            print('Computer and player made the same move!')
            draws += 1
        else:
            score, msg = Moves.get((computer, user)) #used msg instead of creating multiline strings
            print(msg)
            wins += score

            play_again = input("Play again? (y/n): ")
            if play_again.lower() == "n":
                print("Now leaving RPS")
                break      
play()