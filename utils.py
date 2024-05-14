from property import Property
import pandas as pd
from typing import List
import os

def read_properties_from_multiple_excels(folder_path: str) -> List[Property]:
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]
    all_properties_df = pd.DataFrame()
    
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        all_properties_df = pd.concat([all_properties_df, df], ignore_index=True)
    
    properties = [Property(row['FOLIO'], row['ADDRESS'], row['CITY'], row['STATE'], row['ZIP']) for index, row in all_properties_df.iterrows()]
    return properties


def export_enriched_properties(properties_list, excel_export_path):
    properties_data = []
    for prop in properties_list:
        # Ensure AI Property Analysis is an integer, otherwise replace with an empty space
        try:
            ai_property_analysis = int(prop.ai_property_analysis)
        except (ValueError, TypeError):
            ai_property_analysis = ''

        properties_data.append({
            "FOLIO": prop.folio,
            "Street Address": prop.street_address,
            "City": prop.city,
            "State": prop.state,
            "ZIP": prop.zipcode,
            "Repair Urgency Level": ai_property_analysis
        })

    df = pd.DataFrame(properties_data)
    df.to_excel(excel_export_path, index=False)
    print("Enriched properties exported to excel successfully")
    return True