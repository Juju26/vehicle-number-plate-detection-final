video breaken down into frames ('olcar.mp4' --> 30 frames inside imgs folder)
suitable frames are selected for detection and recognition process 
Enhancement process is carried on the selected images(cropped image [temporary folder])
           
           > 1. Grayscale
           > 2. Bilateral filter
           > 3. Edge detection (canny)
           > 4. Finding all Contours
           > 5. Selecting top contours
           > 6.  Cropping number plate

cropped plate is send as a input for text detection