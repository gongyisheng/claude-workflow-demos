"""Computer vision dependencies.

One function per dependency: opencv-python (cv2), scikit-image (skimage),
pillow (PIL).
"""

import numpy as np
import cv2
import skimage
from skimage.transform import resize
from PIL import Image


def to_grayscale(image: "np.ndarray") -> "np.ndarray":
    """cv2: convert an RGB image array to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def resize_image(image: "np.ndarray", shape=(32, 32)) -> "np.ndarray":
    """skimage: resize an image array."""
    return resize(image, shape)


def new_blank_image(size=(64, 64)) -> "Image.Image":
    """pillow: create a new blank RGB image."""
    return Image.new("RGB", size, color=(255, 255, 255))


def random_rgb_image(size=(64, 64)) -> "np.ndarray":
    """Helper: produce a random RGB image array for the functions above."""
    return (np.random.rand(size[0], size[1], 3) * 255).astype("uint8")
