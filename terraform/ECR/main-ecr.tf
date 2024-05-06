resource "aws_ecr_repository" "ecr" {
  name                 = "greet_ecr_repository"
  image_tag_mutability = var.image_mutability
  encryption_configuration {
    encryption_type = var.encrypt_type
  }
  image_scanning_configuration {
    scan_on_push = true
  }
  tags = var.tags
}