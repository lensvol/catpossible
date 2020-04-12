import numpy as np
from detecto import utils
from detecto.core import Model


def cat_detector(path_to_photo):
    model = Model()
    image = utils.read_image(path_to_photo)

    try:
        results = model.predict_top(image)
    except ValueError:
        results = None

    if results is None:
        try:
            results = model.predict_top(image[..., ::-1] - np.zeros_like(image))
        except ValueError:
            return False

    labels, boxes, predictions = results
    return "cat" in labels
