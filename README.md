# Sample commands

```sh
cd helloword
PROJECT_ID=$(gcloud config get-value project)
COMMIT_SHA="$(git rev-parse --short=7 HEAD)"

# build a container image on Artifact Registry
gcloud artifacts repositories create my-repository --repository-format=docker --location=europe-west6
gcloud builds submit --tag="europe-west6-docker.pkg.dev/${PROJECT_ID}/my-repository/object-detector:${COMMIT_SHA}" .

# create a Kubernet cluster and connect to it
gcloud container clusters create-auto mycluster --region europe-west6
gcloud container clusters get-credentials mycluster --region europe-west6

# deploy the built container
sed -i -e "s/\$PROJECT_ID/$PROJECT_ID/g" gke.yaml
sed -i -e "s/\$COMMIT_SHA/$COMMIT_SHA/g" gke.yaml
kubectl apply -f gke.yaml
```