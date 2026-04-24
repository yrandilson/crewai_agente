"""
config.py — Configurações centrais do projeto
"""

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY    = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL      = os.getenv("OPENAI_MODEL_NAME", "gpt-4o")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
VERBOSE           = os.getenv("VERBOSE", "true").lower() == "true"

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
