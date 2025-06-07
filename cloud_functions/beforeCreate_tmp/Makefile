deploy:
	gcloud functions deploy before-create \
		--runtime=nodejs20 \
		--no-gen2 \
	    --trigger-http \
		--allow-unauthenticated \
		--entry-point=beforeCreate \
		--source=. \
		--region=europe-central2 \
		--project=fast-academy-458612-a4
