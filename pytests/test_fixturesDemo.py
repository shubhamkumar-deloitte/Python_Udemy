import pytest


def test_firstProgram():
    msg = "Hello"
    print(msg)
    assert msg == "Hello", "Test failed strings did not match"


# it is a predefined mark in python, when we mark any test case with skip then python will skip that test case
@pytest.mark.skip
def test_SecondProgram():
    print("Second Method file 2")


@pytest.mark.usefixtures("setUp")  # the following set up run setUp and yield before and after every test case
class TestExample:

    def test_fixtures1(self):
        print("after setUp 1")

    def test_fixtures2(self):
        print("after setUp 2")

    def test_fixtures3(self):
        print("after setUp 3")

    def test_fixtures4(self):
        print("after setUp 4")


@pytest.mark.usefixtures("setUpOnce")  # the following set up run setUp once in the beginning
                                        # and yield part at the last after all the test cases is executed
class TestExampleOnce:

    def test_fixtures1(self):
        print("after setUp 1")

    def test_fixtures2(self):
        print("after setUp 2")

    def test_fixtures3(self):
        print("after setUp 3")

    def test_fixtures4(self):
        print("after setUp 4")
