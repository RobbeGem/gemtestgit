from odoo.tests.common import TransactionCase


class TestMyModel(TransactionCase):
    def setUp(self):
        super().setUp()
        self.my_model = self.env['my.model']

    def test_create_record(self):
        # Create a record
        record = self.my_model.create({
            'my_field': 'Test Value',
        })

        # Check if the record is created
        self.assertEqual(record.my_field, 'Test Value')

    def test_update_record(self):
        # Create a record
        record = self.my_model.create({
            'my_field': 'Test Value',
        })

        # Update the record
        record.write({
            'my_field': 'Updated Value',
        })

        # Check if the record is updated
        self.assertEqual(record.my_field, 'Updated Value')

    def test_delete_record(self):
        # Create a record
        record = self.my_model.create({
            'my_field': 'Test Value',
        })

        # Delete the record
        record.unlink()

        # Check if the record is deleted
        self.assertFalse(self.my_model.exists([record.id]))