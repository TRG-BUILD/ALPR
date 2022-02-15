# import the necessary packages
from skimage.segmentation import clear_border
import pytesseract
import numpy as np
import imutils
import cv2

class PyImageSearchANPR:
    def __init__(self, minAR=4, maxAR=5, debug=False):
	    # store the minimum and maximum rectangular aspect ratio
	    # values along with whether or not we are in debug mode
        self.minAR = minAR
        self.maxAR = maxAR
        self.debug = debug

    def debug_imshow(self, title, image, waitKey=False):
    		# check to see if we are in debug mode, and if so, show the
		# image with the supplied title
        if self.debug:
            cv2.imshow(title, image)

			# check to see if we should wait for a keypress
            if waitKey:
                cv2.waitKey(0)
                
    def locate_license_plate_candidates(self, gray, keep=5):
    		# perform a blackhat morphological operation that will allow
		# us to reveal dark regions (i.e., text) on light backgrounds
		# (i.e., the license plate itself)
        rectKern = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
        blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKern)
        self.debug_imshow("Blackhat", blackhat)