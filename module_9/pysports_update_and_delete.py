from ast import Delete
from optparse import Values
from tkinter import INSERT
from turtle import update
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print(f'\n Database user {config["user"]} connected to MySQL on host {config["host"]} with database {config["database"]}.')

    insert_cursor = db.cursor()
    insert_cursor.execute("INSERT INTO player (first_name, last_name, team_id) Values ('Smeagol', 'Shire Folk', 1)");

    cursor1 = db.cursor()
    cursor1.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor1.fetchall()

    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f'''
    Player ID: {player[0]}
    First Name: {player[1]}
    Last Name: {player[2]}
    Team Name: {player[3]}
        ''')

    update_cursor = db.cursor()
    update_cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'");

    cursor2 = db.cursor()
    cursor2.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor2.fetchall()

    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f'''
    Player ID: {player[0]}
    First Name: {player[1]}
    Last Name: {player[2]}
    Team Name: {player[3]}
        ''')

    delete_cursor = db.cursor()
    delete_cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol'");

    cursor3 = db.cursor()
    cursor3.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id");

    players = cursor3.fetchall()

    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f'''
    Player ID: {player[0]}
    First Name: {player[1]}
    Last Name: {player[2]}
    Team Name: {player[3]}
        ''')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()
