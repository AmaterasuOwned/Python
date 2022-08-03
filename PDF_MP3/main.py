from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path="1.pdf", language="en"):
    """Превращаем файл из pdf в mp3."""
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        print(f"[+] Original file: {Path(file_path).name}")
        print("[+] Working...")

        text = "".join(pages)
        text = text.replace("\n", "")

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")

        return f"[+] Job done {file_name}.mp3"
    else:
        return NotImplementedError


def main():
    """Главная функция"""
    tprint("PDF--TO--MP3", font="bulbhead")
    file_path = input("\n Enter a file path: ")
    language = input("\n Enter a language, 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == "__main__":
    main()
