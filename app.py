from pathlib import Path

from api import create_app

if Path('instance').exists():
    app = create_app(config_file='config.py')
else:
    app = create_app()
