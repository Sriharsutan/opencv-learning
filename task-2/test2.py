import cv2
import numpy as np

def refine_box(thresh_raw, x, y, w, h):
    roi = thresh_raw[y:y+h, x:x+w]

    ys, xs = np.where(roi > 0)

    if len(xs) == 0 or len(ys) == 0:
        return x, y, w, h

    x_min = xs.min()
    x_max = xs.max()
    y_min = ys.min()
    y_max = ys.max()

    pad = 2
    x_min = max(0, x_min - pad)
    y_min = max(0, y_min - pad)
    x_max = min(roi.shape[1] - 1, x_max + pad)
    y_max = min(roi.shape[0] - 1, y_max + pad)

    new_x = x + x_min
    new_y = y + y_min
    new_w = x_max - x_min + 1
    new_h = y_max - y_min + 1

    return new_x, new_y, new_w, new_h


def detect_text_lines(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    thresh_raw = thresh.copy()
    cv2.imwrite('1_thresh_raw.jpg', thresh_raw)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 6))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('2_thresh_cleaned.jpg', thresh)

    line_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 3))
    detected_lines = cv2.dilate(thresh, line_kernel, iterations=2)
    cv2.imwrite('3_detected_lines.jpg', detected_lines)

    cnts, _ = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imwrite('4_contours.jpg', detected_lines)

    colors = [(0, 0, 255), (255, 0, 25), (0, 0, 0), (255, 0, 0)]

    total_boxes = {}
    id = 0
    for i, c in enumerate(cnts):
        x, y, w, h = cv2.boundingRect(c)

        if w > 140 and h > 5 and h < 50:
            rx, ry, rw, rh = refine_box(thresh_raw, x, y, w, h)
            cv2.rectangle(img,(rx, ry),(rx + rw, ry + rh),colors[i % len(colors)],2,)
            total_boxes[id] = (int(rx), int(ry), int(rw), int(rh))
            id += 1

    cv2.imwrite("output_with_boxes.jpg", img)
    #print("Total boxes detected:", len(total_boxes))

detect_text_lines("output_large_fonts_only.jpg")