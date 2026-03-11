"""
script_generator.py
Generates a full YouTube documentary-style script using Groq API (Free).
"""

from groq import Groq


def generate_script(topic: str, client: Groq) -> str:
    """
    Generate a YouTube documentary script for the given topic.

    Args:
        topic: The subject for the video script.
        client: An authenticated Groq client instance.

    Returns:
        A formatted YouTube script as a string.
    """
    prompt = f"""You are an expert YouTube scriptwriter. Write a full, engaging YouTube documentary-style video script about the following topic:

Topic: {topic}

Requirements:
- Include a strong HOOK at the beginning to grab attention within the first 30 seconds
- Structure the script with clear sections: INTRO, MAIN CONTENT (with 3-5 sub-sections), and OUTRO
- Use a conversational and engaging tone suitable for YouTube
- Include "[B-ROLL: ...]" directions where relevant to guide video editors
- Add "[MUSIC CUE: ...]" notes where background music changes are needed
- End with a call-to-action asking viewers to like, comment, and subscribe
- The script should be detailed enough for a 8-12 minute video

Format the output clearly with section headers in UPPERCASE followed by a colon.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a professional YouTube scriptwriter specializing in educational and documentary-style content.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
        max_tokens=2500,
    )

    return response.choices[0].message.content.strip()
