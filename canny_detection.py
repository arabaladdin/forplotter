#noise reduction
#gradient calculation
#non-maximum suppression
#double threshold
#edge tracking by hysteresis

#import photo
import numpy as np

def gaussian_kernel(size, sigma=1):
    size = int(size)
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 /(2.0 * np.pi * sigma**2)
