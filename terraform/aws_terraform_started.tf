terraform {
  required_version = ">= 0.12.21"

  backend "s3" {
    region         = "{region}"
    bucket         = "{s3-bucket-name}"
    dynamodb_table = "{dynamodb-lock-table}"
    key            = "{file-key}"
    encrypt        = true
  }
}

// prodivers.tf

provider "aws" {
  version = "~> 2.53"

  region  = var.region
  profile = var.profile
}

// variables.tf

variable "region" {
  default = "my-region"
}


variable "profile" {
  default = "my-aws-profile"
}