import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

detail = [(np.empty((100, 2, 2)), np.empty((100, 2, 2))) for _ in range(360)]


for i in range(len(detail)):
    # Create new tuples with arrays that have random values
    detail = [(np.random.rand(100, 2, 2), np.random.rand(100, 2, 2) )for _ in range(360)]
    


class Detail:
    def __init__(self, id, arr):
        self.id = id
        self.arr = arr
    
    def draw(self, x=0, y=0, angle=0, space=0):
        # Calculate the width and height of the combined array
        combined_arr = np.concatenate(self.arr)
        width = combined_arr.shape[1] / combined_arr.shape[0]
        height = 2
        
        # Adjust the x and y coordinates to avoid overlap
        x = x + space * self.id
        y = y + space * self.id
        
        # Rotate and plot the array
        rotated_arr = ndimage.rotate(combined_arr, angle, reshape=False)
        plt.imshow(rotated_arr, extent=[x, x+width, y, y+height])
        plt.show()


detail1 = Detail(1, [np.ones((5,5)), np.zeros((5,5))])
detail2 = Detail(2, [np.ones((5,5)), np.zeros((5,5))])

detail1.draw(x=5, y=10, angle=90, space=0.1)
detail2.draw(x=1, y=6, angle=45, space=0.1)