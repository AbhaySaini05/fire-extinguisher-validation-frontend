import cv2
from PIL import Image


def load_and_preprocess_image(image_path):

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"Could not read image: {image_path}")

    img = cv2.resize(img, (1024, 1024))

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(rgb)

    return pil_image


def preprocess_for_ocr(image_path):

    img = cv2.imread(image_path)

    img = cv2.resize(img, (1024, 1024))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.threshold(
        blur,
        150,
        255,
        cv2.THRESH_BINARY
    )[1]

    rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    pil_image = Image.fromarray(rgb)

    return pil_image


def check_blur(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    return variance