.PHONY: build
serve:
	docker-compose up

image:
	docker-compose build

static:
	docker-compose run hovercraft hovercraft /usr/src/app/presentation/slides.rst /usr/src/app/presentation/_build

clean:
	rm -rf presentation/_build

test:
	cd presentation/src && python -m unittest
