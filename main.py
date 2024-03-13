from pypdf import PdfReader
from gtts import gTTS
from tqdm import tqdm

pdf_file = input("Seslendirmek istediğiniz Pdf dosyasının yolunu girin: ")
sound_name = input("Kayıt adı girin: ")
reader = PdfReader(pdf_file)
text=""
total_pages = len(reader.pages)

for page_no in tqdm(range(total_pages), desc="Pdf okunuyor..."):
    page = reader.pages[page_no]
    text +=page.extract_text()
sound = gTTS(text=text, lang='tr',slow=False)
print("Ses kayıt ediliyor...")
sound.save('%s.mp3'%sound_name)