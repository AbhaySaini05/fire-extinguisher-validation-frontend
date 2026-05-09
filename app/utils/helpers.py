import os

from app.utils.preprocess import load_and_preprocess_image


def load_images_from_folder(folder_path):

    images = []

    valid_extensions = [".jpg", ".jpeg", ".png"]

    for file in os.listdir(folder_path):

        if any(file.lower().endswith(ext) for ext in valid_extensions):

            path = os.path.join(folder_path, file)

            img = load_and_preprocess_image(path)

            images.append(img)

    return images