variable "instance_type" {
    description = "Type instance type EC2"
    type = string
    default = "t2.micro"
  
}

locals{
    instance_count = 2
    instance_name = "act6-adri-fabro"
}


resource "aws_instance" "adrifabro_server_terr" {
    count = local.instance_count
    ami = "ami-0ca4d5db4872d0c28"
    instance_type = "t3.micro"
    
    tags = {
        Name = local.instance_name
    } 
}

output "server_name" {
    value = aws_instance.adrifabro_server_terr[0].tags.Name
  
}