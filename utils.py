import cv2
import matplotlib.pyplot as plt
import numpy as np
import PIL
import pandas as pd
from IPython.display import display, HTML


def imshow(img):
    ''' imshow function courtesy of our lab notebooks '''

    img = img.clip(0, 255).astype("uint8")
    if img.ndim == 3:
        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    display(PIL.Image.fromarray(img))

