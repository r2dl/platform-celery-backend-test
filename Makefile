build:
	docker build -t $$(basename "`pwd`" | sed 's/[A-Z, -]//g') .

run: build
	docker run -d -p 8000:8000	--name	$$(basename "`pwd`" | sed 's/[A-Z, -]//g')  backendframework

test:
	pytest --cov

linter:
	black -l 120 --check .