resource "aws_s3_bucket" "mybucket" {
  bucket = "my-bucket-example"
  acl    = "private"
}

