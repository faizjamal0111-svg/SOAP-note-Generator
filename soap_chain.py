from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from prompts import soap_prompt

load_dotenv()


parser = StrOutputParser()



def generate_soap_note(encounter_text, temperature):
    """Generate a SOAP note from raw encounter text. Returns a string."""
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.5-flash',
        temperature=temperature
    )
    chain = soap_prompt | llm | parser
    return chain.invoke({'encounter': encounter_text})

    
if __name__ == "__main__":
    sample = (
        "45 y/o male presents with sharp chest pain for 2 days, worse on "
        "exertion. BP 150/95, HR 92. No fever. History of hypertension. "
        "Started on aspirin, ECG ordered, follow up in 1 week."
    )
    print(generate_soap_note(sample, 0.3))
