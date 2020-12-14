# request_test.py
# Read and get information from http

import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# raise an error if there is one

response.raise_for_status()

# Create a variable to store the file
f = open("Romeo_and_Juliet.txt", "wb")

# Grab info from http and save it in the variable
for chunk in response.iter_content(1000000):
    f.write(chunk)

# Write the file to disk
f.close()