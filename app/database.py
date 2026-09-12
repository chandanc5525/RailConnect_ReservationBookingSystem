# Import sqlite3 Library
import sqlite3 

# Setting Database Path 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "railway.db"

# Function Definition
def create_database():

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    # Train table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            train_number TEXT UNIQUE NOT NULL,
            train_name TEXT NOT NULL,
            source TEXT NOT NULL,
            destination TEXT NOT NULL,
            departure_time TEXT,
            arrival_time TEXT,
            total_seats INTEGER NOT NULL,
            available_seats INTEGER NOT NULL
        )
    """)

    # Passenger table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT,
            phone TEXT
        )
    """)

    # Booking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pnr TEXT UNIQUE NOT NULL,
            train_id INTEGER,
            passenger_id INTEGER,
            seat_number TEXT,
            booking_date TEXT,
            status TEXT,
            FOREIGN KEY (train_id) REFERENCES trains(id),
            FOREIGN KEY (passenger_id) REFERENCES passengers(id)
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")


# Function Calling
create_database()