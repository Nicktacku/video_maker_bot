from PIL import Image
import os
from matplotlib import pyplot as plt
import numpy as np

def resize_img(r_id):
    for image in os.listdir(f"screenshots/{r_id}"):
        im = Image.open(f"screenshots/{r_id}/{image}")

        width, height = im.size

        ratio = height/width

        new_height = 1000 * ratio

        im1 = im.resize((1000, int(new_height)))
        im1.save(f"screenshots/{r_id}/{image}")