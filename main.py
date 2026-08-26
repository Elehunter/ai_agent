import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import response_apply_patch_tool_call


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            }
        ]
    )

    if not response.usage:
        raise RuntimeError("failed API request")

    print(f"Prompt tokens: {tokens.prompt_tokens}")
    print(f"Response tokens: {tokens.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
