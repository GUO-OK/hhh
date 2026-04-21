from openai import OpenAI
from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    SYSTEM_PROMPT,
    TEMPERATURE,
    MAX_TOKENS,
    TOP_P
)

class DeepSeekClient:
    print("✅ 正在使用正确的 deepseek.py")

    def __init__(self, page):
        self.page = page
        self.client = OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_BASE_URL
        )

        self.system_prompt = SYSTEM_PROMPT
        self.model = DEEPSEEK_MODEL
        self.temperature = TEMPERATURE
        self.max_tokens = MAX_TOKENS
        self.top_p = TOP_P

        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ]

    def send_message(self, user_input: str):
        try:
            self.messages.append({"role": "user", "content": user_input})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p
            )

            reply = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": reply})

            return reply, None

        except Exception as e:
            return None, str(e)