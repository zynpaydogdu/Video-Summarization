import os
import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline
from googletrans import Translator
import whisper

def mp4_to_mp3(mp4_path):
    try:
        audio_path = mp4_path.replace(".mp4", ".mp3")
        os.system(f"ffmpeg -i \"{mp4_path}\" -vn -acodec mp3 \"{audio_path}\"")
        return audio_path
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while converting from MP4 to MP3: {e}")
        return None

def audio_to_text(mp3_path):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(mp3_path)
        return result["text"]
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while converting the audio file to text: {e}")
        return ""

def summarize_text(input_text):
    try:
        summarizer = pipeline("summarization")
        max_token_length = 1000  
        chunks = [input_text[i:i + max_token_length] for i in range(0, len(input_text), max_token_length)]
        summaries = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for chunk in chunks]
        return " ".join(summaries)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while summarizing: {e}")
        return ""

def translate_to_turkish(input_text):
    try:
        translator = Translator()
        max_length = 4000  
        chunks = [input_text[i:i + max_length] for i in range(0, len(input_text), max_length)]
        
        translated_chunks = []
        for chunk in chunks:
            translation = translator.translate(chunk, src="en", dest="tr")
            if translation and translation.text:
                translated_chunks.append(translation.text)
            else:
                translated_chunks.append("")
        return " ".join(translated_chunks)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during translation: {e}")
        return ""

def process_file():
    try:
        mp4_file = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
        if not mp4_file:
            return

        mp3_file = mp4_to_mp3(mp4_file)
        if not mp3_file:
            return

        transcript = audio_to_text(mp3_file)
        if not transcript:
            return

        summary = summarize_text(transcript)
        if not summary:
            return

        translated_summary = translate_to_turkish(summary)
        if not translated_summary:
            return

        save_text_to_file(summary, "summary.txt")
        save_text_to_file(translated_summary, "summary_tr.txt")

        display_summaries()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during the operation: {e}")

def display_summaries():
    try:
        with open("summary.txt", "r", encoding="utf-8") as f:
            english_summary = f.read()

        with open("summary_tr.txt", "r", encoding="utf-8") as f:
            turkish_summary = f.read()

        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "English Summary:\n")
        text_output.insert(tk.END, english_summary + "\n\n")
        text_output.insert(tk.END, "Turkish Summary:\n")
        text_output.insert(tk.END, turkish_summary)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while viewing summaries: {e}")

def save_text_to_file(text, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while in text members: {e}")

window = tk.Tk()
window.title("Video Summarization")
window.geometry("800x600")

tk.Label(window, text="Video Summarization", font=("Arial", 16)).pack(pady=10)
process_button = tk.Button(window, text="Upload Video", command=process_file, bg="pink", fg="white", font=("Arial", 12))
process_button.pack(pady=20)

tk.Label(window, text="Result:", font=("Arial", 14)).pack(pady=5)
text_output = tk.Text(window, height=20, width=80, wrap="word", font=("Arial", 12))
text_output.pack(pady=10)

window.mainloop()