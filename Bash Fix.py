import requests
import os 
import json

student_name = input("What is your first name? ")
#agify
agify_url = f"https://api.agify. io/?name={student_name}"
agify_get = requests.get(agify_url)
agify_data = agify_get.json ( )
print(agify_data)

#Terraform
latest_tf_url = "https://releases.hashicorp.com/terraform/1.1.7/terraform_1.1.7_linux_amd64.zip"
filename = latest_tf_url.split("/")[-1]
try:
    if not os.path.exists(filename):
        tf_get = requests.get (latest_tf_url, allow_redirects=True)
        open(filename, "wb").write(tf_get.content)
        print(f"Successfully downloaded Terraform {filename}" )
    else:
        print(f"Terraform {filename} already exists!")
except Exception as e:
    print(f"Error occurred while downloading Terraform: {e}")

print( "That's all folks!")
