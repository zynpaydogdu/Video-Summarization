# Video Summarization Tool

This project provides a tool for summarizing videos by converting them into text, summarizing the text, and translating it into Turkish. The process uses state-of-the-art machine learning models, including OpenAI Whisper for transcription and the Transformers library for summarization.

## Features

- Convert MP4 video files to MP3 audio files.
- Transcribe audio files into text using Whisper.
- Summarize transcribed text using the Transformers library.
- Translate the summarized text into Turkish using Google Translate.
- Display and save both English and Turkish summaries.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or later
- Virtual environment set up (recommended)
- Required Python libraries

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Use the GUI to upload an MP4 video file.

3. The tool will:
   - Convert the video to audio (MP3).
   - Transcribe the audio to text.
   - Summarize the text.
   - Translate the summary into Turkish.

4. The English and Turkish summaries will be displayed in the GUI and saved as `summary.txt` and `summary_tr.txt`, respectively.

## Notes

- This project is designed to run in a Python virtual environment.
- Ensure you have `ffmpeg` installed and available in your system's PATH for audio conversion.
- Internet access is required for Google Translate and the Hugging Face API.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Google Translate API](https://pypi.org/project/googletrans/)
