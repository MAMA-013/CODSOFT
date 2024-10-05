import random




while True:
    user1=input("Enter you name:-")
    print(f"Hi {user1}, Welcome to Rock Paper Scissor game!! \n" "Winning Rules of this game:- \n" "Rock v/s Scissor -->Rock wins \n" "Rock v/s Paper --> Paper wins \n" "Scissor v/s Paper--> Scissor wins" )

    print("Enter your choice \n 1 :- Rock \n 2 :- Paper \n 3 :- Scissors \n")

    
    choice = int(input("Enter your choice: "))

    
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺: '))

    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    
    computer_choice = random.randint(1, 3)

    
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissors'

    print("Computer choice is:", computer_choice_name)
    print(choice_name, 'vs', computer_choice_name)

    
    if choice == computer_choice:
        result = "DRAW"
    elif (choice == 1 and computer_choice == 2) or (computer_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and computer_choice == 3) or (computer_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and computer_choice == 3) or (computer_choice == 2 and choice == 3):
        result = 'Scissors'

    
    if result == "DRAW":
        print("<-- It's a tie!!--> ")
    elif result == choice_name:
        print("<-- User wins! -->")
    else:
        print("<-- Computer wins! -->")
    print("Thanks for playing!!")
    print("Do you want to play again? (Y/N)")
    rps = input().lower()
    if rps == 'n':
        break


    
    