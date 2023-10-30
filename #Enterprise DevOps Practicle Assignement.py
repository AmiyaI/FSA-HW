#Enterprise DevOps Practicle Assignement - Amiya Islam

import requests
import os
import json

student_name = input("What is your first name? ")
#agify
agify_url = f"https://api.agify.io/?name={student_name}"
agify_get = requests.get(agify_url)
agify_data = agify_get.json()
print(agify_data)

#Terraform
tf_url = "https://releases.hashicorp.com/terraform/index.json"
try:
    tf_get = requests.get(tf_url)
    tf_data = tf_get.json()
    urls = [b["url"] for v in tf_data["versions"].values() for b in ["builds"] if "rc"
not in b["name"] and "beta" not in b["name"] and "linux" in b["name"] and "amd64" in b["name" ]]
    if not urls:
        raise ValueError("No Terraform URLs found that match the specified criteria")
    latest_tf_url = max(urls)
    filename = latest_tf_url.split("/")[-1]
    tf_get = requests.get(latest_tf_url, allow_redirects=True)
    open(filename, "wb").write(tf_get.content)
    print(f"Successfully downloaded Terraform {filename}")
except Exception as e:
    print(f"Error occurred while downloading Terraform: {e}")

print("That's all folks!")
