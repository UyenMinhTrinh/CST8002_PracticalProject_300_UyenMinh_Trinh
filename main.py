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
