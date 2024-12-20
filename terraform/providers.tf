provider "google" {
  credentials = file("C:/Users/Nabil/Downloads/MLops/credentials/terraform-key.json")
  project     = "mlops-project-191920"
  region      = "europe-west9"
}
