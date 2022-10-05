from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open(input("Paste the file path for the image you want to get the text from: "))
imgtext = pytesseract.image_to_string(img)
name = input("enter a file name: ")
filename = name + ".txt"
with open(filename, "w") as textfile:
    textfile.write(imgtext)
