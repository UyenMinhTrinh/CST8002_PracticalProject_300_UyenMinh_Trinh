from database import session, Record

class RecordManager:
    def add_record(self, name, value):
        """Insert a new record into the database."""
        new_record = Record(name=name, value=value)
        session.add(new_record)
        session.commit()
        print(f"Added: {new_record}")

    def get_all_records(self):
        """Retrieve all records from the database."""
        records = session.query(Record).all()
        return records

    def update_record(self, record_id, new_name, new_value):
        """Update a record in the database."""
        record = session.query(Record).filter(Record.id == record_id).first()
        if record:
            record.name = new_name
            record.value = new_value
            session.commit()
            print(f"Updated Record {record_id}")
        else:
            print("Record not found!")

    def delete_record(self, record_id):
        """Delete a record from the database."""
        record = session.query(Record).filter(Record.id == record_id).first()
        if record:
            session.delete(record)
            session.commit()
            print(f"Deleted Record {record_id}")
        else:
            print("Record not found!")

# Example Usage
if __name__ == "__main__":
    manager = RecordManager()
    manager.add_record("Example Name", 100)
    print(manager.get_all_records())
