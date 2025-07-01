
---

## answer-sheet-scanner/answer_sheet_scanner.py

```python
import cv2
import numpy as np

def main():
    image = cv2.imread('answer_sheet.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bubbles = []
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        area = cv2.contourArea(cnt)
        if 20 < w < 50 and 0.8 < aspect_ratio < 1.2 and area > 400:
            bubbles.append(cnt)

    bubbles = sorted(bubbles, key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))

    answers = []
    for i, bubble in enumerate(bubbles):
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [bubble], -1, 255, -1)
        total = cv2.countNonZero(mask)
        filled = cv2.countNonZero(cv2.bitwise_and(thresh, thresh, mask=mask))
        fill_ratio = filled / float(total)

        if fill_ratio > 0.5:
            answers.append((i + 1, "Filled"))
        else:
            answers.append((i + 1, "Empty"))

    for q_num, state in answers:
        print(f"Bubble {q_num}: {state}")

if __name__ == "__main__":
    main()
