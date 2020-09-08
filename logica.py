import os
import shutil
from time import sleep

from colorama import Fore


def baner():
    # os.system("echo '''		Term-Cust''' | lolcat")
    print(Fore.RED + '''    Term-Cust''' + Fore.RESET)


def mo():
    print('''
    [A] - About
    [T] - Themes
    [F] - Fonts
    [P] - PS1
    [Q] - Quit''')


def about():
    print('''
    Что-то об авторе и программе
    [select Q to exit to main menu]: ''')


def list_of_slots():
    print('''
    [☆] - list of slots
    ''')
    for array_values in Array_PU:
        numbering = str(Array_PU.index(array_values) + 1)
        print('''    [{}] - {}'''.format(numbering, array_values))


def slots_exist__menu():
    print('''
    [C] - Create Slot
    [R] - Read slot
    [I] - Install slot
    [D] - Delete slot
    [Q] - To exit to the main menu''')


def no_slots__menu():
    print('''
    [!] The list of slots is empty
    [☆] Create a new one

    [C] - Create slot
    [Q] - To exit to main menu''')


def opt_q():
    print('''
    [☆] Have a nice day, bye bye.''')


def incorrect_input():
    print('''
    [!] Incorrect input!
    [☆] Try again..''')


def clear():
    # os.system("clear")
    print("\n" * 100)


def time():
    sleep(1.5)


Dir_T = "C:/Xlebpyshek/Termux/Base/Themes/"
Dir_F = "C:/Xlebpyshek/Termux/Base/Fonts/"
Dir_P = "C:/Xlebpyshek/Termux/Base/PS1/"
Dir_PU = "C:/Xlebpyshek/Termux/Base/PS1/PU/"


while True:
    clear()
    baner()
    mo()
    OPT = input('''
    [Select]: ''')

    if OPT == "A" or OPT == "a":
        while True:
            clear()
            about()
            submenu_A = input()
            if submenu_A == "Q" or submenu_A == "q":
                break
            else:
                incorrect_input()
                time()

    elif OPT == "T" or OPT == "t":
        while True:
            clear()
            Array_T = []
            for a, b, c in os.walk(Dir_T.index(int(1, 10))):
                Array_T.append(b)
            Array_T = Array_T[0]
            print('''
    [☆] - list of slots
                ''')
            for array_values in Array_T:
                numbering = str(Array_T.index(array_values) + 1)
                print('''    [{}] - {}'''.format(numbering, array_values))
            input()

    elif OPT == "F" or OPT == "f":
        print("в разработке")
    elif OPT == "P" or OPT == "p":
        while True:
            clear()
            Array_PU = []
            for a, b, c in os.walk(Dir_PU):
                Array_PU.append(b)
            Array_PU = Array_PU[0]

            if len(Array_PU) == 0:
                no_slots__menu()
                sub_submenu_U_i = input("\n    Select: ")
                if sub_submenu_U_i == "C" or sub_submenu_U_i == "c":
                    clear()
                    new_slot_name_i = input("\n    [☆] Enter a name for the new slot: ")
                    try:
                        os.mkdir(Dir_PU + new_slot_name_i)
                        # создание файла .bashrc
                    except OSError:
                        clear()
                        print('''    [!] Slot "{}" not created\n    [☆] Try again..'''.format(new_slot_name_i))
                        time()
                        continue
                    else:
                        clear()
                        print('''    [☆] Slot "{}" created successfully\n    [☆] Edit it..'''.format(new_slot_name_i))
                        time()
                elif sub_submenu_U_i == "Q" or sub_submenu_U_i == "q":
                    break
                else:
                    incorrect_input()
                    time()

            else:
                slots_exist__menu()
                sub_submenu_U_i = input("\n    Select: ")
                if sub_submenu_U_i == "C" or sub_submenu_U_i == "c":
                    while True:
                        clear()
                        list_of_slots()
                        new_slot_name_i = input("\n    [☆] Enter a name for the new slot: ")
                        try:
                            os.mkdir(Dir_PU + new_slot_name_i)
                            # создание файла .bashrc
                        except OSError:
                            clear()
                            if os.path.exists(Dir_PU + new_slot_name_i):
                                clear()
                                print(
                                    '''    [!] Slot "{}" already exists\n    [☆] Try again..'''.format(new_slot_name_i))
                                time()
                                continue
                            else:
                                clear()
                                print('''    [!] Slot "{}" not created\n    [☆] Try again..'''.format(new_slot_name_i))
                                time()
                                continue
                        else:
                            clear()
                            print(
                                '''    [☆] Slot "{}" created successfully\n    [☆] Edit it..'''.format(new_slot_name_i))
                            time()

                elif sub_submenu_U_i == "R" or sub_submenu_U_i == "r":
                    while True:
                        print("r")
                        time()

                elif sub_submenu_U_i == "I" or sub_submenu_U_i == "i":
                    while True:
                        print("i")
                        time()

                elif sub_submenu_U_i == "D" or sub_submenu_U_i == "d":
                    while True:
                        clear()
                        list_of_slots()
                        slot_number = input('''\n    [☆] Enter slot number: ''')
                        if slot_number in [str(i + 1) for i in range(len(Array_PU))]:
                            clear()
                            print('''    [!] Slot "{}" will be deleted\n    [☆] Are you sure? Y/n - Yes/No'''.format(
                                Array_PU[int(slot_number) - 1]))
                            the_confirmation = input('''\n    [!] Confirm: ''')
                            if the_confirmation == "Y" or the_confirmation == "y":
                                try:
                                    if slot_number in [str(i + 1) for i in range(len(Array_PU))]:
                                        shutil.rmtree(Dir_PU + Array_PU[int(slot_number) - 1])
                                except OSError:
                                    clear()
                                    print('''    [!] Slot "{}" not deleted'''.format(Array_PU[int(slot_number) - 1]))
                                    time()
                                    break
                                else:
                                    clear()
                                    print('''    [☆] Slot "{}" successfully deleted'''.format(
                                        Array_PU[int(slot_number) - 1]))
                                    time()
                                    break
                            elif the_confirmation == "N" or the_confirmation == "n":
                                continue
                            else:
                                clear()
                                incorrect_input()
                                time()
                                continue
                        else:
                            clear()
                            incorrect_input()
                            time()

                elif sub_submenu_U_i == "Q" or sub_submenu_U_i == "q":
                    break

                else:
                    clear()
                    incorrect_input()
                    time()
                    continue

    elif OPT == "Q" or OPT == "q":
        opt_q()
        time()
        clear()
        break
    else:
        incorrect_input()
        time()
