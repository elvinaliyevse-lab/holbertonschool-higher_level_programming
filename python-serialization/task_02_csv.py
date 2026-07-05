#!/usr/bin/python3
"""Convert CSV data to JSON output."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file into a JSON file named data.json."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            return True
    except Exception as exc:
        print("An error occurred:", exc)
        return False


def main():
    """Run the CSV-to-JSON conversion with the default input file."""
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")


if __name__ == "__main__":
    main()

