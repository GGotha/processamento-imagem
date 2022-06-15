#!/usr/bin/python

from black import out
import cv2
from matplotlib.pyplot import axis
import numpy as np
from matplotlib import pyplot as plt

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

while 1 == 1:
  img = cv2.imread('./imagem.jpg')
  img2 = cv2.imread('./imagem2.jpg')

  img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)
  img2 = cv2.resize(img2, dsize=(0, 0), fx=0.5, fy=0.5)

  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  vis = cv2.vconcat([img_gray, img2_gray])

  plt.imshow(vis, cmap="gray")
  plt.show()

  key = cv2.waitKey(20)
  if key == 27:
      break

cv2.destroyWindow("output")