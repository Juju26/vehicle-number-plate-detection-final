import cv2
import imutils
import numpy as np 
import os
import detect_plate
import recognize_plate
import time
import shutil

def Main(image_name,cur_path):
	
	image = cv2.imread(image_name)

	plate = detect_plate.Detect_plate(image)
	plate_path=cur_path+'/imgs/13 i .png'
	time.sleep(5)
	recognize_plate.Recognize_plate(plate_path)
	shutil.rmtree(plate)


if __name__ == '__main__':

	print("please make sure the image is in the same folder in which the file main.py is/n")

	image_name = input("enter video path with extension: ")
	cur_path=os.getcwd()
	imag='E:/ANPR john/vehicle-number-plate-detection-master/vehicle-number-plate-detection-master/imgs/18.jpeg'
	Main(imag,cur_path)
	

	
