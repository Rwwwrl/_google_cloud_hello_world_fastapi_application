build:
	docker build -f Dockerfile -t google-cloud-hello-world-fastapi-application:latest .

run:
	docker run -d --rm -p 8080:8080 --name fastapi google-cloud-hello-world-fastapi-application:latest

stop:
	docker stop fastapi

container_shell:
	docker exec -it fastapi bash



# google cloud

deploy:
		yes | gcloud app deploy
