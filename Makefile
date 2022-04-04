build:
	docker build -t $$(basename "`pwd`" | sed 's/[A-Z, -]//g') .

test:
	pytest --cov

linter:
	black -l 120 --check .