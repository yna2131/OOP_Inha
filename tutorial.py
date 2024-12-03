import time
import os

def tutorial():
    os.system("cls")
    print("""
          
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠀⠀⠀⠀⠀⠀⠀⠐⠂⠤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢄⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
    ⠀⡀⠀⠀⠀⠀⢀⡴⠁⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
    ⠀⢰⠀⠀⠀⢠⠎⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀
    ⠀⠸⡀⠀⣠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⡇⠀
    ⠀⠀⡇⢠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⡿⠿⠛⠛⡟⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⠃⠀
    ⠀⠀⢃⡏⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⡀⠀⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⣇⠀⠀⠀⠀⡇⠀⠀⠀⠀⣰⡆⠀⠙⢿⣿⣿⣿⠿⣿⣿⣿⣿⣇⠀⠀⠀⡇⠀⠀
    ⠀⠀⢸⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢠⣿⡯⣆⠀⠀⠀⡇⠉⠀⠀⢰⣿⢹⡄⠀⠘⢿⣿⣧⣵⣼⣿⣿⣿⣿⠀⠀⠀⢃⠀⠀
    ⠀⠀⢸⠀⠀⠀⣿⣿⣟⣿⣿⣿⣿⣿⣏⠀⠀⢸⣿⡇⢸⠀⢀⣤⣷⣄⠀⠀⢸⣿⠀⡇⣀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿⡇⣸⣶⡟⡿⣿⢢⠙⠲⠾⣿⡀⡇⠋⠐⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡌⠀⠀
    ⢸⡄⠸⠀⠀⠀⠸⣿⡿⠋⠉⠙⢿⣿⣇⣠⣤⢼⡋⢃⡴⠋⣰⠁⢿⠈⣆⠀⠀⠀⠉⠳⠤⣀⣸⣿⡿⢛⡏⠉⠻⣿⡇⠀⠀⠀⡇⢀⡇
    ⢸⣿⡄⣇⠀⠀⠀⢻⡁⠀⣀⡤⠞⡫⠛⢑⠖⡭⠂⠉⠀⠀⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⢄⡀⠀⡿⠁⠀⠀⢰⢁⣾⡇
    ⢸⣿⣿⣼⡄⠀⠀⠀⢣⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣶⣶⣶⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠿⣳⠁⠀⠀⠀⣎⣾⣿⡇
    ⢸⣿⣿⣿⣷⡀⠀⠀⠀⠳⡀⠀⠀⠈⠉⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⢯⡉⠁⠀⢀⡜⠁⠀⠀⠀⣼⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣷⣄⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢢⡤⠋⠀⠀⠀⢀⣾⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⡷⣄⠀⠀⠀⠙⠢⣀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⠀⢀⢴⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣮⡳⣄⠀⠀⠀⠈⠑⠢⢄⣀⠀⠀⠀⣿⣿⣿⡇⢠⠃⠀⠀⣀⡠⠔⠊⠁⠀⠀⠀⣀⠔⣹⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡑⠦⣀⠀⠀⠀⠀⠈⠉⠑⠒⢻⣿⣿⡇⡾⠒⠚⠉⠁⠀⠀⠀⠀⢀⡤⠚⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠑⠦⢄⡀⠀⠀⠀⠀⠈⢿⣿⣿⠃⠀⠀⠀⠀⠀⣀⠤⠚⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠈⠑⠒⠤⠤⣀⣀⣛⣁⣀⡤⠤⠐⠚⠉⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
    ⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠲⢤⣀⡠⠔⠚⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀
    Welcome to Galactic Vendetta
    """)
    time.sleep(2)
    os.system("cls")
    print("""
          
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠀⠀⠀⠀⠀⠀⠀⠐⠂⠤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢄⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
    ⠀⡀⠀⠀⠀⠀⢀⡴⠁⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
    ⠀⢰⠀⠀⠀⢠⠎⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀
    ⠀⠸⡀⠀⣠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⡇⠀
    ⠀⠀⡇⢠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⡿⠿⠛⠛⡟⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⠃⠀
    ⠀⠀⢃⡏⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⡀⠀⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⣇⠀⠀⠀⠀⡇⠀⠀⠀⠀⣰⡆⠀⠙⢿⣿⣿⣿⠿⣿⣿⣿⣿⣇⠀⠀⠀⡇⠀⠀
    ⠀⠀⢸⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢠⣿⡯⣆⠀⠀⠀⡇⠉⠀⠀⢰⣿⢹⡄⠀⠘⢿⣿⣧⣵⣼⣿⣿⣿⣿⠀⠀⠀⢃⠀⠀
    ⠀⠀⢸⠀⠀⠀⣿⣿⣟⣿⣿⣿⣿⣿⣏⠀⠀⢸⣿⡇⢸⠀⢀⣤⣷⣄⠀⠀⢸⣿⠀⡇⣀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿⡇⣸⣶⡟⡿⣿⢢⠙⠲⠾⣿⡀⡇⠋⠐⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡌⠀⠀
    ⢸⡄⠸⠀⠀⠀⠸⣿⡿⠋⠉⠙⢿⣿⣇⣠⣤⢼⡋⢃⡴⠋⣰⠁⢿⠈⣆⠀⠀⠀⠉⠳⠤⣀⣸⣿⡿⢛⡏⠉⠻⣿⡇⠀⠀⠀⡇⢀⡇
    ⢸⣿⡄⣇⠀⠀⠀⢻⡁⠀⣀⡤⠞⡫⠛⢑⠖⡭⠂⠉⠀⠀⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⢄⡀⠀⡿⠁⠀⠀⢰⢁⣾⡇
    ⢸⣿⣿⣼⡄⠀⠀⠀⢣⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣶⣶⣶⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠿⣳⠁⠀⠀⠀⣎⣾⣿⡇
    ⢸⣿⣿⣿⣷⡀⠀⠀⠀⠳⡀⠀⠀⠈⠉⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⢯⡉⠁⠀⢀⡜⠁⠀⠀⠀⣼⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣷⣄⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢢⡤⠋⠀⠀⠀⢀⣾⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⡷⣄⠀⠀⠀⠙⠢⣀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⠀⢀⢴⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣮⡳⣄⠀⠀⠀⠈⠑⠢⢄⣀⠀⠀⠀⣿⣿⣿⡇⢠⠃⠀⠀⣀⡠⠔⠊⠁⠀⠀⠀⣀⠔⣹⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡑⠦⣀⠀⠀⠀⠀⠈⠉⠑⠒⢻⣿⣿⡇⡾⠒⠚⠉⠁⠀⠀⠀⠀⢀⡤⠚⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠑⠦⢄⡀⠀⠀⠀⠀⠈⢿⣿⣿⠃⠀⠀⠀⠀⠀⣀⠤⠚⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠈⠑⠒⠤⠤⣀⣀⣛⣁⣀⡤⠤⠐⠚⠉⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
    ⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠲⢤⣀⡠⠔⠚⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀
    You can trade resources  and battle space pirates
    """)
    time.sleep(2)
    os.system('cls')
    print("Are you ready to play?")
    time.sleep(2)
    os.system('cls')
    print("At the start of the game, you have two ships.")
    time.sleep(2)
    print("\n")
    print("Cargo Ship: high cargo space, no ability to fight")
    time.sleep(2)
    print("Fighter Ship: strong weapons, no inventory included")
    time.sleep(2)
    os.system('cls')
    print("There are different planets you can visit")
    time.sleep(2)
    print("Choose a destination, and remember to ensure you have enough fuel before traveling.")
    time.sleep(2.5)
    print("You use fuel for your trips and fights")
    time.sleep(2)
    print("You won't be able to continue if there is no more fuel left.")
    time.sleep(2.5)
    os.system('cls')
    print("Each planet offers unique goods and prices")
    time.sleep(2)
    print("\n")
    print("Visit the planets to:")
    time.sleep(2)
    print("Buy items")
    time.sleep(2)
    print("Sell items")
    time.sleep(2)
    print("Fight against pirates!")
    os.system('cls')
    print("Plan your journey carefully")
    os.system('cls')
    print("Earn credits through trading or combat and win the game!")
    time.sleep(2.5)
    os.system('cls')
    print("""
          
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠀⠀⠀⠀⠀⠀⠀⠐⠂⠤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢄⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
    ⠀⡀⠀⠀⠀⠀⢀⡴⠁⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
    ⠀⢰⠀⠀⠀⢠⠎⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀
    ⠀⠸⡀⠀⣠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⡇⠀
    ⠀⠀⡇⢠⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⡿⠿⠛⠛⡟⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⠃⠀
    ⠀⠀⢃⡏⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⡀⠀⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⣇⠀⠀⠀⠀⡇⠀⠀⠀⠀⣰⡆⠀⠙⢿⣿⣿⣿⠿⣿⣿⣿⣿⣇⠀⠀⠀⡇⠀⠀
    ⠀⠀⢸⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢠⣿⡯⣆⠀⠀⠀⡇⠉⠀⠀⢰⣿⢹⡄⠀⠘⢿⣿⣧⣵⣼⣿⣿⣿⣿⠀⠀⠀⢃⠀⠀
    ⠀⠀⢸⠀⠀⠀⣿⣿⣟⣿⣿⣿⣿⣿⣏⠀⠀⢸⣿⡇⢸⠀⢀⣤⣷⣄⠀⠀⢸⣿⠀⡇⣀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⠀⠀
    ⠀⠀⢸⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⣿⡇⣸⣶⡟⡿⣿⢢⠙⠲⠾⣿⡀⡇⠋⠐⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡌⠀⠀
    ⢸⡄⠸⠀⠀⠀⠸⣿⡿⠋⠉⠙⢿⣿⣇⣠⣤⢼⡋⢃⡴⠋⣰⠁⢿⠈⣆⠀⠀⠀⠉⠳⠤⣀⣸⣿⡿⢛⡏⠉⠻⣿⡇⠀⠀⠀⡇⢀⡇
    ⢸⣿⡄⣇⠀⠀⠀⢻⡁⠀⣀⡤⠞⡫⠛⢑⠖⡭⠂⠉⠀⠀⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⢄⡀⠀⡿⠁⠀⠀⢰⢁⣾⡇
    ⢸⣿⣿⣼⡄⠀⠀⠀⢣⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣶⣶⣶⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠿⣳⠁⠀⠀⠀⣎⣾⣿⡇
    ⢸⣿⣿⣿⣷⡀⠀⠀⠀⠳⡀⠀⠀⠈⠉⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⢯⡉⠁⠀⢀⡜⠁⠀⠀⠀⣼⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣷⣄⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢢⡤⠋⠀⠀⠀⢀⣾⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⡷⣄⠀⠀⠀⠙⠢⣀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⠀⢀⢴⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣮⡳⣄⠀⠀⠀⠈⠑⠢⢄⣀⠀⠀⠀⣿⣿⣿⡇⢠⠃⠀⠀⣀⡠⠔⠊⠁⠀⠀⠀⣀⠔⣹⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡑⠦⣀⠀⠀⠀⠀⠈⠉⠑⠒⢻⣿⣿⡇⡾⠒⠚⠉⠁⠀⠀⠀⠀⢀⡤⠚⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠑⠦⢄⡀⠀⠀⠀⠀⠈⢿⣿⣿⠃⠀⠀⠀⠀⠀⣀⠤⠚⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠈⠑⠒⠤⠤⣀⣀⣛⣁⣀⡤⠤⠐⠚⠉⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
    ⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠲⢤⣀⡠⠔⠚⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀
    """)
    time.sleep(1.5)
    print(". . .")
    time.sleep(1.5)
    print(". . .")
    time.sleep(1.5)
    print(". . .")
    time.sleep(1.5)
    os.system('cls')
    print("Good luck traveler!")
    time.sleep(2)
    





if __name__ == "__main__":
    tutorial()