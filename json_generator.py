import json

def create_json_file(file_name, data):
    """
    Create a JSON file with the specified data.

    Parameters:
        file_name (str): The name of the JSON file to be created.
        data (dict): The data to be written to the JSON file.
    """
    try:
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON file '{file_name}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the JSON file: {e}")

# Example usage
default_format = {
    "default_Bed_count": 5,
    "default_Sex_count": 3,
    "default_Entries_count": 5,
    "default_table_rows_count": 5,

    "each_sex_value_names": {"Sex_1_name":"Male" ,"Sex_2_name":"Female","Sex_3_name":"Other"},

    "each_entry_layout":{
                          "entry_1":{"title":"Antimicrobials","title_Description":"Some_details_about_antimicrobials"},
                          "entry_2":{"title":"Feeds","title_Description":"Some_details_about_feeds"},
                          },

    "each_table_row_layout":{

                          "row_1":{"row_header_name":"Date","row_header_description":"some_date"},
                          "row_2":{"row_header_name":"Time","row_header_description":"some_time"},
                          "row_3":{"row_header_name":"Weight","row_header_description":"some_weight"},
                          "row4":{"row_header_name":"Height","row_header_description":"some_Height"},
                          "row5":{"row_header_name":"IVF","row_header_description":"some_IVF"},

                            },

}



file_name = "Default_format.json"
create_json_file(file_name, default_format)
