import os
from datetime import datetime

def write_diary_entry():
    entry = input("Write your diary entry:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp}\n{entry}\n\n")
    print("Diary entry saved successfully!\n")

def read_diary_entries():
    if os.path.exists("diary.txt"):
        with open("diary.txt", "r") as file:
            entries = file.read()
            print("----- Your Diary Entries -----")
            print(entries)
    else:
        print("No diary entries found.\n")

# Main program loop

while True:
    print("1. Write a Diary Entry")
    print("2. Read Diary Entries")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

# write in diary
    if choice == "1":
        write_diary_entry()
# read from diary
    elif choice == "2":
        read_diary_entries()
# exit
    elif choice == "3":
        print("Exiting the Personal Diary application. Goodbye!")
        break
# choice validation
    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")
