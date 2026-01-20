# import cv2 as cv
# import xml.etree.ElementTree as ET
# from collections import defaultdict

# class Token:
#     def __init__(self, text, x, y, width, height, fsize):
#         self.text = text
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.font_size = fsize    

# class Parser:
#     def __init__(self, xml_file):
#         self.xml_file = xml_file

#     def parse_xml(self):
#         self.tree = ET.parse(self.xml_file)
#         self.root = self.tree.getroot()

#     def extract_tokens(self):
#         tokens = []
#         for token in self.root.iter('TOKEN'):
#             word = token.text.strip() if token.text else ''
#             x = int(token.attrib['x'])
#             y = int(token.attrib['y'])
#             width = int(token.attrib['width'])
#             height = int(token.attrib['height'])
#             fsize = int(token.attrib.get('font-size'))

#             tokens.append(Token(word, x, y, width, height, fsize))
#         return tokens
    
# def rescaleImg(img, scale=0.2):
#     height = int(img.shape[0] * scale)
#     width = int(img.shape[1] * scale)
#     dimensions = (width, height)
#     return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

# img = cv.imread('output.jpg')
# parser = Parser('output.xml')
# parser.parse_xml()
# tokens = parser.extract_tokens()


# rows = defaultdict(list)
# for token in tokens:
#     row_key = token.y // 80

#     rows[row_key].append(token)

# final_lines = []

# for row in rows.values():
#     row.sort(key=lambda t: t.x)

#     current = [row[0]]

#     for prev, cur in zip(row, row[1:]):
#         gap = cur.x - (prev.x + prev.width)

#         if gap > 35:
#             final_lines.append(current)
#             current = [cur]
#         else:
#             current.append(cur)

#     final_lines.append(current)


# colors = [(0,0,0), (0, 0, 255), (0, 0, 255), (100, 155, 0), (255, 0, 25), (0, 25, 25)]

# for i, line in enumerate(final_lines):
#     x1 = min(t.x for t in line)
#     y1 = min(t.y for t in line)
#     x2 = max((t.x + t.width) for t in line)
#     y2 = max((t.y + t.height) for t in line)

#     cv.rectangle(img, (x1, y1), (x2, y2), colors[i % len(colors)], 2)


# # for i in list(lines.items())[:10]:
# #     print(i)
# # print(max(list(lines.keys())))
# # for i in final_lines[:10]:
# #     print([t.text for t in i])


# for i in list(rows.items())[:10]:
#     print([t.text for t in i[1]])

# img = rescaleImg(img, scale=0.2)
# cv.imshow('Image with Line Boxes', img)
# cv.imwrite('sample_output.jpg', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # import cv2 as cv
# # import xml.etree.ElementTree as ET
# # from collections import defaultdict

# # class Token:
# #     def __init__(self, text, x, y, width, height, fsize):
# #         self.text = text
# #         self.x = x
# #         self.y = y
# #         self.width = width
# #         self.height = height
# #         self.font_size = fsize

# # class Parser:
# #     def __init__(self, xml_file):
# #         self.xml_file = xml_file

# #     def parse_xml(self):
# #         self.tree = ET.parse(self.xml_file)
# #         self.root = self.tree.getroot()

# #     def extract_tokens(self):
# #         tokens = []
# #         for token in self.root.iter('TOKEN'):
# #             word = token.text.strip() if token.text else ''
# #             x = int(token.attrib['x'])
# #             y = int(token.attrib['y'])
# #             width = int(token.attrib['width'])
# #             height = int(token.attrib['height'])
# #             fsize = int(token.attrib.get('font-size'))

# #             tokens.append(Token(word, x, y, width, height, fsize))
# #         return tokens

# # img = cv.imread('output.jpg')
# # parser = Parser('output.xml')
# # parser.parse_xml()
# # tokens = parser.extract_tokens()

# # all_fonts = []
# # for token in tokens:
# #     x = token.font_size
# #     if x not in all_fonts:
# #         all_fonts.append(x)

# # all_fonts.sort()
# # print("All font sizes in the document:", all_fonts)


# import cv2
# import numpy as np

# def detect_all_text_lines(image_path):
#     img = cv2.imread(image_path)
#     if img is None:
#         print("Error: Image not found.")
#         return
    
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # 2. Binary Thresholding (Otsu's method)
#     # Invert so text is white and background is black
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#     # 3. Clean up noise (Morph Open)
#     # Keeps text intact but removes small noise dots
#     clean_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#     thresh_cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, clean_kernel)

#     # --- PASS 1: DETECT SMALL/BODY TEXT ---
#     # Kernel: Wide enough to connect small letters (20), thin (1) to prevent vertical merging
#     kernel_small = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
#     dilated_small = cv2.dilate(thresh_cleaned, kernel_small, iterations=1)
    
#     cnts_small, _ = cv2.findContours(dilated_small, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # --- PASS 2: DETECT LARGE/HEADLINE TEXT ---
#     # Kernel: Much wider (100) to bridge big gaps in titles. 
#     # Taller (5) to handle large font stroke thickness and accents.
#     kernel_large = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 5))
#     dilated_large = cv2.dilate(thresh_cleaned, kernel_large, iterations=1)
    
#     cnts_large, _ = cv2.findContours(dilated_large, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     final_boxes = []

#     # Process Small Contours
#     for c in cnts_small:
#         x, y, w, h = cv2.boundingRect(c)
#         # Filter for body text height (approx 5 to 50 pixels)
#         if w > 10 and 5 < h < 50:
#             final_boxes.append((x, y, w, h))

#     # Process Large Contours
#     for c in cnts_large:
#         x, y, w, h = cv2.boundingRect(c)
#         # Filter for headline height (approx 55 to 200 pixels)
#         # We also limit max height (200) to avoid drawing a box around a whole merged paragraph
#         if w > 50 and 50 <= h < 300:
#             final_boxes.append((x, y, w, h))

#     # 4. Draw all valid boxes
#     # Using a single color (Green) for all, or you can alternate
#     for (x, y, w, h) in final_boxes:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     cv2.imshow('Detected Lines (Small & Large)', img)
#     cv2.imwrite('output_all_lines.jpg', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# detect_all_text_lines('output.jpg')


import cv2 as cv
import xml.etree.ElementTree as ET
from collections import defaultdict

class Token:
    def __init__(self, text, x, y, width, height, fsize):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = fsize

class Parser:
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def parse_xml(self):
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    def extract_tokens(self):
        tokens = []
        for token in self.root.iter('TOKEN'):
            word = token.text.strip() if token.text else ''
            x = int(token.attrib['x'])
            y = int(token.attrib['y'])
            width = int(token.attrib['width'])
            height = int(token.attrib['height'])
            fsize = int(token.attrib.get('font-size', 0))

            tokens.append(Token(word, x, y, width, height, fsize))
        return tokens
    
def rescaleImg(img, scale=0.2):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('output.jpg')
parser = Parser('output.xml')
parser.parse_xml()
tokens = parser.extract_tokens()

TARGET_FONTS = (14, 15, 17, 19, 20, 21, 22, 24, 42, 58)

rows = defaultdict(list)
for token in tokens:
    if token.font_size in TARGET_FONTS:
        if token.font_size in (24, 42, 58):
            row_key = token.y // 70
        elif token.font_size == 21:
            row_key = token.y // 100
        elif token.font_size == 10:
            row_key = token.y // 100
        else:
            row_key = token.y // 80
            
        rows[row_key].append(token)

final_lines = []
FONT_GAP_THRESHOLDS = {
    10: 40,
    22: 35,
    24: 37,
    42: 40,
    58: 40      
}
DEFAULT_GAP = 40

for row in rows.values():
    if not row: continue
    
    row.sort(key=lambda t: t.x)
    current = [row[0]]

    for prev, cur in zip(row, row[1:]):
        gap = cur.x - (prev.x + prev.width)
        gap_thresh = FONT_GAP_THRESHOLDS.get(prev.font_size, DEFAULT_GAP)

        if gap > gap_thresh:
            final_lines.append(current)
            current = [cur]
        else:
            current.append(cur)

    final_lines.append(current)

final_lines = []
for row in rows.values():
    if not row: continue
    row.sort(key=lambda t: t.x)
    current = [row[0]]
    for i in range(1, len(row)):
        prev = row[i-1]
        cur = row[i]
        gap = cur.x - (prev.x + prev.width)
        gap_thresh = FONT_GAP_THRESHOLDS.get(prev.font_size, DEFAULT_GAP)
        
        if gap > gap_thresh:
            final_lines.append(current)
            current = [cur]
        else:
            current.append(cur)
    final_lines.append(current)

colors = [(0, 0, 255), (255, 0, 25), (0, 25, 25)]

for i, line in enumerate(final_lines):
    if not line: continue
    x1 = min(t.x for t in line)
    y1 = min(t.y for t in line)
    x2 = max((t.x + t.width) for t in line)
    y2 = max((t.y + t.height) for t in line)

    cv.rectangle(img, (x1, y1), (x2, y2), colors[i % len(colors)], 2)

cv.imwrite('output_large_fonts_only.jpg', img)

img_display = rescaleImg(img, scale=0.2)
cv.imshow('Large Fonts Only', img_display)
cv.waitKey(0)
cv.destroyAllWindows()