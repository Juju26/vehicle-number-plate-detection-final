import cv2
import imutils
import numpy as np 
import os
import detect_plate
import recognize_plate
import video_to_img
import time
import shutil

def Main(image_name,cur_path):
	
	image = cv2.imread(image_name)

	plate = detect_plate.Detect_plate(image)
	plate_path=cur_path+'/13 i .png'
	time.sleep(5)
	recognize_plate.Recognize_plate(plate_path)
	shutil.rmtree(plate)


if __name__ == '__main__':
	video_name = input("Enter video path with extension : ")
	video_to_img.frame_creator(video_name)
	cur_path=os.getcwd()
	imag=cur_path+'/imgs/18.jpeg'
	Main(imag,cur_path)