from pypdf import PdfReader
from gtts import gTTS

pdf_file = input("Seslendirmek istediğiniz Pdf dosyasının yolunu girin: ")
sound_name = input("Kayıt adı girin: ")
reader = PdfReader(pdf_file)
text=""
for page_no in range(len(reader.pages)):
    page = reader.pages[page_no]
    text +=page.extract_text()
sound = gTTS(text=text, lang='tr',slow=False)
sound.save('%s.mp3'%sound_name)