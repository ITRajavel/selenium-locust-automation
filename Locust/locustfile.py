
from locust import HttpUser, task, between

class FakeStoreApiUser(HttpUser):
    wait_time = between(1, 2)  # wait for 1-2 seconds between requests

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def products(self):
        self.client.get("/products")

    @task(1)
    def product(self):
        self.client.get("/products/1")