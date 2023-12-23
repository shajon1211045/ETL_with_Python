# ETL with Python

This project demonstrates a simple ETL (Extract, Transform, Load) process implemented in Python. The script extracts data from CSV, JSON, and XML files, transforms the data, and saves the transformed data to a CSV file.

## Project Structure

The project is organized as follows:

1. `ETL.py`: The main Python script that performs the ETL process.
2. `datasource/`: The directory containing CSV, JSON, and XML files with sample data.
3. `log_file.txt`: The log file where progress and timestamped messages are recorded.
4. `transformed_data.csv`: The target CSV file where the transformed data is saved.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shajon1211045/ETL_with_Python.git
   cd ETL_with_Python

2. **Run the ETL Script**
   ```bash
   python ETL.py

3.**Check the Output:**
- Transformed data is displayed on the console.  
- Check the log file `log_file.txt` for progress and timestamped messages. 
+ If data is transformed successfully and not empty, the transformed data is saved to transformed_data.csv.  

**Dependencies**  
`Python 3.x`    
`pandas library`  

**Author**
``Md Zahidul Islam``
