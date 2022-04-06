build:
	docker build -t $$(basename "`pwd`" | sed 's/[A-Z, -]//g') .

run: build
	docker run -it --rm -p 8080:8080 --name backendframework $$(basename "`pwd`" | sed 's/[A-Z, -]//g')

test:
	PYTHONPATH=. pytest --cov

linter:
	PYTHONPATH=. black -l 120 --check .
