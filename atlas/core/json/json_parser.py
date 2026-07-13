"""
Enterprise JSON Parser
"""

import json
import re


class JSONParser:
    @staticmethod
    def extract(text):
        if not text:
            raise ValueError("Empty response.")

        text = text.strip()

        # Remove markdown code blocks
        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.startswith("```"):
            text = text.replace("```", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        # Try parsing directly
        try:
            return json.loads(text)

        except Exception:
            pass

        # Extract first JSON object from surrounding text
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except Exception:
                pass

        # Regex fallback
        match = re.search(r"\{[\s\S]*\}", text)

        if match:
            try:
                return json.loads(match.group())
            except Exception:
                pass

        raise ValueError("No valid JSON found.")
