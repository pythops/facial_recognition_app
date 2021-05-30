SHELL := /bin/bash

setup:
	@(\
		python3 -m venv .venv && \
		source .venv/bin/activate && \
		pip3 install -U pip && \
		pip3 install -r requirements.txt \
	)

pip-update:
	@pip-compile --output-file=requirements.txt -U requirements.in

run:
	@(\
		source .venv/bin/activate && \
		flask run \
	)
