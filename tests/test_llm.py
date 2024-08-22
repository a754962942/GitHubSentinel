import unittest

from openai import OpenAI

class TestLLM(unittest.TestCase):

    def test_llm(self):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',
        )
        messages = [
            {"role": "system", "content": "请你用中国道家思维来回答我的所有问题"},
            {"role": "user", "content": "你是谁？"},
        ]
        self.client

