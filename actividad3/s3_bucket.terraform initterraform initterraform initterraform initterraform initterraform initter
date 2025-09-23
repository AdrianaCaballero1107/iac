provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "adriana_bucket" {
  bucket = "adriana-bucket-terr"  # Nombre único, obligatorio en S3
  acl    = "private"              # Permisos privados por default

  tags = {
    Name = "adriana-bucket-terr"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.adriana_bucket.bucket
}


