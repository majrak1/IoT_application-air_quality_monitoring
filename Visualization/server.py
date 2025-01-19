from flask import Flask, jsonify
import csv
import os

timestamp = 2

app = Flask(__name__)

# CSV_FILE_PATH = "./datasets/AirQuality.csv"
CSV_FILE_PATH = "../datasets/air_df_correct_format.csv"
# CSV_FILE_PATH = "./datasets/processed.csv"

def read_csv_file(file_path, timestamp):
    """Read data from a CSV file and return it as a list of dictionaries."""
    if not os.path.exists(file_path):
        return []
    
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';', skipinitialspace=True)
        checker = 0
        for row in reader:
            if checker < timestamp:
                checker += 1
                # Convert comma-separated values to dot-separated for numerical consistency
                converted_row = {key: value.replace(",", ".") for key, value in row.items()}
                data.append(converted_row)
            else:
                break
            
    return data

@app.route("/data", methods=["GET"])
def get_data():
    global timestamp
    """Endpoint to fetch data from the CSV file."""
    try:
        data = read_csv_file(CSV_FILE_PATH, timestamp)
        timestamp += 1
        print(timestamp)
        if not data:
            return jsonify({"message": "No data found."}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # run the app on port 5577 with debug true
    app.run(port=5577, debug=True)
