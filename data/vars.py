googlemaps_api_key = 'AIzaSyAm9nhbKjQdjrdY_WRWuzqQxLQS46y97Fk'
openai_api_key = "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"
import_path = 'data/marketing list'
excel_export_path = 'data/enriched_properties.xlsx'
prompt = """
Carefully analyze the provided image to evaluate the property's condition, focusing solely on 
observable physical indicators. Check for signs that suggest the level of upkeep, 
such as the condition of the roof, exterior walls, windows, and landscaping. 

Determine the property's state based on these visual cues, rating it on a scale 
from 0 (best condition) to 5 (needs extensive repairs). If the image does not feature a property, classify the outcome as 'Empty'. Remember, the only required output is a condition rating between 0 and 5, or 'Empty' if applicable, based on assessments up to April 2023. Do not provide any explanations or assumptions beyond the visual evidence presented in the image.
"""