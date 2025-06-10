from groq import Groq

client = Groq(api_key="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")  # Replace with your actual API key

def learn_german(text):
    if not text.strip():
        return "❗ Please enter an English sentence."

    prompt = f"""
You are a helpful AI German language tutor. Your job is to:
1. Translate the given English sentence into German.

Sentence: "{text}"

Your response must be in the following format:
Translation: <German Translation>
"""
    try:
        completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=200,
            top_p=0.9,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

import ast

import json
import re

def generate_mcq_questions():
    prompt = """
Generate 10 multiple choice questions to help a user practice German.
Each question should be a JSON object like:
{
  "question": "What is the German translation for 'Good morning'?",
  "options": ["Guten Morgen", "Gute Nacht", "Hallo", "Danke"],
  "answer": "Guten Morgen"
}
Return ONLY a JSON list of 10 such objects, nothing else (no variable names, no Python code, no markdown).
"""

    try:
        completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800,
            top_p=0.9,
        )

        content = completion.choices[0].message.content.strip()
        print("\n🧠 LLM Raw Response:\n", content)

        # Remove any markdown code fences like ```json or ```python
        content = re.sub(r"```(?:json|python)?\n", "", content)
        content = re.sub(r"```", "", content)

        # Now parse as JSON
        mcqs = json.loads(content)

        # Verify it's a list of dicts
        if isinstance(mcqs, list) and all(isinstance(q, dict) for q in mcqs):
            return mcqs
        else:
            raise ValueError("Parsed JSON is not a list of dictionaries.")

    except Exception as e:
        print("⚠️ LLM Error:", str(e))
        return []


