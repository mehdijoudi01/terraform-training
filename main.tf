terraform {
  required_version = ">= 1.0"
  required_providers {
    render = {
      source  = "registry.terraform.io/render-oss/render"
      version = "~> 1.0"
    }
  }

  cloud {
    organization = "terraform-training-mehdi"

    workspaces {
      name = "terraform-training"
    }
  }
}

provider "render" {
}

resource "render_static_site_test" "example" {
  name          = "render-terraform-example-try"
  repo_url      = "https://github.com/mehdijoudi01/terraform-training"
  branch        = "main"
  build_command = "" # no build needed for html file, ---- ken 3ana container we prepare Dockerfile
  publish_path  = "."
  auto_deploy   = true

}

output "site_url" {
  value = render_static_site_test.example.url
}