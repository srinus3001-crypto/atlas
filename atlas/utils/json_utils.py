"""
JSON Utilities
"""

import json


class JsonUtils:
    @staticmethod
    def parse(text: str):
        try:
            return json.loads(text)

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON returned by AI: {e}")
