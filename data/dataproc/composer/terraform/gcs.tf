resource "google_storage_bucket" "orders_bucket" {
  name     = "orders-landing-bucket-demo"
  location = "asia-south1"
}