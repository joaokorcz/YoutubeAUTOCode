from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString
from html.parser import HTMLParser
import os
import time
import pyscreenshot as ImageGrab
import pytesseract
from PIL import Image
from PIL import ImageChops
import PIL.ImageOps

time.sleep(2)

imM = ImageGrab.grab(bbox=(133, 40, 400, 70))
imM.save('print.png')
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"
#url = 'https://www.'
#url += pytesseract.image_to_string(imM)
url = "https://www.youtube.com/watch?v=7tyUYHbX_0M"
print("URL> ",url)
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

yt = soup.findAll('p')
v_lines = []
for p in yt:
    if "Faça login para reportar conteúdo inadequado." not in p.text and "Carregando" not in p.text and "Processando..." not in p.text:
        p = str(p)
        for i in range(len(p)):
            if p[i]=='>':
                a = i+1
                line = ''
                if a<len(p):
                    while p[a]!='<':
                        line+=p[a]
                        a+=1
                if line != '':
                    v_lines.append(line)

for i in range(len(v_lines)):
    print(v_lines[i])
