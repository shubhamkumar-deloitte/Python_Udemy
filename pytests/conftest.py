import pytest


@pytest.fixture()
def setUp():
    print("executing the setup")
    yield  # whatever in yield will act like teardown and will be executed at the last
    print("fixtures demo completed")


@pytest.fixture(scope="class")
def setUpOnce():
    print("executing the setup")
    yield  # whatever in yield will act like teardown and will be executed at the last
    print("fixtures demo completed")


@pytest.fixture()
def dataload():
    return ["Rahul", "shetty", "qdjhd.com"]


@pytest.fixture(params=["chrome", "IE"])
def crossBrowser(request):  # request is fixed can't use anything else
    return request.param


@pytest.fixture(params=[({"name": ("shubham", "paddu")}), ("nextparam","firstindex_1"), ("thordparam","firstindex_2")])
def crossBrowser2(request):  # request is fixed can't use anything else
    return request.param
