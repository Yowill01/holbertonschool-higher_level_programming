#!/usr/bin/env python3
"""Module that converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and save it in data.json.

    Args:
        csv_filename: path of the input CSV file.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(rows, f)
        return True
    except (OSError, csv.Error):
        return False
