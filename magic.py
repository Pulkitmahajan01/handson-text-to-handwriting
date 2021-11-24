# imports
from PIL import Image
import pdfplumber
import docx


def writee(char):
    global x, y, bg
    if char == '\n':
        x = 75
        y += 200
    else:
        char.lower()
        cases = Image.open(
            "myfont/%s.png" % char)
        bg.paste(cases, (x, y))
        size = cases.width
        x += size
        del cases


def letterwrite(word, sizeOfSheet, allowedChars):
    global x, y
    if x > sizeOfSheet - 95*(len(word)):
        x = 75
        y += 200
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)


def worddd(Input, sizeOfSheet, allowedChars):
    wordlist = Input.split(' ')
    for i in wordlist:
        letterwrite(i, sizeOfSheet, allowedChars)
        writee('space')


def magicWand(filePath, extension):
    #print("File path: ", filePath)
    #print("Extension: ", extension)
    global bg, x, y
    bg = Image.open("myfont/bg.png")
    sizeOfSheet = bg.width
    x, y = 75, 0
    allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890\n'

    data = ""

    if extension == "txt":
        with open(filePath, 'r') as file:
            dataT = file.read()
            data += dataT
        file.close()
    elif extension == "pdf":
        with pdfplumber.open(r''+filePath) as file:
            for page in file.pages:
                dataTemp = page.extract_text()
                data += dataTemp
        file.close()
    elif extension == 'docx':
        from docx import Document
        doc = Document(filePath)
        fText = []
        for para in doc.paragraphs:
            fText.append(para.text)
            data = '\n'.join(fText)
    else:
        print("Extension not supported!!")

    # print(data)
    l = len(data)
    nn = len(data)//600
    chunks, chunk_size = len(data), len(data)//(nn+1)
    p = [data[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

    for i in range(0, len(p)):
        worddd(p[i], sizeOfSheet, allowedChars)
        writee('\n')
        bg.save('%dout.png' % i)
        bg1 = Image.open(
            "myfont/bg.png")
        bg = bg1
        x = 75
        y = 0
