output "vpc_id" {
  description = "ID of the Project 3 VPC"
  value       = aws_vpc.main.id
}

output "subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "security_group_id" {
  description = "ID of the server security group"
  value       = aws_security_group.server.id
}

output "instance_id" {
  description = "ID of the Project 3 EC2 instance"
  value       = aws_instance.server.id
}

output "instance_public_ip" {
  description = "Public IP address of the Project 3 EC2 instance"
  value       = aws_instance.server.public_ip
}

output "elastic_ip" {
  description = "Elastic IP address of the Project 3 EC2 instance"
  value       = aws_eip.server.public_ip
}