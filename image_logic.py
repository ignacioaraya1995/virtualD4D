import requests
from data.vars import *
from PIL import Image
from io import BytesIO
import numpy as np

def download_street_view_image(property, googlemaps_api_key, size='1200x1200'):
    address = f"{property.street_address}, {property.city}, {property.state} {property.zipcode}, USA"
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    image_path = f"images/{property.folio}.jpg"
    params = {
        'size': size,
        'location': address,
        'key': googlemaps_api_key
    }
    error_image_path = 'images/error.jpg'  # Path to the error.jpg file
    try:
        response = requests.get(base_url, params=params, stream=True)
        if response.status_code == 200:
            img_bytes = response.content
            if not images_are_same(error_image_path, img_bytes):
                with open(image_path, 'wb') as f:
                    f.write(img_bytes)

                property.image_path = image_path
                return True
            else:
                print("Downloaded image is the same as error.jpg. Skipping save.")
                return False
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def images_are_same(img1_path, img2_bytes):
    """Check if the given image file and image bytes are the same."""
    try:
        with open(img1_path, 'rb') as f:
            img1 = Image.open(f)
            img1_array = np.array(img1)

        img2 = Image.open(BytesIO(img2_bytes))
        img2_array = np.array(img2)

        return np.array_equal(img1_array, img2_array)
    except Exception as e:
        print(f"An error occurred while comparing images: {e}")
        # If there's an error in comparison, assume images are not the same.
        return False
