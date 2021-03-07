gcloud builds submit --tag gcr.io/corona-tagebuch2/corona
gcloud run deploy --image gcr.io/corona-tagebuch2/corona --platform managed