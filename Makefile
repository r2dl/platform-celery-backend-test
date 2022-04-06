build:
	docker build -t $$(basename "`pwd`" | sed 's/[A-Z, -]//g') .

run: build
	docker run -d -p 8080:8080	--name	$$(basename "`pwd`" | sed 's/[A-Z, -]//g')  backendframework

test:
	PYTHONPATH=. pytest --cov

linter:
	PYTHONPATH=. black -l 120 --check .
