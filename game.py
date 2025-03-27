#import logo and game data
#randomly generate first 2 selection
#compare if b's followers count > a's
#if guess is correct b becomes a
#if wrong exit
import random

from logo import logo
print(logo)
from game_data import data



#new account creation
def create_new_acc(exclude_acc):
    while True:
        new_acc = random.choice(data)
        if new_acc != exclude_acc:
            return new_acc


#compare followers
def compare_foll_higher(A_foll , B_foll, score):
    if B_foll > A_foll:
        print("You're right!")
        return score + 1

    else:
        print("Your guess is wrong!")
        print(f"your score is {score}")
        return - 1


def compare_foll_lower(A_foll , B_foll, score):
    if B_foll < A_foll:
        print("You're right! guess next")
        return score + 1

    else:
        print("Your guess is wrong!")
        print(f"your score is {score}")
        return - 1


def display_data(Account):
    acc_name = Account["name"]
    acc_description = Account["description"]
    acc_country = Account["country"]
    print(f"{acc_name} , a {acc_description} from {acc_country}")


#main
def game():
    print("Welcome!")
    #random generation
    Acc_A = random.choice(data)
    Acc_B = random.choice(data)

    display_data(Acc_A)
    display_data(Acc_B)
    score = 0

    while True :
        foll_A = Acc_A['follower_count']
        foll_B = Acc_B['follower_count']
        nameA = Acc_A["name"]
        nameB = Acc_B["name"]
        guess = input(f"select whether {nameB} has higher or lower followers than {nameA} (h/l) :")
        if guess == 'h':
            result = compare_foll_higher(foll_A , foll_B , score)
        elif guess == 'l':
            result = compare_foll_lower(foll_A, foll_B , score)

        if result == -1:
            print(f"You guessed it wrong! game over")
            break
        else:
             score = result
             Acc_A = Acc_B
             Acc_B = create_new_acc(Acc_A)
             print(f"Your score is {score}...Guess next")


game()

