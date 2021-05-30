from pathlib import Path


class Config:
    SECRET_KEY = "nonacZunMissyiccadPyctOv3Shryd"
    MODEL_DIR = Path.cwd().joinpath("models")


config = Config()
