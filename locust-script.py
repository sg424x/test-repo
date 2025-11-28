from locust import HttpUser, task, between
import json
import uuid

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task(8)
    def get_all_items(self):
        self.client.get("items/")

    @task(4)
    def get_item_by_id(self):
        self.client.get("items/1/")

    @task(1)
    def create_item(self):
        name = str(uuid.uuid1())
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        self.client.post('/items',data= json.dumps({
                  "id": name,
                  "name": "load test"
        }),
        headers=headers,
        name = "Create a new item")
# locust -f locust-script.py -H ${ApiUrl} --headless -u 100 -r 5 -t 10m