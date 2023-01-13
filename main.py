# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from numpy import random
import mysql.connector

# Defining Colours for Printing Purposes
red = (255, 51, 51)
yellow = (255, 255, 102)
green = (102, 255, 102)
blue = (102, 178, 255)
purple = (204, 153, 255)
orange = (255, 178, 102)
dark_blue = (102, 102, 255)
pink = (255, 153, 204)

# Functions for printing a coloured text
def print_colored(color, text):
    print(f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[38;2;255;255;255m")
    print()


def input_colored(color, text):
    input1 = input(
        f"\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[38;2;255;255;255m"
    )
    print()
    return input1


# MYSQL Connection
conn = mysql.connector.connect(user="root", password="sqlpass@2021", database="project")
cursor = conn.cursor()

cursor.execute("SELECT * FROM stats")

# Reading the database as a dataframe
df = pd.DataFrame(cursor.fetchall()).astype(float)
df.columns = cursor.column_names

# Welcome Screen
print_colored(
    purple,
    """
        ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
        ───█▒▒░░░░░░░░░▒▒█───
        ────█░░█░░░░░█░░█────          WELCOME TO SONG STAT GRAPH PROJECT
        ─▄▄──█░░░▀█▀░░░█──▄▄─
        █░░█─▀▄░░░░░░░▄▀─█░░█
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█       - Made by:  Sakshham   &   Vasundhra
        █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█                    Bhagat         Sharma
        █░░║║║╠─║─║─║║║║║╠─░░█
        █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█

""",
)

# Define Function For HISTOGRAM
def histogram():
    print_colored(orange, "\n: SELECT DATA :")
    print_colored(
        pink,
        "Which data would you like to view? \n (1) Danceability \n (2) Energy \n (3) Tempo \n (4) Time_Signature ",
    )
    reply5 = input_colored(blue, "Select one - (1)/(2)/(3)/(4) : ")
    if reply5 == "1":
        df["Danceability"].plot(kind="hist", color="yellow", edgecolor="black")
        plt.show()
    elif reply5 == "2":
        df["Energy"].plot(kind="hist", color="red", edgecolor="black")
        plt.show()
    elif reply5 == "3":
        df["Tempo"].plot(kind="hist", color="green", edgecolor="black")
        plt.show()
    elif reply5 == "4":
        df["Time_signature"].plot(kind="hist", color="purple", edgecolor="black")
        plt.show()
    else:
        print_colored(red, "Choose a valid option")
        return


# Define Common Function For PLOTTING
def axis_select(type: str):
    random_color = str(
        random.choice(
            ["red", "green", "blue", "yellow", "purple", "pink", "black", "brown"]
        )
    )
    # random_marker = str(random.choice(["o", "d"]))
    # print(random_marker)
    print_colored(orange, "\n: SELECT AXES : ")
    print_colored(
        yellow, " (1) Danceability \n (2) Energy \n (3) Tempo \n (4) Time_signature"
    )
    reply3 = input_colored(blue, "Select X-axis - (1)/(2)/(3)/(4): ")
    reply4 = input_colored(blue, "Select Y-axis - (1)/(2)/(3)/(4): ")
    if reply3 == "1" and reply4 == "2":
        df.plot(
            kind=type,
            color=random_color,
            x="Danceability",
            y="Energy",
        )
    elif reply3 == "1" and reply4 == "3":
        df.plot(
            kind=type,
            color=random_color,
            x="Danceability",
            y="Tempo",
        )
    elif reply3 == "1" and reply4 == "4":
        df.plot(
            kind=type,
            color=random_color,
            x="Danceability",
            y="Time_signature",
        )
    elif reply3 == "2" and reply4 == "1":
        df.plot(
            kind=type,
            color=random_color,
            x="Energy",
            y="Danceability",
        )
    elif reply3 == "2" and reply4 == "3":
        df.plot(
            kind=type,
            color=random_color,
            x="Energy",
            y="Tempo",
        )
    elif reply3 == "2" and reply4 == "4":
        df.plot(
            kind=type,
            color=random_color,
            x="Energy",
            y="Time_signature",
        )
    elif reply3 == "3" and reply4 == "1":
        df.plot(
            kind=type,
            color=random_color,
            x="Tempo",
            y="Danceability",
        )
    elif reply3 == "3" and reply4 == "2":
        df.plot(
            kind=type,
            color=random_color,
            x="Tempo",
            y="Energy",
        )
    elif reply3 == "3" and reply4 == "4":
        df.plot(
            kind=type,
            color=random_color,
            x="Tempo",
            y="Time_signature",
        )
    elif reply3 == "4" and reply4 == "1":
        df.plot(
            kind=type,
            color=random_color,
            x="Time_signature",
            y="Danceability",
        )
    elif reply3 == "4" and reply4 == "2":
        df.plot(
            kind=type,
            color=random_color,
            x="Time_signature",
            y="Energy",
        )
    elif reply3 == "4" and reply4 == "3":
        df.plot(
            kind=type,
            color=random_color,
            x="Time_signature",
            y="Tempo",
        )
    else:
        print_colored(red, "Choose a valid option")
        return
    print(f": SHOWING A GRAPH OF TYPE *{type.upper()}*")
    plt.show()


# Define Function For Deleting The DATA
def delete(rec):
    cursor.execute(f"DELETE from stats WHERE Sno = {rec}")
    cursor.execute("ALTER TABLE stats DROP Sno")
    cursor.execute("ALTER TABLE stats ADD Sno INT AUTO_INCREMENT PRIMARY KEY FIRST")
    conn.commit()
    print_colored(green, "Deleted Record")


# Define Function For Adding The DATA
def add(Danceability, Energy, Tempo, Time_signature):
    cursor.execute(
        f"INSERT into stats(Danceability, Energy, Tempo, Time_signature) VALUES({Danceability}, {Energy}, {Tempo}, {Time_signature})"
    )
    conn.commit()
    print_colored(green, "Added a new record")


# Main Screen
while True:
    print_colored(
        dark_blue,
        "What do you want to do ? \n  (1) View Graph \n  (2) Edit Data \n  (3) View Data \n  (4) Exit",
    )
    reply = input_colored(blue, "Select one - (1)/(2)/(3)/(4) : ")
    if reply == "1":
        print_colored(orange, "\n: VIEW GRAPHS : ")
        print_colored(
            green,
            "Which type of graph do you want to view? \n (1) Line Graph \n (2) Bar Graph \n (3) Histogram \n (4) Scatter",
        )
        reply2 = input_colored(blue, "Select one - (1)/(2)/(3)/(4)/(5): ")
        if reply2 == "1":
            axis_select("line")
        elif reply2 == "2":
            axis_select("bar")
        elif reply2 == "3":
            histogram()
        elif reply2 == "4":
            axis_select("scatter")
        else:
            print_colored(red, "Choose a valid option")
    elif reply == "2":
        print_colored(orange, "What do you want to do?\n (1) Add \n (2) Delete")
        action = input_colored(blue, "Select one - (1)/(2): ")
        if action == "1":
            danceability = float(
                input_colored(dark_blue, "Enter value for Danceability: ")
            )
            energy = float(input_colored(dark_blue, "Enter value for Energy: "))
            tempo = float(input_colored(dark_blue, "Enter value for Tempo: "))
            ts = int(input_colored(dark_blue, "Enter value for Time Signature: "))
            add(danceability, energy, tempo, ts)
            break
        if action == "2":
            rec = int(input_colored(blue, "Enter which record you want to delete?: "))
            if rec <= len(df.index):
                delete(rec)
            else:
                print_colored(red, "Choose a valid index")
            break

    elif reply == "3":
        print_colored(green, df.to_string(index=False))
    elif reply == "4":
        print_colored(purple, "Thanks for using ^^")
        exit()
    else:
        print_colored(red, "Choose a valid option")
