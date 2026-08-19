from pathlib import Path


PROJECT_NAME = "Railway_Booking_System"


folders = [
    "app",
    "app/database",
    "app/models",
    "app/schemas",
    "app/routers",
    "app/services",
    "app/utils",
    "data",
]


files = [
    "app/main.py",

    "app/database/__init__.py",
    "app/database/connection.py",

    "app/models/__init__.py",
    "app/models/train.py",
    "app/models/passenger.py",
    "app/models/booking.py",

    "app/schemas/__init__.py",
    "app/schemas/train.py",
    "app/schemas/passenger.py",
    "app/schemas/booking.py",

    "app/routers/__init__.py",
    "app/routers/trains.py",
    "app/routers/passengers.py",
    "app/routers/bookings.py",

    "app/services/__init__.py",
    "app/services/booking_service.py",

    "app/utils/__init__.py",
    "app/utils/pnr_generator.py",

    "requirements.txt",
    "README.md",
]


file_contents = {

    "app/main.py": "",

    "app/database/__init__.py": "",

    "app/database/connection.py": "",

    "app/models/__init__.py": "",

    "app/models/train.py": "",

    "app/models/passenger.py": "",

    "app/models/booking.py": "",

    "app/schemas/__init__.py": "",

    "app/schemas/train.py": "",

    "app/schemas/passenger.py": "",

    "app/schemas/booking.py": "",

    "app/routers/__init__.py": "",

    "app/routers/trains.py": "",

    "app/routers/passengers.py": "",

    "app/routers/bookings.py": "",

    "app/services/__init__.py": "",

    "app/services/booking_service.py": "",

    "app/utils/__init__.py": "",

    "app/utils/pnr_generator.py": "",

    "requirements.txt": "",

    "README.md": "",
}


def create_project():

    project_path = Path(PROJECT_NAME)

    for folder in folders:
        folder_path = project_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)

    for file in files:
        file_path = project_path / file

        if not file_path.exists():
            file_path.write_text(
                file_contents.get(file, ""),
                encoding="utf-8"
            )

            print(f"Created: {file_path}")
        else:
            print(f"Already exists: {file_path}")

    print()
    print("Railway Booking System structure created successfully.")
    print(f"Location: {project_path.absolute()}")


if __name__ == "__main__":
    create_project()