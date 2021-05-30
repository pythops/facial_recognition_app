setup:
	@(\
		python3 -m venv .venv && \
		pip3 install -U pip && \
		pip3 install -r requirements.txt \
	)

pip-update:
	@pip-compile --output-file=requirements.txt -U requirements.in
run:
	@flask run
