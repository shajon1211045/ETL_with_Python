import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    # Checking if the csv file is empty to handle such cases.
    if dataframe.empty:
        return pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])

    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    # Checking if the JSON file is empty to handle such cases.
    if dataframe.empty:
        return pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    # Checking if the XML file is empty to handle such cases.
    if len(root) == 0:
        return pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = car.find("year_of_manufacture").text
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe = pd.concat([dataframe, pd.DataFrame([{"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel}])], ignore_index=True)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])

    # process all csv files except "transformed_data.csv"
    for csvfile in glob.glob("datasource/*.csv"):
        if csvfile != "transformed_data.csv":
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("datasource/*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

    # process all xml files
    for xmlfile in glob.glob("datasource/*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

    return extracted_data

def transform(data):
    # Capitalize the car model name
    data['car_model'] = data.car_model.str.capitalize()

    # Rounding the fuel price up to two decimal points
    data['price'] = round(data.price, 2)

    return data

def load_data(target_file, transformed_data):
    if not transformed_data.empty:
        transformed_data.to_csv(target_file, index=False)

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')

# Log the initialization of the ETL process
log_progress("ETL Job Started")

# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data = extract()

# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_data(target_file, transformed_data)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")

