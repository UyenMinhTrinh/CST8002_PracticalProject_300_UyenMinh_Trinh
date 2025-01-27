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
    records = []
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
                records.append(record)
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
    print("Author: Uyen Minh Trinh")
    file_path = 'Dwellingunitsdownload.csv'
    records = load_data(file_path)
    if records:
        display_records(records)
    else:
        print("No records to display.")

if __name__ == "__main__":
    main()
