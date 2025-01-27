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
