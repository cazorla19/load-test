# Load / Integration Tests

These tests simulate actual end user usage of the application. They are used to validate the overall functionality and can also be used to put simulated load on the system. The tests are written using [locust.io](http://locust.io)

## Running locally

### Running on workstation's namespace

```
pip install locust
locust --headless --users 10 --spawn-rate 1 -H http://host.name
```


### Running in Docker

```
docker run -it --rm -v ${PWD}/:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py --headless --users 10 --spawn-rate 1 -H http://host.name
```
