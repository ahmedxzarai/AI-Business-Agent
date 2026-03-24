from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def process_task(task: str) -> str:
    prompt = f"""
    You are an AI business assistant.

    Task:
    {task}

    Give a clear, professional result.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content