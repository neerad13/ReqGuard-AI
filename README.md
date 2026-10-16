# ReqGuard AI
### AI-Assisted Software Requirements Engineering and Analysis

ReqGuard AI is a Python-based application designed to improve the quality, clarity, consistency, and testability of Software Requirements Specification (SRS) documents.

The application combines rule-based analysis, text similarity techniques, and Generative AI to help identify requirement issues and support software requirements engineering workflows.

## Features

- **PDF Requirement Extraction:** Extract software requirements from uploaded PDF documents.
- **Ambiguity Detection:** Identify potentially ambiguous wording using predefined rules.
- **Requirement Quality Analysis:** Assess requirement quality based on detected ambiguity.
- **Requirement Classification:** Classify requirements into relevant categories.
- **Readability Analysis:** Evaluate the readability of requirement statements.
- **AI-Assisted Rewriting:** Use Google's Gemini API to suggest clearer requirement statements.
- **Duplicate Detection:** Identify potentially duplicate requirements using TF-IDF and cosine similarity.
- **Conflict Analysis:** Detect potential inconsistencies between requirements.
- **IEEE-Style Structure Checking:** Check document structure against selected IEEE-style criteria.
- **Test Case Generation:** Generate test cases from extracted requirements.
- **Requirements Traceability Matrix (RTM):** Support traceability between requirements and test cases.
- **Requirement Chatbot:** Ask questions about requirement documents using retrieval-augmented responses.
- **Dashboard and Reports:** View analysis results and generate reports.

## Technology Stack

- **Language:** Python
- **Application Framework:** Streamlit
- **Generative AI:** Google Gemini API
- **Machine Learning and Text Processing:** scikit-learn, TF-IDF, cosine similarity
- **PDF Processing:** PyMuPDF
- **Data Processing and Visualization:** Python data-processing and visualization libraries

## Architecture Overview

ReqGuard AI uses a combination of deterministic analysis and AI-assisted functionality.

1. PDF documents are processed to extract requirement statements.
2. Rule-based and text-analysis modules evaluate ambiguity, readability, quality, classification, and similarity.
3. AI-assisted functionality supports requirement rewriting and conversational queries.
4. Additional modules support conflict analysis, test case generation, traceability, and document structure checks.
5. The application presents results through a Streamlit interface.

The outputs are intended to support engineering review and should not be treated as a replacement for human validation or formal verification.

## Getting Started

### Prerequisites

- Python installed on your system
- Git
- A Google Gemini API key for features that require the Gemini API

### 1. Clone the repository

```bash
git clone https://github.com/neerad13/ReqGuard-AI.git
cd ReqGuard-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a local `.env` file in the project root if required by your configuration.

Add your own Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your actual key. Never commit `.env` or publish API credentials to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit should open the application in your browser.

## Project Structure

```text
ReqGuard-AI/
├── app.py
├── modules/
│   ├── duplicate_detector.py
│   ├── ieee_compliance.py
│   ├── llm.py
│   ├── metrics.py
│   ├── pdf_parser.py
│   ├── project_health.py
│   ├── quality_score.py
│   ├── rag_engine.py
│   ├── readability.py
│   ├── report_generator.py
│   ├── requirement_extractor.py
│   ├── requirement_verifier.py
│   ├── test_case_generator.py
│   └── traceability.py
├── tests/
├── outputs/
├── reports/
├── uploads/
├── requirements.txt
├── .env.example
└── README.md
```

*Note: The structure above highlights the main application files. Some folders and modules may vary as the project evolves.*

## Testing

The project includes unit tests for requirement verification and conflict detection.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

## Current Scope

ReqGuard AI is an evolving Software Requirements Engineering project. Its analysis combines predefined rules, text-based similarity methods, and AI-assisted features. Detection results can depend on the rules and input context, so human review remains important.

## Future Improvements

- Improve contextual understanding of complex requirements.
- Expand evaluation using additional unseen requirement examples.
- Improve the handling of uncertain or incomplete evidence.
- Strengthen traceability and validation workflows.

## Security

- Do not commit `.env` files or API keys.
- Use `.env.example` only for placeholder configuration.
- Keep credentials private and configure your own API key locally.

## Author

Developed as a Software Engineering project exploring requirements analysis, NLP, and Generative AI.

**ReqGuard AI — Making software requirements clearer, more consistent, and easier to validate.**
