# Autonomous Insurance Claims Processing Agent

## 📌 Overview

This project implements a lightweight **Autonomous Insurance Claims Processing Agent** designed to process FNOL (First Notice of Loss) documents in **TXT and PDF** formats.

Insurance FNOL documents are typically unstructured. This agent automatically:
- Extracts key claim information
- Validates mandatory fields
- Applies predefined business routing rules
- Produces a structured JSON output with a clear explanation of decisions

The solution is intentionally kept simple, readable, and explainable, aligning with real-world backend processing systems used in insurtech companies.

---

## 🎯 Problem Statement

Insurance companies receive FNOL documents that must be processed quickly and accurately.  
Manual processing is slow and error-prone.

The goal of this project is to build a backend agent that:
- Understands FNOL content
- Identifies missing or risky information
- Routes claims to the correct workflow automatically

---

## ⚙️ Features

✔ Accepts FNOL documents in **TXT and PDF** formats  
✔ Extracts policy, incident, asset, and claim details  
✔ Detects missing mandatory fields  
✔ Applies deterministic business routing rules  
✔ Generates explainable, human-readable reasoning  
✔ Outputs results in a strict JSON format  
✔ Runs locally with no UI, database, or cloud dependencies  

---

## 🧠 Extracted Information

### Policy Information
- Policy Number  
- Policyholder Name  
- Effective Dates  

### Incident Information
- Date of Loss  
- Time of Loss  
- Location of Loss  
- Description of Incident  

### Asset Details
- Asset Type (vehicle / property)  
- Asset ID (VIN, etc.)  
- Estimated Damage Amount  

### Other Mandatory Fields
- Claim Type (vehicle / injury)  
- Attachments (yes / no)  
- Initial Estimate  

---

## 🚦 Claim Routing Rules

The following rules are applied **in priority order**:

1. **Manual Review**  
   - If any mandatory field is missing  

2. **Investigation Flag**  
   - If the description contains keywords such as  
     `fraud`, `staged`, or `inconsistent`

3. **Specialist Queue**  
   - If the claim type is `injury`

4. **Fast-track**  
   - If the estimated damage amount is less than **25,000**

Each routing decision includes a short explanation describing *why* the claim was routed.

---

## 📂 Project Structure

```text
insurance-claims-agent/
├── main.py
├── utils/
│   ├── pdf_reader.py
│   ├── field_extractor.py
│   └── router.py
├── sample_fnol/
│   ├── sample1.txt
│   └── sample2.txt
├── output.json
├── requirements.txt
└── README.md
🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run the application
python main.py
3️⃣ View output
The processed result will be:

Printed to the console

Saved in output.json

📄 Sample Output
{
  "extractedFields": {
    "policy_number": "POL12345",
    "policyholder_name": "John Doe",
    "date_of_loss": "12/01/2026",
    "time_of_loss": "14:30",
    "location": "Hyderabad, India",
    "description": "Rear-end collision, vehicle damaged.",
    "asset_type": "vehicle",
    "asset_id": "VIN987654",
    "estimated_damage": 18000,
    "claim_type": "vehicle",
    "attachments": "no",
    "initial_estimate": 18000
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage below threshold for fast-track processing"
}
🧪 Notes & Assumptions
Field extraction uses regex and keyword matching

Accuracy is intentionally balanced with explainability

No UI is included, as this is a backend processing component

Designed for local execution and easy review

🧑‍💻 Author
Sumanth Kalla

