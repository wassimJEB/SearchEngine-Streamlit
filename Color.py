# import the necessary packages
import numpy as np
import cv2
import imutils
class ColorDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins
	def describe(self, image):
		def describe(self, image):
			features = []
			hist = cv2.calcHist([image], [0, 1, 2], None, self.bins, [0, 180, 0, 256, 0, 256])
			hist = cv2.normalize(hist, hist).flatten()
			features.extend(hist)
			return features


