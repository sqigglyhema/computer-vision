import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread(r"C:\Users\itsme\Downloads\tree.jpeg")
cv2.imshow("original image",img)
def plot_histogram(img, title, mask=None):
   channels = cv2.split(img)
   colors = ("b", "g", "r")
   plt.title(title)
   plt.xlabel("Bins")
   plt.ylabel("# of Pixels")
   for (channel, color) in zip(channels, colors):
      hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
      plt.plot(hist, color=color)
      plt.xlim([0, 256])
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (160, 130), (410, 290), 255, -1)
masked = cv2.bitwise_and(img, img, mask=mask)
plot_histogram(img, "Histogram for Masked Image", mask=mask)
plt.show()
cv2.imshow("Mask", mask)
cv2.imshow("Mask Image", masked)
cv2.waitKey(0)
