import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rahul","Shetty","Naresh"]


@pytest.fixture(params=[("chrome","Rahul"),"firefox","IE"])
def crossbrowser(request):
    return request.param