import cv2 as cv
import numpy as np
import xml.etree.ElementTree as ET

class Token:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class OCRParser:
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def parse_xml(self):
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    def extract_tokens(self):
        tokens = []
        for token in self.root.iter('TOKEN'):
            text = token.text.strip() if token.text else ''
            x = int(token.attrib['x'])
            y = int(token.attrib['y'])
            width = int(token.attrib['width'])
            height = int(token.attrib['height'])

            tokens.append(Token(text, x, y, width, height))
        return tokens

def rescaleImg(img, scale=0.2):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('sample_news_image.jpg')

parser = OCRParser('2010-09-28_01-00003A_ocrwrd.xml')
parser.parse_xml()
tokens = parser.extract_tokens()

for token in tokens:
    cv.rectangle(img, (token.x, token.y), (token.x + token.width, token.y + token.height), (255, 0, 0), 2)
    # cv.putText(img, token.text, (token.x, token.y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

img = rescaleImg(img, scale=0.2)
cv.imshow('Image with Boxes', img)
cv.imwrite('output.jpg', img)

cv.waitKey(0)
cv.destroyAllWindows()