import os
import openai
from src.config import config

try:
    from gpt4all import GPT4All  # Локальная модель
    LOCAL_MODEL_AVAILABLE = True
except ImportError:
    LOCAL_MODEL_AVAILABLE = False

class AIEngine:
    """Класс для работы с OpenAI API и локальными моделями."""
    
    def __init__(self, mode="hybrid"):
        self.mode = mode
        self.api_key = os.getenv("OPENAI_API_KEY", config.OPENAI_API_KEY)
        self.local_model = None
        
        if LOCAL_MODEL_AVAILABLE:
            self.local_model = GPT4All(model_path=config.LOCAL_MODEL_PATH)

    def generate(self, prompt):
        """Выбирает доступный движок и генерирует ответ."""
        if self.mode == "online" and self.api_key:
            return self.generate_online(prompt)
        elif self.mode == "offline" and self.local_model:
            return self.generate_offline(prompt)
        elif self.mode == "hybrid":
            return self.generate_online(prompt) if self.api_key else self.generate_offline(prompt)
        else:
            return "❌ Нет доступных моделей."

    def generate_online(self, prompt):
        """Генерация через OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                api_key=self.api_key
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"⚠️ Ошибка API: {str(e)}"

    def generate_offline(self, prompt):
        """Генерация через локальную модель GPT4All."""
        if not self.local_model:
            return "❌ Локальная модель недоступна."
        return self.local_model.generate(prompt)

# Экземпляр движка, который будем использовать в API
ai_engine = AIEngine(mode=config.MODE)