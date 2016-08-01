install:
	@pip install --upgrade .

uninstall:
	@pip uninstall hot -y

test-http:
	@python scripts/monkeypatch_01.py
