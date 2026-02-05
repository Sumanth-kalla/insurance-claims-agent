import json
import os
from utils.pdf_reader import read_pdf
from utils.field_extractor import extract_fields, find_missing_fields
from utils.router import route_claim

def read_input(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format")

def main():
    input_file = "sample_fnol/sample1.txt"
    text = read_input(input_file)

    fields = extract_fields(text)
    missing = find_missing_fields(fields)
    route, reason = route_claim(fields, missing, text)

    output = {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
