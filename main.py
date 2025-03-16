"""
Course: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Due Date: 26/01/2025
Author: Uyen Minh Trinh

Description:
This is the main program file for parsing a CSV file into Record objects
and displaying the records in the console. It demonstrates the use of File I/O,
Object-Oriented Programming (OOP), and error handling in Python.
"""

import csv
from record import Record
from persistence import Persistence
from business import Business
from record_manager import RecordManager

def load_data(file_path):
    """
    Loads data from a CSV file and initializes Record objects.
    :param file_path: Path to the CSV file.
    :return: A list of Record objects.
    """
    records = []  # Initialize an empty list
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader for column-based access
            for row in reader:
                # Extract relevant fields from each row
                csduid = row['CSDUID']
                csd = row['CSD']
                period = row['Period']
                description = row['IndicatorSummaryDescription']
                value = row['OriginalValue']
                
                # Handle missing or invalid values for "value"
                value = float(value) if value else None
                
                # Create a Record object and add it to the list
                record = Record(csduid, csd, period, description, value)
                records.append(record)  # Add each Record object to the list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except KeyError as e:
        print(f"Missing column in the dataset: {e}")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
    return records

def display_records(records):
    """
    Displays all records in the console.
    :param records: List of Record objects.
    """
    print("\n--- Records ---")
    for record in records:
        print(record)

def main():
    manager = RecordManager()  # ✅ Now it should work

    while True:
        print("\n1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            value = int(input("Enter value: "))
            manager.add_record(name, value)

        elif choice == "2":
            records = manager.get_all_records()
            for record in records:
                print(f"ID: {record.id}, Name: {record.name}, Value: {record.value}")

        elif choice == "3":
            record_id = int(input("Enter ID to update: "))
            new_name = input("Enter new name: ")
            new_value = int(input("Enter new value: "))
            manager.update_record(record_id, new_name, new_value)

        elif choice == "4":
            record_id = int(input("Enter ID to delete: "))
            manager.delete_record(record_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
