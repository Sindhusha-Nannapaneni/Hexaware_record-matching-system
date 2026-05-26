# Record Matching System

## Overview

This project builds a record matching system between CRM records and Calendar events.

The system:
- Loads data from JSON files
- Matches records across sources
- Calculates confidence scores
- Evaluates predictions against labeled data
- Exposes predictions through a REST API

---

## Project Structure

record-matching-system/
│
├── data/
│   ├── crm_events.json
│   ├── calendar_events.json
│   └── evaluation_labels.json
│
├── src/
│   ├── api.py
│   ├── loader.py
│   ├── preprocess.py
│   ├── features.py
│   ├── matcher.py
│   └── evaluator.py
│
├── results/
│
├── run_pipeline.py
├── run_api.py
├── requirements.txt
├── README.md
└── .gitignore

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Matching Pipeline

```bash
python run_pipeline.py
```

This runs:
- data ingestion
- preprocessing
- matching
- evaluation

---

## Run API

```bash
python run_api.py
```

Swagger UI:

http://127.0.0.1:8000/docs

---

## Matching Approach

The matching system uses a weighted scoring approach based on:

- Time similarity
- Attendee similarity
- Company similarity
- Text similarity
- Location similarity

Each feature contributes to a final confidence score.

---

## Handling Bad Data

The system handles:
- Missing values
- Different datetime formats
- Timezone inconsistencies
- Virtual meeting normalization
- Duplicate calendar events

---

## Evaluation Results

Final Metrics:

- Precision: 1.00
- Recall: 0.75
- F1 Score: 0.857

---

## Assumptions

- Records close in time are more likely to match
- Company and attendee similarity are strong indicators
- Virtual meeting locations are normalized

---

## Tradeoffs

A heuristic-based approach was chosen instead of a trained ML model because:
- Dataset size is small
- Rules are interpretable
- Faster implementation and debugging

---

## AI Tool Usage

AI coding assistants were used to help with:
- project structuring
- debugging
- boilerplate generation

Generated code was reviewed and modified during implementation.