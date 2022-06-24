from base64 import b64encode
from locust import HttpUser, task
from random import randint, choice


class WebUser(HttpUser):

    @task
    def load(self):
        # user: foo, password: bar
        user_pass = b64encode(b"foo:bar").decode("ascii")
        catalogue = self.client.get("/catalogue").json()
        category_item = choice(catalogue)
        item_id = category_item["id"]

        self.client.get("/")
        self.client.get("/login", headers={"Authorization":"Basic %s" % user_pass})
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.delete("/cart")
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        self.client.get("/basket.html")
        self.client.post("/orders")

