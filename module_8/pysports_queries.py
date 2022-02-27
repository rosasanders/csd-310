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
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    for team in teams:
        print(f'''
        -- DISPLAYING TEAM RECORDS --
        Team ID: {team[0]}
        Team Name: {team[1]}
        Mascot: {team[2]}
        ''')

    cursor1 = db.cursor()
    cursor1.execute("SELECT player_id, first_name, last_name, team_id from player")
    players = cursor1.fetchall()

    for player in players:
        print(f'''
        -- DISPLAYING PLAYER RECORDS --
        Player ID: {player[0]}
        First Name: {player[1]}
        Last Name: {player[2]}
        Team ID: {player[3]}
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


