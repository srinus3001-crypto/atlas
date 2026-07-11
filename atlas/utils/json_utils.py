"""
JSON Utilities
"""

import json


class JsonUtils:

    @staticmethod
    def extract_json(text):

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        return json.loads(text)

