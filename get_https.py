#!/usr/bin/env python
import requests

r = requests.get("http://0.0.0.0:5000/")

print(r.status_code)
print(r.headers)
print(r.content)
