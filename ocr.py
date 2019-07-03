# USAGE
# set path=C:\Program Files\Tesseract-OCR;C:\Users\Amey Gondhalekar\PycharmProjects\FirstLook\venv\Scripts
# python ocr.py --image images/imgoo0.jpg         ----With preprocessing


from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re

# parsing the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# loading & converting to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)

print("Results: \n**************")
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
# print(list(filter(bool, re.split(':|\n',text))))
# print(re.split(':|\n',text))

# show the output images
# cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
