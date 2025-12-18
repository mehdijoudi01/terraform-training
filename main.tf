terraform {
  required_version = ">= 1.0"
  required_providers {
    render = {
      source  = "registry.terraform.io/render-oss/render"
      version = "~> 1.0"
    }
  }
}

provider "render" {
}

resource "render_static_site" "example" {
  name          = "render-terraform-example-try6"
  repo_url      = "https://github.com/mehdijoudi01/terraform-training"
  branch        = "main"
  build_command = "" # no build needed for html file, ---- ken 3ana container we prepare Dockerfile
  publish_path  = "."
  auto_deploy   = true

}

output "site_url" {
  value = render_static_site.example.url
}