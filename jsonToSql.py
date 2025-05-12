import json
import sqlite3


with open("graph_data.json", "r") as file:
    data = json.load(file)

conn = sqlite3.connect("sluggers.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sluggers (
        name varchar(20) PRIMARY KEY,
        varients int
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Connections (
        name1 varchar(20), 
        name2 varchar(20),
        pos bool,
        primary key (name1, name2)
    )
""")

for player in data["nodes"]:
    cursor.execute("INSERT INTO Sluggers (name, varients) VALUES (?, ?)", 
                   (player["label"], player["varients"]))
    
for connection in data["edges"]:
    cursor.execute("INSERT INTO Connections (name1, name2, pos) VALUES (?, ?, true)", 
                   (connection["source"], connection["target"]))

for connection in data["edgesNeg"]:
    cursor.execute("INSERT INTO Connections (name1, name2, pos) VALUES (?, ?, false)", 
                   (connection["source"], connection["target"]))
    
conn.commit()
conn.close()
