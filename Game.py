def start_game():
    print("You are in a dark forest. Do you want to go 'left' or 'right'?")
    choice = input("> ").lower()
    if choice == 'left':
        print("You encounter a friendly wizard. He offers you a potion.")
    elif choice == 'right':
        print("You find a treasure chest filled with gold!")
    else:
        print("Invalid choice. Try again.")

start_game()
