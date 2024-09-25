def menu(options):
    while True:
        user_choice = input(f'Enter your choice {options}: ').strip()
        if user_choice in options:
            return user_choice
        print(f'Invalid option {user_choice}; try again')

def greet(name):
    return f'Hello, {name}!'