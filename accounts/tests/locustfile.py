from locust import HttpUser, TaskSet, task, between


#Load tests for the user 
class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def homepage(self):
        self.client.get("http://www.gradrotate.uk/")

    @task(5)
    def register(self):
        self.client.get("http://www.gradrotate.uk/register")

#locust -f accounts/tests/locustfile.py -H http://www.gradrotate.uk/ -u 3 -r 1