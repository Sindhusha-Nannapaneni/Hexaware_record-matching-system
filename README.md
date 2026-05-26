**Record Matching System (CRM ↔ Calendar)**

**Overview**
This project implements an intelligent record matching system that links CRM records with Calendar events using a rule-based similarity engine.

The system identifies whether two records refer to the same real-world meeting using:
Temporal similarity
Text similarity
Company alignment
Attendee matching
Weighted scoring + strict filtering

It is exposed via a FastAPI REST service and supports batch pipeline evaluation.

**Project Architecture**
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
│   ├── features.py
│   ├── matcher.py
│   ├── evaluator.py
│
├── run_pipeline.py
├── run_api.py
├── requirements.txt
└── README.md


**Setup Instructions**
Install dependencies
pip install -r requirements.txt


**Running the Pipeline**
python run_pipeline.py


**Pipeline Steps:**
Load CRM and Calendar data
Preprocess text and datetime fields
Generate candidate pairs (filtering)
Compute similarity scores
Predict matches
Evaluate performance


**Running the API**
python run_api.py


**Swagger UI:**
http://127.0.0.1:8000/docs


**Matching Approach**
The system uses a two-stage hybrid heuristic model:
**1. Candidate Filtering (Hard Gate)**
A pair is considered only if at least 2 of 3 signals are strong:
- Time proximity
- Text similarity
- Company similarity

**2. Weighted Scoring Model**
Final confidence is computed using:
- Time similarity → 45%
- Text similarity → 30%
- Company similarity → 20%
- Attendee match → 5%

  
**Evaluation Results**
Precision : 0.889
Recall    : 0.85
F1 Score  : 0.869


**Key Features**
Handles missing and noisy data
Supports multiple datetime formats
Normalizes virtual meeting locations
Prevents false positive matching using strict gating
Scalable rule-based architecture


**Design Decisions**
Why rule-based approach?
Small dataset
High interpretability required
Fast debugging and iteration
No training data required


**Why two-stage filtering?**
Improves precision significantly
Reduces noise from weak similarity pairs
Mimics production-grade entity matching systems


**Limitations**
No machine learning model (pure heuristic)
Performance depends on threshold tuning
Limited to structured fields only


**Future Improvements**
Replace similarity rules with embeddings (SBERT / OpenAI embeddings)
Add ML classifier on top of features
Improve entity resolution using clustering
Add logging + monitoring for API

**AI Assistance**
AI tools were used for:
Code structuring
Debugging pipeline issues
Improving feature engineering
Documentation drafting
