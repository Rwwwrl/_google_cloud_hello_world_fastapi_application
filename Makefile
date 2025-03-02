# Docker
up:
	docker compose -p hello-world-fastapi-application up -d

down:
	docker compose -p hello-world-fastapi-application down

restart:
	$(MAKE) down
	$(MAKE) up

build:
	docker build -f Dockerfile -t hello-world-fastapi-application:latest .

run:
	docker run -d --rm -p 8080:8080 --name fastapi hello-world-fastapi-application:latest

stop:
	docker stop fastapi


# Google cloud
deploy:
	gcloud app deploy --quiet
