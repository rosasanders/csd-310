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

    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

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