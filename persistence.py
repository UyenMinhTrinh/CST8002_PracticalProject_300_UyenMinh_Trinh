import csv
import uuid
import os
from record import Record

class Persistence:
    @staticmethod
    def load_data(filename):
        """Reloads data from CSV, replacing in-memory data."""
        records = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    records.append(Record(
                        row['CSDUID'], row['CSD'], row['Period'], 
                        row['IndicatorSummaryDescription'], row['OriginalValue']
                    ))
            print("Data successfully reloaded from the dataset.")
        except FileNotFoundError:
            print("Error: File not found.")
        return records

    @staticmethod
    def save_data(records, directory='output'):
        """Saves records to a new file with a unique UUID-based filename."""
        if not os.path.exists(directory):
            os.makedirs(directory)  # Ensure the output directory exists

        # Generate a unique filename using UUID
        filename = os.path.join(directory, f"output_{uuid.uuid4()}.csv")

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            # Write the CSV header
            writer.writerow(["CSDUID", "CSD", "Period", "IndicatorSummaryDescription", "OriginalValue"])
            # Write the data records
            for record in records:
                writer.writerow([record.csduid, record.csd, record.period, record.description, record.value])

        print(f"Data saved to {filename}")
