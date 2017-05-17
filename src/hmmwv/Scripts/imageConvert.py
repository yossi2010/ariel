from numpy import genfromtxt
my_data = genfromtxt('my_file.csv', delimiter=',')
import cv2
cv2.imwrite("output.png", my_data)