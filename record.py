"""
Course: CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Due Date: 26/01/2025
Author: Uyen Minh Trinh

Description:
This file defines the Record class, which represents a single record from the dwelling units dataset.
The class encapsulates data fields and provides a clean string representation for display.
"""

class Record:
    def __init__(self, csduid, csd, period, description, value):
        """
        Constructor to initialize a record object.
        :param csduid: Unique identifier for the area
        :param csd: Name of the area
        :param period: Year of the record
        :param description: Data type description
        :param value: The actual value for the record (float or None if missing)
        """
        self.csduid = csduid
        self.csd = csd
        self.period = period
        self.description = description
        self.value = value

    def __str__(self):
        """
        String representation of the record object.
        :return: A formatted string containing the record data.
        """
        value_str = f"{self.value:.2f}" if self.value is not None else "N/A"
        return (f"CSDUID: {self.csduid}, CSD: {self.csd}, Period: {self.period}, "
                f"Description: {self.description}, Value: {value_str}")

# Example usage for testing:
if __name__ == "__main__":
    # Example data for testing the class
    record = Record("4807044", "Sedgewick", "1994", "Dwelling Units", 364.0)
    print(record)  # Expected Output: CSDUID: 4807044, CSD: Sedgewick, Period: 1994, Description: Dwelling Units, Value: 364.00

    record_with_missing_value = Record("4807045", "ExampleCity", "1995", "Dwelling Units", None)
    print(record_with_missing_value)  # Expected Output: CSDUID: 4807045, CSD: ExampleCity, Period: 1995, Description: Dwelling Units, Value: N/A
