AUDITUS: The Explainer Robot (XAI)

Automated Justification Reports for Audit Transparency

🌟 Project Overview: The RegTech Suite

This application is part of a three-piece RegTech Suite designed to automate critical compliance workflows using modern AI/ML simulation techniques. This specific component addresses the need for Explainable AI (XAI).

Key Value Proposition

The AUDITUS simulates an XAI engine that allows auditors and regulatory bodies to automatically generate structured justification reports that explain why a compliance breach was detected, ensuring full transparency.

🚀 Live Demo and Core Functionality

Live Application: https://auditus-xai-lisa-silva.streamlit.app/

Feature

Description

Business Impact

XAI Justification Report

Creates a structured, numbered report detailing the breach, the governing rule, and the rationale (the 'Why').

Fulfills regulatory requirements for explaining automated decisions, drastically simplifying the audit process.

Streamlit Interface

Provides a simple, interactive web interface built entirely in Python.

No special software installation needed for end-users; accessible via any browser.

Specific Evidence Trace

Clearly links the non-compliant finding back to the exact keyword(s) found in the evidence.

Provides a direct, auditable path from raw data to the final non-compliant classification.

💻 Local Setup and Installation

To run this application locally, you will need Python 3.8+.

Prerequisites

Clone the Repository:

git clone github.com/lisa-silva/auditus-xai/edit/main/README.md
cd auditus-xai


Create a Virtual Environment (venv):

python -m venv venv
.\venv\Scripts\activate  # Windows
# or source venv/bin/activate # macOS/Linux


Running the App

Install Dependencies:
This app requires streamlit (listed in requirements.txt).

pip install -r requirements.txt


Launch the Application:

streamlit run auditus_app.py 


The application will automatically open in your browser at http://localhost:8501.

🛠️ Technology Stack

Framework: Streamlit (Python)

Version Control: Git & GitHub

Deployment: Streamlit Cloud

Language: Python 3.x
