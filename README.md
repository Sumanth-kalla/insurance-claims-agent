# Autonomous Insurance Claims Processing Agent

## Overview
This project implements a lightweight autonomous agent to process FNOL (First Notice of Loss) insurance documents. The system extracts key claim information, validates mandatory fields, applies business routing rules, and outputs a structured JSON response with a clear explanation.

## Approach
- Supports PDF and TXT FNOL documents
- Uses regex and keyword-based extraction for clarity
- Validates mandatory fields before routing
- Applies deterministic business rules for claim routing
- Produces explainable JSON output

## Routing Rules
- Missing mandatory fields → Manual Review
- Fraud-related keywords → Investigation Flag
- Injury claims → Specialist Queue
- Estimated damage < 25,000 → Fast-track

## How to Run
```bash
pip install -r requirements.txt
python main.py
