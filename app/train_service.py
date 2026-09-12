import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "railway.db"


def add_train():
    print("\nAdd Train")

    train_number = input("Enter train number: ").strip()
    train_name = input("Enter train name: ").strip()
    source = input("Enter source: ").strip()
    destination = input("Enter destination: ").strip()
    departure_time = input("Enter departure time: ").strip()
    arrival_time = input("Enter arrival time: ").strip()

    try:
        total_seats = int(input("Enter total seats: "))

        if total_seats <= 0:
            print("Total seats must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number for seats.")
        return

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO trains (
                train_number,
                train_name,
                source,
                destination,
                departure_time,
                arrival_time,
                total_seats,
                available_seats
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            train_number,
            train_name,
            source,
            destination,
            departure_time,
            arrival_time,
            total_seats,
            total_seats
        ))

        connection.commit()
        print("Train added successfully.")

    except sqlite3.IntegrityError:
        print("Train number already exists.")

    finally:
        connection.close()


def view_trains():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            train_number,
            train_name,
            source,
            destination,
            departure_time,
            arrival_time,
            total_seats,
            available_seats
        FROM trains
        ORDER BY train_number
    """)

    trains = cursor.fetchall()
    connection.close()

    print("\nAll Trains")

    if not trains:
        print("No trains found.")
        return

    for train in trains:
        print("-" * 60)
        print(f"ID              : {train[0]}")
        print(f"Train Number    : {train[1]}")
        print(f"Train Name      : {train[2]}")
        print(f"Route           : {train[3]} -> {train[4]}")
        print(f"Departure       : {train[5]}")
        print(f"Arrival         : {train[6]}")
        print(f"Total Seats     : {train[7]}")
        print(f"Available Seats : {train[8]}")


def search_trains():
    source = input("\nEnter source: ").strip()
    destination = input("Enter destination: ").strip()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            train_number,
            train_name,
            source,
            destination,
            departure_time,
            arrival_time,
            available_seats
        FROM trains
        WHERE LOWER(source) = LOWER(?)
        AND LOWER(destination) = LOWER(?)
        AND available_seats > 0
        ORDER BY departure_time
    """, (source, destination))

    trains = cursor.fetchall()
    connection.close()

    print("\nSearch Results")

    if not trains:
        print("No available trains found.")
        return

    for train in trains:
        print("-" * 60)
        print(f"Train Number    : {train[0]}")
        print(f"Train Name      : {train[1]}")
        print(f"Route           : {train[2]} -> {train[3]}")
        print(f"Departure       : {train[4]}")
        print(f"Arrival         : {train[5]}")
        print(f"Available Seats : {train[6]}")


def update_train():
    train_number = input("\nEnter train number to update: ").strip()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM trains
        WHERE train_number = ?
    """, (train_number,))

    train = cursor.fetchone()

    if not train:
        print("Train not found.")
        connection.close()
        return

    print("\nPress Enter to keep the existing value.")

    train_name = input(f"Train name [{train[2]}]: ").strip()
    source = input(f"Source [{train[3]}]: ").strip()
    destination = input(f"Destination [{train[4]}]: ").strip()
    departure_time = input(f"Departure [{train[5]}]: ").strip()
    arrival_time = input(f"Arrival [{train[6]}]: ").strip()

    train_name = train_name or train[2]
    source = source or train[3]
    destination = destination or train[4]
    departure_time = departure_time or train[5]
    arrival_time = arrival_time or train[6]

    cursor.execute("""
        UPDATE trains
        SET
            train_name = ?,
            source = ?,
            destination = ?,
            departure_time = ?,
            arrival_time = ?
        WHERE train_number = ?
    """, (
        train_name,
        source,
        destination,
        departure_time,
        arrival_time,
        train_number
    ))

    connection.commit()
    connection.close()

    print("Train updated successfully.")


def delete_train():
    train_number = input("\nEnter train number to delete: ").strip()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT train_name
        FROM trains
        WHERE train_number = ?
    """, (train_number,))

    train = cursor.fetchone()

    if not train:
        print("Train not found.")
        connection.close()
        return

    print(f"Train found: {train[0]}")

    confirmation = input("Are you sure you want to delete it? (yes/no): ").strip().lower()

    if confirmation == "yes":
        cursor.execute("""
            DELETE FROM trains
            WHERE train_number = ?
        """, (train_number,))

        connection.commit()
        print("Train deleted successfully.")
    else:
        print("Delete operation cancelled.")

    connection.close()

# Define Orchestrator: Entry Point
def main():
    while True:
        print("\nRailway Reservation System")
        print("1. Add Train")
        print("2. View All Trains")
        print("3. Search Train")
        print("4. Update Train")
        print("5. Delete Train")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_train()

        elif choice == "2":
            view_trains()

        elif choice == "3":
            search_trains()

        elif choice == "4":
            update_train()

        elif choice == "5":
            delete_train()

        elif choice == "6":
            print("Thank you for using Railway Reservation System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Function Calling
main()