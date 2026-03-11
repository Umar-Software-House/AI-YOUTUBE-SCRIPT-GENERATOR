"""
hashtag_generator.py
Generates YouTube hashtags using Groq API (Free).
"""

from groq import Groq


def generate_hashtags(topic: str, client: Groq) -> str:
    """
    Generate 10 YouTube hashtags for the given topic.

    Args:
        topic: The subject for the video.
        client: An authenticated Groq client instance.

    Returns:
        A formatted string of 10 hashtags.
    """
    prompt = f"""You are a YouTube SEO and social media expert. Generate exactly 10 highly relevant and trending YouTube hashtags for the following topic:

Topic: {topic}

Requirements:
- Mix broad hashtags (high search volume) and niche hashtags (targeted audience)
- All hashtags must start with the # symbol
- Use camelCase for multi-word hashtags (e.g., #AppleVsSamsung)
- Include at least 2 evergreen hashtags related to the general category
- Arrange from most relevant to least relevant
- Return only the hashtags on a single line, separated by spaces

Return only the hashtags. No extra commentary or numbering.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a YouTube SEO specialist who creates hashtag strategies that maximise video discoverability.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=150,
    )

    return response.choices[0].message.content.strip()
