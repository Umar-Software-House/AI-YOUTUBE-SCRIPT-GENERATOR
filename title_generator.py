"""
title_generator.py
Generates YouTube video titles and a video description using Groq API (Free).
"""

from groq import Groq


def generate_titles(topic: str, client: Groq) -> str:
    """
    Generate 5 YouTube title ideas for the given topic.

    Args:
        topic: The subject for the video.
        client: An authenticated Groq client instance.

    Returns:
        A formatted string containing 5 YouTube title options.
    """
    prompt = f"""You are a YouTube SEO expert and content strategist. Generate exactly 5 compelling YouTube video title ideas for the following topic:

Topic: {topic}

Requirements:
- Each title must be highly clickable and curiosity-driven
- Include power words (e.g., "shocking", "untold", "ultimate", "truth", "secret")
- Keep each title under 70 characters for SEO
- Mix different styles: question-based, list-based, story-based, and controversy-based
- Number each title 1-5

Return only the numbered list of titles. No extra commentary.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a YouTube SEO expert who writes high-performing, click-worthy video titles.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()


def generate_description(topic: str, client: Groq) -> str:
    """
    Generate an SEO-optimised YouTube video description for the given topic.

    Args:
        topic: The subject for the video.
        client: An authenticated Groq client instance.

    Returns:
        A formatted YouTube video description as a string.
    """
    prompt = f"""You are a YouTube SEO specialist. Write a professional and SEO-optimised YouTube video description for the following topic:

Topic: {topic}

Requirements:
- Start with a strong 2-3 sentence summary of the video (most important for SEO)
- Include a "What you'll learn:" bullet-point section with 4-5 key takeaways
- Add a "Chapters / Timestamps" placeholder section (use [00:00] format)
- Include a short "About this channel" paragraph at the end
- End with a call-to-action: Like, Subscribe, and turn on notifications
- Keep the total description between 250-350 words
- Write in second person ("You will discover...")

Use plain text only. No markdown symbols.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a YouTube SEO specialist who writes descriptions that rank well and convert viewers into subscribers.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=600,
    )

    return response.choices[0].message.content.strip()
