import os

print("I print out the secret password")
if "SECRET_PASSWORD" in os.environ:
    print(os.environ["SECRET_PASSWORD"])
else:
    print("No SECRET_PASSWORD found")    