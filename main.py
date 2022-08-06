from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(pdf_path):

    if Path(pdf_path).is_file() and Path(pdf_path).suffix=='.pdf':

        print('Processing...')

        with pdfplumber.PDF(open(file=pdf_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')

        mp3 = gTTS(text=text)
        mp3_name = Path(pdf_path).stem
        mp3.save(f'{mp3_name}.mp3')

        return f'{mp3_name}.mp3 saved succesfully!'

    else:
        return 'File NOT exist'

def main():
    pdf_patch = input("Enter a pdf's path (only eng): \n")
    print(pdf_to_mp3(pdf_patch))

if __name__ == '__main__':
    main()