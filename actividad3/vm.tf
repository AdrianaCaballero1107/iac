provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "adriana_server_terr" {
  ami           = "ami-0cfde0ea8edd312d4"
  instance_type = "t3.micro"

  tags = {
    Name = "adriana_server_terr"
  }
}

output "server_name" {
  value = aws_instance.adriana_server_terr.tags.Name
}
