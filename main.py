from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import MySQLConnection

# sqlcon:MySQLConnection = mysql.connector.connect(user="root", password="tobeadded")
# cursor = sqlcon.cursor()

start = True

print("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
""")

while start:
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    dev_y = [38496, 42000, 46752, 49320, 53200,
                56000, 62316, 64928, 67317, 68748, 73752]
    print("What do you want to do?")
    print("(1) View current graph")
    print("(2) Edit values for graph")
    print("(3) Exit")
    input1 = int(input("Type your choice here (1/2/3): "))
    if input1 == 1:
        plt.plot(dev_x, dev_y)
        plt.xlabel('Ages')
        plt.ylabel('Median Salary (USD)')
        plt.title('Median Salary (USD) by Age')
        plt.show()
    elif input1 == 2:
        while True:
            x = int(input("Input value to add on x-axis: "))
            y = int(input("Input value to add on y-axis: "))
            more = input("Do you want to add more items? (Y/N): ")
            dev_x.clear()
            dev_y.append(y)
            if more.lower() == "n":
                break
            else: continue
            
    elif input1 == 3:
        break
    else: print("\n==========ERROR: Choose from 1/2/3==========\n")

#                _                          
#               | |                         
#  __      _____| | ___ ___  _ __ ___   ___ 
#  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
#   \ V  V /  __/ | (_| (_) | | | | | |  __/
#    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                          
                                          
