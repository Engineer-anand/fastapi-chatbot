import os
from typing import AsyncGenerator
from App.ai.base import AIPlatform
from groq import AsyncGroq

def load_prompt() -> str:
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(current_dir, "..", "prompts", "system_prompt.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error loading system prompt: {e}")
        return "null"
class Groq(AIPlatform):
    def __init__(self, api_key: str, system_prompt: str = None, model: str = "llama-3.3-70b-versatile"):
        self.api_key = api_key
        self.system_prompt = system_prompt if system_prompt is not None else load_prompt()
        self.model = model
        self.client = AsyncGroq(api_key=self.api_key)

    async def chat(self, prompt: str) -> AsyncGenerator[str, None]:
        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": prompt})

        stream = await self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            stream=True,
        )
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content

# Environment variables load karne ke liye
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # Fallback agar python-dotenv installed na ho
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_dir, "..", "..", ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    os.environ[k.strip()] = v.strip().strip('"').strip("'")

groq_api_key = os.getenv("GROQ_API_KEY")
ai_platform = Groq(api_key=groq_api_key)
