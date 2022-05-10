import os

# ===================================================================================

def terminal_color():
    print('''
Choose a color for your terminal:

0 = Black       8 = Gray
1 = Blue        9 = Light Blue
2 = Green       A = Light Green
3 = Aqua        B = Light Aqua
4 = Red         C = Light Red
5 = Purple      D = Light Purple
6 = Yellow      E = Light Yellow
7 = White       F = Bright White
    ''')

    color = input('> ')

    os.system(f'color {color}')

# ===================================================================================

def pyshell():
    print('''
===================
Welcome to PyShell
===================
    ''')

    valid = True
    while valid:
        commands = input("pyshell> ")
        if "exit" in commands:
            quit()
        
        if "menu" in commands:
            os.system('cls')
            main()

        os.system(f"{commands}")

# ===================================================================================

def main():
    print('''
===================================================
Welcome to the Python terminal emulator (PyShell)
===================================================''')

    print('''
[·] Change the terminal color
[·] Start a shell session
[·] Update PyShell
''')

    valid = True

    while valid:
        try:
            action = input("Choose and action (1-3) > ")
            action = int(action)

            if action == 1:
                os.system('cls')
                terminal_color()
                os.system('cls')
                main()
            elif action == 2:
                os.system('cls')
                pyshell()

            elif action == 3:
                os.system('git clone ')

        except ValueError:
            print("\nInvalid input! Please try again")
            valid = False

# ===================================================================================

if __name__ == "__main__":
    main()