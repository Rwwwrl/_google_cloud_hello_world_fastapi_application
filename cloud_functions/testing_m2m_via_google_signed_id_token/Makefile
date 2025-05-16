deploy:
	gcloud auth activate-service-account --key-file=cloud-run-deploy-service-acount.json
	gcloud run deploy testing-m2m-via-google-signed-id-token \
		--source . \
		--function testingM2MViaGoogleSignedIdToken \
		--base-image nodejs22 \
		--region europe-central2 \
		--no-allow-unauthenticated \
		--project fast-academy-458612-a4 \
		--env-vars-file=config.yaml


ping:
	curl -H "Authorization: Bearer $$(gcloud auth print-identity-token)" https://testing-m2m-via-google-signed-id-token-215060903815.europe-central2.run.app
