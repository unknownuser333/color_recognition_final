import keras
import numpy as np


colors_map = {
    "black": np.array([0.] * 0 + [1.] + [0.] * 10),
    "blue": np.array([0.] * 1 + [1.] + [0.] * 9),
    "brown": np.array([0.] * 2 + [1.] + [0.] * 8),
    "green": np.array([0.] * 3 + [1.] + [0.] * 7),
    "grey": np.array([0.] * 4 + [1.] + [0.] * 6),
    "orange": np.array([0.] * 5 + [1.] + [0.] * 5),
    "pink": np.array([0.] * 6 + [1.] + [0.] * 4),
    "red": np.array([0.] * 7 + [1.] + [0.] * 3),
    "violet": np.array([0.] * 8 + [1.] + [0.] * 2),
    "white": np.array([0.] * 9 + [1.] + [0.] * 1),
    "yellow": np.array([0.] * 10 + [1.] + [0.] * 0)
}


def image_preprocessing(image_path):
    image = keras.preprocessing.image.load_img(path=image_path, target_size=(64, 64))
    image_array = keras.preprocessing.image.img_to_array(img=image)

    return image_array[np.newaxis]
    
