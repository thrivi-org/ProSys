# READ.ME

#### ProSys

(Owned & developed by, for and through Thrivi)

## This project processes MP3 files, transcribes them, extracts data, and provides results through a web interface.

markdown

\# ProSys - MP3 Transcription and Data Extraction System

ProSys is a Python-based application designed for transcription and extraction of structured data from MP3 files. Leveraging advanced speech-to-text models like OpenAI's Whisper, ProSys enables seamless extraction of information such as phone numbers, dates, names, and addresses. It includes a user-friendly web interface for file uploads and result visualization.

## Features

- **MP3 to Text Conversion**: Transcribes MP3 files using OpenAI Whisper for high-accuracy speech-to-text.
- **Data Extraction**: Identifies structured data such as phone numbers, dates, and names using regular expressions.
- **Web Interface**: A responsive web UI for uploading MP3 files and viewing categorized results.
- **Email Notifications**: Sends results via email upon successful processing.
- **Error Handling**: Robust backend with clear feedback for invalid inputs or processing errors.

## Getting Started

### Prerequisites

- Python 3.10 (Recommended)
- Pip (Python package manager)

### Installation

1. **Clone the Repository**

```other
git clone https://github.com/thrivi-org/ProSys.git
cd ProSys`
```

2. **Set Up Virtual Environment**

   bash

   Copy code

   `python -m venv .venv

   source .venv/bin/activate    # Linux/Mac

   .venv\Scripts\activate       # Windows`

3. **Install Dependencies**

   bash

   Copy code

   `pip install -r requirements.txt`

4. **Install Whisper**

   bash

   Copy code

   `pip install openai-whisper torch`

5. **Configure Environment Variables** Create a `.env` file in the root directory with the following:

   makefile

   Copy code

   `EMAIL_HOST=[smtp.example.com](http://smtp.example.com)

   EMAIL_PORT=587

   [EMAIL_USER=your_email@example.com](mailto:EMAIL_USER=your_email@example.com)

   EMAIL_PASSWORD=your_password`

---

### Usage

#### Run the Flask Application

bash

`python app.py`

#### Access the Web Interface

Open your browser and navigate to:

[http://127.0.0.1](http://127.0.0.1)

#### Upload MP3 Files

1. Use the web interface to upload your MP3 file.
2. Wait for processing to complete.
3. Download the results or view the extracted data directly on the web interface.

#### Process Text Directly

- Paste the text into the provided text input box on the web interface.
- Extracted data will be categorized and displayed.

---

### File Structure

## bash
Copy code `ProSys/ │ ├── app/                # Backend code for the Flask application │   ├── __init__.py     # Flask app initialization │   ├── routes.py       # Flask endpoints for upload and processing │   ├── utils.py        # Utility functions for processing │ ├── templates/          # HTML files for the web interface │   ├── index.html      # Main upload and results page │ ├── static/             # Static assets like CSS and JS │   ├── styles.css      # Custom styling for the interface │ ├── uploads/            # Directory for uploaded MP3 files ├── results/            # Directory for processed results ├── requirements.txt    # Project dependencies ├── README.md           # This README file ├── .env                # Environment variables (ignored in .gitignore) ├── .gitignore          # Ignored files and directories └── app.py              # Main entry point for the Flask application`

### Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Speech-to-Text**: OpenAI Whisper
- **Data Processing**: Python's `re` for regex-based extraction
- **Email Notifications**: `smtplib`

---

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

### License

## This project is licensed under the MIT License. See `LICENSE` for more information.

### Contact

For any issues or feature requests, please contact the maintainer:

- **Email**: [hi@thrivi.org](mailto:hi@thrivi.org)
- **GitHub Issues**: [ProSys Issues](https://github.com/thrivi-org/ProSys/issues)

yaml

``---

### Steps to Use the README:

1. Save the content as a file named `README.md` in the root of your project.
2. Update the repository link, contact email, or any specifics that are unique to your project.

Would you like additional customization for this README?``

?descriptionFromFileType=function+toLocaleUpperCase()+{+[native+code]+}+File&mimeType=application/octet-stream&fileName=READ.ME.md&fileType=undefined&fileExtension=md
