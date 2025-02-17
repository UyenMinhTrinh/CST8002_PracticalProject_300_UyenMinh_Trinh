class Business:
    def __init__(self, records):
        self.records = records

    def find_record(self, period):
        """Find and return records matching a given period."""
        results = [record for record in self.records if record.period == period]
        if results:
            return results
        else:
            return None

    def add_record(self, record):
        """Adds a new record to the in-memory dataset."""
        self.records.append(record)
        print("Record successfully added.")


    def list_records(self):
        """Displays all records, printing 'Program by Uyen Minh Trinh' every 10 records."""
        if not self.records:
            print("No records available.")
            return

        print("\n--- Listing Records ---")
        for index, record in enumerate(self.records, start=1):
            print(record)
            if index % 10 == 0:
                print("\nProgram by Uyen Minh Trinh\n")