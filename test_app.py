import unittest
import os
from flask import Flask
from io import BytesIO
from UXUI1 import app  # Import your Flask app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Ensure the upload and result directories exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

    def tearDown(self):
        # Clean up the upload and result directories after each test
        for folder in [app.config['UPLOAD_FOLDER'], app.config['RESULT_FOLDER']]:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

    def test_upload_file(self):
        # Create a dummy MP3 file
        data = {
            'file': (BytesIO(b"Dummy MP3 content"), 'test.mp3')
        }
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('File processed successfully', response.get_data(as_text=True))

        # Check if the PDF file was created
        pdf_filename = 'test.pdf'
        pdf_filepath = os.path.join(app.config['RESULT_FOLDER'], pdf_filename)
        self.assertTrue(os.path.exists(pdf_filepath))

if __name__ == '__main__':
    unittest.main()