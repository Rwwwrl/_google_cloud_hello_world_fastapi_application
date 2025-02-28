build:
	docker build -f Dockerfile -t hello-world-fastapi-application:latest .

run:
	docker run -d --rm -p 8080:8080 --name fastapi hello-world-fastapi-application:latest

stop:
	docker stop fastapi

container_shell:
	docker exec -it fastapi bash


# tests

build_tests_image:
	docker build -f Dockerfile --target image_for_running_tests -t hello-world-fastapi-application-test-stage:latest .

run_tests:
	docker run --rm hello-world-fastapi-application-test-stage:latest


# google cloud

deploy:
	gcloud app deploy --quiet
