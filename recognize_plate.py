import easyocr
import os
import cv2


def Recognize_plate(plate):

	#pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" #Enter your plate where tesseract-ocr is installed
	

	
	#for filename in glob.glob(os.plate.join(plate, '*.jpg')):
	with open(plate, 'r') as f:
	#img_pa='C:/Users/Asus/OneDrive/Desktop/juju/smrt goggles/codes/using web cam/download.png' 
		res_list=[]
		read=easyocr.Reader(['en'])
		result=read.readtext(plate)
		for i in range(len(result)):    
			p=[]
			p.append(result[i][1])
			res_list.append(''.join(i for i in p))
		print(res_list)

