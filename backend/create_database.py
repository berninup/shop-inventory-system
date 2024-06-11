import sqlite3

def create_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create Locations table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Locations (
        LocationID INTEGER PRIMARY KEY AUTOINCREMENT,
        LocationDescription TEXT NOT NULL
    )
    ''')

    # Create Totes table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Totes (
        ToteID INTEGER PRIMARY KEY AUTOINCREMENT,
        ToteDescription TEXT NOT NULL,
        LocationID INTEGER,
        FOREIGN KEY (LocationID) REFERENCES Locations (LocationID)
    )
    ''')

    # Create Items table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Items (
        ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        ItemName TEXT NOT NULL,
        Description TEXT,
        Keywords TEXT,
        ToteID INTEGER,
        FOREIGN KEY (ToteID) REFERENCES Totes (ToteID)
    )
    ''')

    # Insert sample data
    cursor.execute("INSERT INTO Locations (LocationDescription) VALUES ('Shelf A')")
    cursor.execute("INSERT INTO Locations (LocationDescription) VALUES ('Shelf B')")
    cursor.execute("INSERT INTO Totes (ToteDescription, LocationID) VALUES ('Tote 1', 1)")
    cursor.execute("INSERT INTO Totes (ToteDescription, LocationID) VALUES ('Tote 2', 2)")
    cursor.execute("INSERT INTO Items (ItemName, Description, Keywords, ToteID) VALUES ('Widget', 'A useful widget', 'useful,widget', 1)")
    cursor.execute("INSERT INTO Items (ItemName, Description, Keywords, ToteID) VALUES ('Gadget', 'A fancy gadget', 'fancy,gadget', 2)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully with sample data.")
