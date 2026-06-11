# 🩺 SOAP Note Generator

A Streamlit web app that turns raw clinical encounter notes into a structured
**SOAP note** (Subjective, Objective, Assessment, Plan) using a large language
model via LangChain.

> ⚠️ This tool produces a documentation **draft for clinician review**. It is not
> medical advice and not a substitute for professional judgment.

## Features

- Paste free-text encounter notes and generate a clean SOAP note
- Adjustable model **creativity** (temperature) from the sidebar
- Download the generated note as a `.txt` file
- Safety-focused prompt: the model uses only the information provided and never
  invents vitals, labs, or findings

## Tech Stack

- **Python**
- **Streamlit** – web UI
- **LangChain** – prompt + model orchestration (LCEL)
- **Google Gemini** (`gemini-2.5-flash`) via `langchain-google-genai`

## Project Structure

```
.
├── app.py          # Streamlit UI
├── soap_chain.py   # Builds the LangChain chain and generates the note
├── prompts.py      # SOAP prompt template
├── requirements.txt
└── .env            # API keys (not committed)
```

## Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key to a .env file
echo "GOOGLE_API_KEY=your_key_here" > .env

# 4. Run the app
streamlit run app.py
```

Get a free Gemini API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

## How It Works

```
prompt template  →  Gemini model  →  output parser
 (prompts.py)        (soap_chain.py)    (clean text)
```

The encounter text is inserted into a prompt template, sent to the model, and the
response is parsed into plain text — composed as a single LangChain chain:

```python
chain = soap_prompt | llm | parser
```

## License

For educational use.
