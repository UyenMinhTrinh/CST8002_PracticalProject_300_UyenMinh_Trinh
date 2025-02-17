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
    """
    Main entry point for the program.
    """
    print("Author: Uyen Minh Trinh\n", flush=True)
    # Variable declaration
    file_path = 'Dwellingunitsdownload.csv'
    business = Business(records)

    while True:
        print("\n--- Data Management System ---")
        print("\nProgram by Uyen Minh Trinh\n")
        print("1. List all records")
        print("2. Find a record")
        print("3. Add a record")
        print("4. Update a record")
        print("5. Delete a record")
        print("6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            business.list_records()
        elif choice == "2":
            period = int(input("Enter period: "))
            result = business.find_record(period)
            if result:
                for record in result:
                    print(record)
            else:
                print("Record not found.")
        elif choice == "3":
            csduid = input("Enter CSDUID: ")
            csd = input("Enter CSD: ")
            period = input("Enter period: ")
            description = input("Enter description: ")
            value = input("Enter value: ")
            business.add_record(Record(csduid, csd, period, description, value))
            print("New record has been added.")
        elif choice == "4":
            period = int(input("Enter period to update: "))
            new_value = float(input("Enter new value: "))
            if business.update_record(period, new_value):
                print("Record updated.")
            else:
                print("Record not found.")
        elif choice == "5":
            period = int(input("Enter period to delete: "))
            business.delete_record(period)
            print("Record deleted.")
        elif choice == "6":
            Persistence.save_data(business.records)
            print("Exiting...")
            break
        elif choice == "7":
            records = Persistence.load_data(filename)
            business = Business(records)
            print("Data has been reloaded from the dataset.")
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()
