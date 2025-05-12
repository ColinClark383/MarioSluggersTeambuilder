import sqlite3

# Character stats data
data = [
    ("Yoshi", 4, 4, 6, 9),
    ("Koopa Troopa", 3, 6, 4, 6),
    ("Red Toad", 5, 5, 3, 7),
    ("Shy Guy", 4, 5, 7, 4),
    ("Koopa Paratroopa", 4, 4, 7, 5),
    ("Blue Pianta", 5, 8, 4, 2),
    ("Red Pianta", 4, 8, 4, 2),
    ("Yellow Pianta", 4, 8, 4, 2),
    ("Blue Noki", 5, 4, 4, 7),
    ("Red Noki", 4, 4, 5, 7),
    ("Green Noki", 4, 5, 4, 7),
    ("Hammer Bro", 4, 7, 6, 3),
    ("Blue Toad", 4, 6, 3, 7),
    ("Yellow Toad", 3, 6, 4, 7),
    ("Green Toad", 4, 5, 4, 7),
    ("Purple Toad", 5, 6, 2, 7),
    ("Magikoopa", 8, 2, 8, 2),
    ("Red Magikoopa", 8, 3, 8, 1),
    ("Green Magikoopa", 7, 2, 8, 2),
    ("Yellow Magikoopa", 7, 3, 8, 2),
    ("Red Koopa Troopa", 4, 6, 3, 6),
    ("Green Koopa Paratroopa", 3, 5, 7, 5),
    ("Blue Shy Guy", 5, 4, 7, 4),
    ("Yellow Shy Guy", 4, 4, 7, 5),
    ("Green Shy Guy", 3, 5, 7, 5),
    ("Gray Shy Guy", 4, 4, 8, 4),
    ("Dry Bones", 4, 7, 4, 5),
    ("Green Dry Bones", 3, 7, 4, 6),
    ("Red Dark Bones", 5, 7, 4, 5),
    ("Blue Dry Bones", 3, 7, 5, 5),
    ("Fire Bro", 3, 8, 6, 3),
    ("Boomerang Bro", 5, 7, 5, 3),
    ("Kritter", 4, 7, 7, 3),
    ("Blue Kritter", 5, 6, 7, 3),
    ("Red Kritter", 3, 8, 7, 3),
    ("Brown Kritter", 3, 7, 7, 4),
    ("Red Yoshi", 3, 4, 4, 8),
    ("Blue Yoshi", 4, 2, 6, 8),
    ("Yellow Yoshi", 3, 4, 6, 7),
    ("Light Blue Yoshi", 3, 3, 6, 8),
    ("Pink Yoshi", 2, 3, 6, 9),
]

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("backend/sluggers.db")
cursor = conn.cursor()


# Function to update or insert data
def update_character_stats(data):
    for name, stat1, stat2, stat3, stat4 in data:
        cursor.execute(
            """
            UPDATE Varients
            SET pitching = ?, batting = ?, feilding = ?, speed = ?
            WHERE varient = ?
            """,
            (stat1, stat2, stat3, stat4, name),
        )

# Update or insert the character data
update_character_stats(data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Character stats have been updated in the database.")
