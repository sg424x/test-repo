from locust import HttpUser, task, between
import json
import uuid

class MyUser(HttpUser):
    wait_time = between(1, 3)

    def create_name(self):
        self.name = str(uuid.uuid1())

    @task(1)
    def index(self):
        self.client.get("items/")
        self.client.get("items/")
        self.client.get("items/")

# locust -f locust-script.py -H ${ApiUrl} --headless -u 500 -r 100 -t 1m
        