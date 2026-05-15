import csv
import json

REQUIRED_COLUMNS = ["name", "age", "email"]

def validate_row(row):
    for col in REQUIRED_COLUMNS:
        if not row.get(col):
            return False
    return True

def process_csv(file_path):
    clean_data = []

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)


            #validate columns
            if not all(col in reader.fieldnames for col in REQUIRED_COLUMNS):
                raise Exception("Missing required columns")
            
            for row in reader:
                if validate_row(row):
                    # clean/ transform data
                    clean_data.append({
                        "name": row["name"].strip(),
                        "age": int(row["age"]),
                        "email": row["email"].strip().lower()
                    })
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

    return clean_data


def save_json(data, output_file):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)


data = process_csv("data.csv")
save_json(data, "output.json")

print("Data processing complete. Clean data saved to output.json")



            

