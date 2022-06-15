#!/usr/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt


def adjust_gamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)

while 1 == 1:
  img = cv2.imread('./imagem.jpg')
  img2 = cv2.imread('./imagem2.jpg')

  img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)
  img2 = cv2.resize(img2, dsize=(0, 0), fx=0.5, fy=0.5)

  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  img_gray = adjust_gamma(img_gray, gamma=0.05)
  img2_gray = adjust_gamma(img2_gray, gamma=3)

  vis = cv2.vconcat([img_gray, img2_gray])

  plt.imshow(vis, cmap='gray')
  plt.show()

  key = cv2.waitKey(20)
  if key == 27:
      break

cv2.destroyWindow("output")