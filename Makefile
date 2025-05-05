# Docker
up_mongo:
	docker compose -p fastapi-hello-world -f docker-compose.mongo.yml up -d

down_mongo:
	docker compose -p fastapi-hello-world -f docker-compose.mongo.yml down

restart_mongo:
	$(MAKE) down_mongo
	$(MAKE) up_mongo

dbuild_app_prod_image:
	docker build -t fastapi-hello-world-app:prod_image -f Dockerfile --target prod_image .

drun_app_prod_image:
	docker run -d --rm -p 8080:8080 --name fastapi-hello-world-app fastapi-hello-world-app:prod_image

dbuild_app_tests:
	docker build -t fastapi-hello-world-app:tests -f Dockerfile --target image_for_running_tests_in_github_actions .

drun_app_tests:
	docker run --rm --name fastapi-hello-world-app-tests fastapi-hello-world-app:tests


# Tests
run_pytest:
	pytest -c pytest.ini app --disable-warnings
