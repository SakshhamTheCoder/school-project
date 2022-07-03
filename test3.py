# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from numpy import random
import mysql.connector

# Defining Colours for Printing Purposes
red = (255,51,51)
yellow = (255,255,102)
green = (102,255,102)
blue = (102,178,255)
purple = (204, 153, 255)
orange = (255,178,102)
dark_blue = (102,102,255)
pink = (255, 153, 204)

# Functions for printing a coloured text
def print_colored(color, text):
    print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[38;2;255;255;255m")
def input_colored(color, text):
    input1 = input(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[38;2;255;255;255m")
    return input1

conn = mysql.connector.connect(user="root", password="sqlpass@2021", database="project")
cursor:mysql.connector.connection.CursorBase = conn.cursor()

cursor.execute("SELECT * FROM stats")

# Reading csv file and removing missing values
df = pd.DataFrame(cursor.fetchall()).astype('float64')
df.columns = cursor.column_names

print_colored(purple,'''
        ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
        ───█▒▒░░░░░░░░░▒▒█───
        ────█░░█░░░░░█░░█────          WELCOME TO SONG STAT GRAPH PROJECT
        ─▄▄──█░░░▀█▀░░░█──▄▄─
        █░░█─▀▄░░░░░░░▄▀─█░░█
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█       - Made by:  Sakshham   &   Vasundhra
        █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█                    Bhagat         Sharma
        █░░║║║╠─║─║─║║║║║╠─░░█
        █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█

''')

def histogram():
    print_colored(orange, "\n: SELECT DATA :")
    print_colored(pink,
            "Which data would you like to view? \n (1) Danceability \n (2) Energy \n (3) Tempo \n (4) Time_Signature ")
    reply5 = input_colored(blue, "Select one - (1)/(2)/(3)/(4) : ")
    if reply5 == "1":
        df["Danceability"].plot(kind="hist", color="yellow")
        plt.show()
    elif reply5 == "2":
        df["Energy"].plot(kind="hist", color="red")
        plt.show()
    elif reply5 == "3":
        df["Tempo"].plot(kind="hist", color="green")
        plt.show()
    elif reply5 == "4":
        df["Time_signature"].plot(kind="hist", color="purple")
        plt.show()
    else:
        print_colored(red, "Choose a valid option")
        return

def axis_select(type: str):
    random_color = str(random.choice(
        ["red", "green", "blue", "yellow", "purple", "pink", "black", "brown"]))
    random_marker = str(random.choice(["o", "d"]))
    print_colored(orange, "\n: SELECT AXES : ")
    print_colored(yellow, " (1) Danceability \n (2) Energy \n (3) Tempo \n (4) Time_signature")
    reply3 = input_colored(blue, "Select X-axis - (1)/(2)/(3)/(4): ")
    reply4 = input_colored(blue, "Select Y-axis - (1)/(2)/(3)/(4): ")
    if reply3 == "1" and reply4 == "2":
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Danceability", y="Energy")
        plt.show()
    elif reply3 == "1" and reply4 == "3":
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Danceability", y="Tempo")
        plt.show()
    elif reply3 == '1' and reply4 == '4':
        df.plot(kind=type, color=random_color, marker=random_marker,
                x="Danceability", y="Time_signature")
        plt.show()
    elif reply3 == '2' and reply4 == '1':
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Energy", y="Danceability")
        plt.show()
    elif reply3 == '2' and reply4 == '3':
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Energy", y="Tempo")
        plt.show()
    elif reply3 == '2' and reply4 == '4':
        df.plot(kind=type, color=random_color, marker=random_marker,
                x="Energy", y="Time_signature")
        plt.show()
    elif reply3 == '3' and reply4 == '1':
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Tempo", y="Danceability")
        plt.show()
    elif reply3 == '3' and reply4 == '2':
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Tempo", y="Energy")
        plt.show()
    elif reply3 == '3' and reply4 == '4':
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Tempo", y="Time_signature")
        plt.show()
    elif reply3 == '4' and reply4 == '1':
        df.plot(kind=type, color=random_color, marker=random_marker,
                x="Time_signature", y="Danceability")
        plt.show()
    elif reply3 == '4' and reply4 == '2':
        df.plot(kind=type, color=random_color, marker=random_marker,
                x="Time_signature", y="Energy")
        plt.show()
    elif reply3 == '4' and reply4 == '3':
        df.plot(kind=type, color=random_color,
                marker=random_marker, x="Time_signature", y="Tempo")
        plt.show()
    else:
        print_colored(red, "Choose a valid option")
        return
    # print(f": SHOWING A GRAPH OF TYPE *{type}* WITH X-AXIS AS *{reply3}* AND Y-AXIS AS *{reply4}*")

def delete(column):
    rec = input_colored(blue, "Enter which value you wanna choose?: ")
    cursor.execute(f"DELETE from stats WHERE {column} = {rec}")
    conn.commit()
    print_colored(green, "Deleted Record")

def add(Danceability, Energy, Tempo, Time_signature):
    cursor.execute(f"INSERT into stats VALUES({Danceability}, {Energy}, {Tempo}, {Time_signature})")
    conn.commit()
    print_colored(green, "Added a new record")


print_colored(dark_blue, "What do you want to do ? \n  (1) View graph \n  (2) Edit graph \n  (3) View Data \n  (4) Exit")
reply = input_colored(blue, "Select one - (1)/(2)/(3) : ")
if reply == "1":
    print_colored(orange, "\n: VIEW GRAPHS : ")
    print_colored(green, "Which type of graph do you want to view? \n (1) Line Graph \n (2) Bar Graph \n (3) Histogram \n (4) Pie Chart \n (5) Scatter")
    reply2 = input_colored(blue, "Select one - (1)/(2)/(3)/(4)/(5): ")
    if reply2 == "1":
        axis_select("line")
    elif reply2 == "2":
        axis_select("bar")
    elif reply2 == "3":
        histogram()
    elif reply2 == "4":
        print("pie here")
    elif reply2 == "5":
        axis_select("scatter")
    else:
        print_colored(red, "Choose a valid option")
elif reply == "2":
    print_colored(orange, "What do you want to do?\n (1) Add \n (2) Delete")
    action = input_colored(blue, "Select one - (1)/(2): ")
    if action == '1':
        danceability = float(input_colored(dark_blue, "Enter value for Danceability: "))
        energy = float(input_colored(dark_blue, "Enter value for Energy: "))
        tempo = float(input_colored(dark_blue, "Enter value for Tempo: "))
        ts = int(input_colored(dark_blue, "Enter value for Time Signature: "))
        add(danceability, energy, tempo, ts)
    if action == '2':
        print_colored(green, "With which column you want to delete a record?\n (1) Danceability \n (2) Energy \n (3) Tempo \n (4) Time_signature")
        column = input_colored(blue, "Select one - (1)/(2)/(3)/(4)/(5): ")
        if column == "1":
            delete("Danceability")
        elif column == "2":
            delete("Energy")
        elif column == "3":
            delete("Tempo")
        elif column == "1":
            delete("Time_signature")
        else:
            print_colored(red, "Choose a valid option")

elif reply == "3":
    print_colored(green, df)
elif reply == "4":
    exit()
else:
    print_colored(red, "Choose a valid option")
