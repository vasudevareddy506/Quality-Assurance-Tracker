class QualityRecord:
    def __init__(self, record_id, description, status):
        self.record_id = record_id
        self.description = description
        self.status = status

    def update_record(self, description=None, status=None):
        if description:
            self.description = description
        if status:
            self.status = status

    def __str__(self):
        return (f'Record ID: {self.record_id}, Description: {self.description}, Status: {self.status}')


class QualityTracker:
    def __init__(self):
        self.records = {}

    def create_record(self, record_id, description, status="Pending"):
        if record_id in self.records:
            return f"Record with ID {record_id} already exists."
        else:
            self.records[record_id] = QualityRecord(record_id, description, status)
            return f"Record {record_id} created successfully."

    def read_record(self, record_id):
        return self.records.get(record_id, f"No record found with ID {record_id}")

    def update_record(self, record_id, description=None, status=None):
        record = self.records.get(record_id)
        if record:
            record.update_record(description, status)
            return f"Record {record_id} updated successfully."
        else:
            return f"No record with ID {record_id} exists."

    def delete_record(self, record_id):
        if record_id in self.records:
            del self.records[record_id]
            return f"Record {record_id} deleted successfully."
        else:
            return f"No record with ID {record_id} to delete."

    def log_quality_checks(self, check_id, outcome):
        record = self.records.get(check_id)
        if record:
            # Additional logic for logging the specific outcomes can be implemented here
            return f"Quality check for {check_id}: {outcome}"
        else:
            return f"No record found with ID {check_id} for quality check."

    def manage_quality_issues(self, issue_id, resolution):
        record = self.records.get(issue_id)
        if record:
            record.update_record(status=resolution)
            return f"Issue {issue_id} resolved with resolution: {resolution}"
        else:
            return f"No issue found with ID {issue_id}"


# Part 2: Unit Tests
import unittest

class TestQualityTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = QualityTracker()
        self.tracker.create_record("R001", "First QA Record")

    def test_create_record(self):
        response = self.tracker.create_record("R002", "Second QA Record")
        self.assertIn("created successfully", response)

    def test_read_record_not_found(self):
        response = self.tracker.read_record("R999")
        self.assertIsInstance(response, str)

    def test_update_record(self):
        response = self.tracker.update_record("R001", status="Completed")
        self.assertIn("updated successfully", response)
        record = self.tracker.read_record("R001")
        self.assertEqual(record.status, "Completed")

    def test_delete_record(self):
        response = self.tracker.delete_record("R001")
        self.assertIn("deleted successfully", response)

if __name__ == '__main__':
    unittest.main()
