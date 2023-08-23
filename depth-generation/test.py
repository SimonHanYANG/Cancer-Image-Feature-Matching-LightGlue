from skimage.feature import peak_local_max
from skimage.measure import label
from skimage.segmentation import watershed
from skimage.segmentation import mark_boundaries
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the image
image_path = 'data\\video_image\\frame0.jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
smoothed = cv2.GaussianBlur(gray, (15, 15), 0)

# Use Otsu's method to threshold the image
_, binary = cv2.threshold(smoothed, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Perform a series of dilations and erosions to remove any small blobs of noise from the image
binary = cv2.dilate(binary, None, iterations=2)
binary = cv2.erode(binary, None, iterations=1)

# Compute the exact Euclidean distance from every binary pixel to the nearest zero pixel and then find peaks in this distance map
distance_map = ndimage.distance_transform_edt(binary)
local_max = peak_local_max(distance_map, indices=False, min_distance=20, labels=binary)

# Perform a connected component analysis on the local peaks and use the Watershed algorithm to separate cells
markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
labels = watershed(-distance_map, markers, mask=binary)

# Iterate over the unique labels returned by the Watershed algorithm
segments = []
for label in np.unique(labels):
    if label == 0:
        continue

    # Create a mask for the segment
    mask = np.zeros(gray.shape, dtype='uint8')
    mask[labels == label] = 255
    segments.append(mask)

# Show the output image
for i, seg in enumerate(segments):
    fig, ax = plt.subplots()
    ax.imshow(mark_boundaries(image, seg))
    plt.title(f'Segment {i+1}')
    plt.show()