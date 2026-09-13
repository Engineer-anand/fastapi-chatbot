import os
from typing import AsyncGenerator
from App.ai.base import AIPlatform
from groq import AsyncGroq

# Load environment variables
try:
    from dotenv import load_dotenv
    root_env = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
    if os.path.exists(root_env):
        load_dotenv(root_env)
    else:
        load_dotenv()
except ImportError:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_dir, "..", "..", ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line_str = line.strip()
                if "=" in line_str and not line_str.startswith("#"):
                    k, v = line_str.split("=", 1)
                    os.environ[k.strip()] = v.strip().strip('"').strip("'")

def load_prompt() -> str:
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(current_dir, "..", "prompts", "system_prompt.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error loading system prompt: {e}")
        return ""

class Groq(AIPlatform):
    def __init__(self, api_key: str = None, system_prompt: str = None, model: str = "llama-3.3-70b-versatile"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.system_prompt = system_prompt if system_prompt is not None else load_prompt()
        self.model = model
        self.client = None
        if self.api_key:
            try:
                self.client = AsyncGroq(api_key=self.api_key)
            except Exception as e:
                print(f"Error initializing Groq client: {e}")

    async def chat(self, prompt: str) -> AsyncGenerator[str, None]:
        if not self.client:
            key = self.api_key or os.getenv("GROQ_API_KEY")
            if key:
                self.api_key = key
                self.client = AsyncGroq(api_key=key)
            else:
                yield "⚠️ **GROQ_API_KEY is not configured.** Please set your `GROQ_API_KEY` in the `.env` file and restart the server."
                return

        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            stream = await self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                stream=True,
            )
            async for chunk in stream:
                content = chunk.choices[0].delta.content
                if content is not None:
                    yield content
        except Exception as e:
            yield f"⚠️ **Groq AI Error:** {str(e)}"

groq_api_key = os.getenv("GROQ_API_KEY")
ai_platform = Groq(api_key=groq_api_key)
