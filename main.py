import os
import time
from click import pause

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

    valid = True
    while valid:
        color = input('> ')

        if color not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
            print("--> Invalid color value, try again!")
        else:
            valid = False

    os.system(f'color {color}')

# ===================================================================================

def pyshell():
    print('''
============================
Welcome to PyShell
============================
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

def main():  # sourcery skip: extract-duplicate-method, extract-method, hoist-statement-from-if, switch
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

            if "exit" in action:
                os.system('cls')
                quit()
            
            if "version" in action:
                print("\n--> PyShell v0.1 alpha <--\n")

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
                os.system('cls')
                os.system('color c')
                print("=== Py Shell Updater ===\n")
                confirmations = input("Do you want to update PyShell? (y/n) > ")
                if confirmations in ["y", "yes", "yeah"]:
                    if os.path.isdir('pyshell-py'):
                        os.system('cls')
                        print("\n--> Please remove old version before updating!")
                        valid = False
                        pause("\nPress any key to go back...")
                        os.system('cls')
                        os.system('color f')
                        main()

                    else:
                        print("\nUpdating PyShell...\n")
                        os.system('git clone https://github.com/ItWorksOnLocal-png/pyshell-py.git')
                        print("\n***THE UPDATED VERSION HAS BEEN DOWNLOADED IN A NEW DIRECTORY NAMED 'pyshell-py'***")
                        pause("\nPress any key to go back...")
                        os.system('cls')
                        os.system('color f')
                        main()

                else:
                    print("\nExiting the updater...")
                    time.sleep(1)
                    os.system('cls')
                    os.system('color f')
                    main()


        except ValueError:
            valid = True

# ===================================================================================

if __name__ == "__main__":
    main()