import whisper
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def mp3_to_text(mp3_file):
    """
    Convert MP3 audio to text using OpenAI Whisper.

    Parameters:
    mp3_file (str): Path to the MP3 file to be transcribed.

    Returns:
    str: Transcribed text from the MP3 file.
    """
    try:
        logging.info(f"Loading Whisper model...")
        model = whisper.load_model("base")  # Use "small", "medium", or "large" for better accuracy
        logging.info(f"Transcribing audio file: {mp3_file}")
        result = model.transcribe(mp3_file)
        logging.info(f"Transcription successful.")
        return result['text']
    except Exception as e:
        logging.error(f"Error during transcription: {e}")
        return "An error occurred during transcription."