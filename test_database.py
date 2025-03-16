import pytest
from record_manager import RecordManager

@pytest.fixture
def manager():
    """Fixture to create a new instance of RecordManager."""
    return RecordManager()

def test_add_record(manager):
    """Test adding a record to the database."""
    manager.add_record("Test User", 123)
    records = manager.get_all_records()
    assert len(records) > 0  # Ensure that a record is added
    assert records[-1].name == "Test User"
    assert records[-1].value == 123

def test_update_record(manager):
    """Test updating a record in the database."""
    manager.add_record("Old Name", 50)
    last_record = manager.get_all_records()[-1]
    manager.update_record(last_record.id, "New Name", 100)
    updated_record = manager.get_all_records()[-1]
    assert updated_record.name == "New Name"
    assert updated_record.value == 100

def test_delete_record(manager):
    """Test deleting a record from the database."""
    manager.add_record("Delete Me", 999)
    last_record = manager.get_all_records()[-1]
    manager.delete_record(last_record.id)
    records = manager.get_all_records()
    assert all(record.id != last_record.id for record in records)
