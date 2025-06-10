from groq import Groq

client = Groq(api_key="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")  # Replace with your real API key

def generate_daily_challenge():
    prompt = """
You are an AI German tutor. Please generate today's daily challenge that includes:
1. A simple translation task (EN -> DE)
2. A short multiple choice vocabulary quiz
3. One fill-in-the-blank sentence

Format it clearly with titles.
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
