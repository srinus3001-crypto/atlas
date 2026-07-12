"""
Enterprise JSON Parser
"""

import json
import re


class JSONParser:
    @staticmethod
    def extract(text):
        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")

        if text.startswith("```"):
            text = text.replace("```", "")

        text = text.strip()

        try:
            return json.loads(text)

        except Exception:
            pass

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            return json.loads(match.group())

        raise ValueError("No valid JSON found.")
