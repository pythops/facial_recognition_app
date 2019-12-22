from pathlib import Path

from app import create_app

if Path('instance').exists():
    app = create_app(config_file='config.py')
else:
    app = create_app()
