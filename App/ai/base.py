from abc import ABC, abstractmethod
from typing import AsyncGenerator

class AIPlatform(ABC):

    @abstractmethod
    async def chat(self, prompt: str) -> AsyncGenerator[str, None]:
        pass
