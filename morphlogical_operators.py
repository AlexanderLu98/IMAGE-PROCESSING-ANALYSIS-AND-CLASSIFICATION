"""
As stated in the README I misunderstood the questions so I have created functions that are supposed to work
"""
import numpy as np

#cv2.erode(image, kernel, iterations=1)
def erode(img, kernel, iterations=1):
    # Create an empty array to hold the output image
    out = np.zeros_like(img)
    # Get the kernel size
    size = kernel.shape[0]
    # Get the padding required for full convolution
    pad = size // 2

    for n in range(iterations):
        # Iterate over every pixel in the input image
        for i in range(pad, img.shape[0] - pad):
            for j in range(pad, img.shape[1] - pad):
                # Get the local neighborhood around the current pixel
                neighborhood = img[i - pad:i + pad + 1, j - pad:j + pad + 1]
                # Perform the erosion operation
                out[i, j] = np.min(neighborhood[kernel == 1])
        # Update the input image for the next iteration
        img = out.copy()

    return out

#cv2.dilate(img, kernel, iterations=1)
def dilate(img, kernel, iterations=1):
    # Create an empty array to hold the output image
    out = np.zeros_like(img)
    # Get the kernel size
    size = kernel.shape[0]
    # Get the padding required for full convolution
    pad = size // 2

    for n in range(iterations):
        # Iterate over every pixel in the input image
        for i in range(pad, img.shape[0] - pad):
            for j in range(pad, img.shape[1] - pad):
                # Get the local neighborhood around the current pixel
                neighborhood = img[i - pad:i + pad + 1, j - pad:j + pad + 1]
                # Perform the dilation operation
                out[i, j] = np.max(neighborhood[kernel == 1])
        # Update the input image for the next iteration
        img = out.copy()

    return out

#cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
def open(img, kernel):
    eroded = erode(img, kernel, 1)
    # Apply dilation to the eroded image
    opening = dilate(eroded, kernel, 1)
    # Return the dilated image
    return opening

#cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
def close(img, kernel):
    # Perform dilation
    dilation = dilate(img, kernel, 1)
    # Perform erosion
    closing = erode(dilation, kernel, 1)
    return closing
