import easyocr
import os
import cv2


def Recognize_plate(plate):
	with open(plate, 'r') as f:
		res_list=[]
		read=easyocr.Reader(['en'])
		result=read.readtext(plate)
		for i in range(len(result)):    
			p=[]
			p.append(result[i][1])
			res_list.append(''.join(i for i in p))
		print(res_list)