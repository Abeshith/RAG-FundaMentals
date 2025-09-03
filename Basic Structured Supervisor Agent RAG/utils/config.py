import yaml
import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    with open('config/settings.yaml', 'r') as f:
        return yaml.safe_load(f)

def get_api_keys():
    return {
        'groq': os.getenv('GROQ_API_KEY'),
        'tavily': os.getenv('TAVILY_API_KEY'),
        'langsmith': os.getenv('LANGSMITH_API_KEY')
    }
