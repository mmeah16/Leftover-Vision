from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.environ.get("DB_PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")

def is_running_in_docker():
    return os.getenv("RUNNING_IN_DOCKER") == "true"

# If deploying using a Docker container use host.docker.internal as the Host name, use localhost when developing locally
DB_HOST = 'host.docker.internal' if is_running_in_docker() else 'localhost'
DB_URL = f'postgresql://postgres:{DB_PASSWORD}@{DB_HOST}:5432/postgres'

engine = create_engine(DB_URL, echo=True)

session = Session(engine)

