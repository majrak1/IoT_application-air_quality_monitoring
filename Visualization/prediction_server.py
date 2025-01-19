from flask import Flask, jsonify
import csv
import os

timestampt = 2
timestamph = 2
timestamp = 2

app = Flask(__name__)

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
    global timestampt
    filepath = "../datasets/predictions_T.csv"
    """Endpoint to fetch data from the CSV file."""
    try:
        data = read_csv_file(filepath, timestamp)
        timestamp += 1
        print(timestamp)
        if not data:
            return jsonify({"message": "No data found."}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/data/t", methods=["GET"])
def get_data_h6c6():
    global timestampt
    filepath = "../datasets/predictions_T.csv"
    """Endpoint to fetch data from the CSV file."""
    try:
        data = read_csv_file(filepath, timestampt)
        timestampt += 1
        print(timestampt)
        if not data:
            return jsonify({"message": "No data found."}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/data/h6ch", methods=["GET"])
def get_data_t():
    global timestamph
    filepath = "../datasets/Nosensorpredictions.csv"
    """Endpoint to fetch data from the CSV file."""
    try:
        data = read_csv_file(filepath, timestamph)
        timestamph += 1
        print(timestamph)
        if not data:
            return jsonify({"message": "No data found."}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # run the app on port 5577 with debug true
    app.run(port=5588, debug=True)
