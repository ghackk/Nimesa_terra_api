provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.main.id
  availability_zone = "us-east-1a"
  cidr_block = "10.0.1.0/24"
}

resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.main.id
  availability_zone = "us-east-1b"
  cidr_block = "10.0.2.0/24"
}

resource "aws_security_group" "default" {
  name = "default"
  vpc_id = aws_vpc.main.id

  egress {
    from_port = 0
    to_port = 65535
    cidr_blocks = ["0.0.0.0/0"]
    protocol = "tcp"
  }
}
