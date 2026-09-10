variable "aws_region" {
  description = "AWS region for Project 3"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for AWS resources"
  type        = string
  default     = "project-3-voting"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "c7i-flex.large"
}

variable "key_name" {
  description = "AWS EC2 key pair name"
  type        = string
  default     = "linux-key"
}

variable "allowed_ip" {
  description = "Public IP address allowed to access the server"
  type        = string
}