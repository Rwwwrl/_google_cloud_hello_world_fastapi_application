# Docker
up_tests_env:
	docker compose -p tests_env -f docker-compose.tests_env.yml up -d

down_tests_env:
	docker compose -p tests_env down

restart_tests_env:
	$(MAKE) down_tests_env
	$(MAKE) up_tests_env


# Google cloud
deploy:
	gcloud app deploy --quiet
