from data.vars import *
from image_logic import *
from ai_logic import *
from utils import *
from tqdm import tqdm
import os

MAX = 5  # Maximum number of properties to process

if __name__ == '__main__':
    properties = read_properties_from_multiple_excels(import_path)
    for i, property in enumerate(tqdm(properties, desc="Processing properties")):
        if i >= MAX:
            break  # Stop the loop after processing MAX properties
        
        image_path = f"images/{property.folio}.jpg"
        property.image_path = image_path
        
        if not os.path.exists(image_path):  # Check if the image already exists
            try:
                download_street_view_image(property, googlemaps_api_key)
            except Exception as e:
                print(f"Error with property folio: {property.folio}, Error: {str(e)}")
        
        if os.path.exists(image_path):  # Check again in case the download failed
            try:
                analyze_image(property, prompt, openai_api_key)
            except Exception as e:
                print(f"Error analyzing image for property folio: {property.folio}, Error: {str(e)}")

    export_enriched_properties(properties[:MAX], excel_export_path)


