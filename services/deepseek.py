import openai
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
    def __init__(self, page):
        print("嗨，理理我")
        self.page = page
        openai.api_key = DEEPSEEK_API_KEY
        openai.api_base = DEEPSEEK_BASE_URL + "/v1"  # 注意需要添加 /v1
        self.system_prompt = SYSTEM_PROMPT
        self.model = DEEPSEEK_MODEL
        self.temperature = TEMPERATURE
        self.max_tokens = MAX_TOKENS
        self.top_p = TOP_P
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ]
        print("我讨厌")
        print("冷暴力")

    def send_message(self, user_input: str):
        try:
            print("来了吗")
            print("咋不来")
            self.messages.append({"role": "user", "content": user_input})

            print("难道要朕请你吗！")
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p
            )

            reply = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": reply})
            print("朕错了，你真不肯来吗")
            return reply, None

        except Exception as e:
            print("别这样")
            import traceback
            traceback.print_exc()
            return None, str(e)