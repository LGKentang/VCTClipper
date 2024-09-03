from googleapiclient.discovery import build
from path import dotenv_path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path)
API_KEY = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=API_KEY)

