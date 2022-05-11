import pytest


# smoke here is word used to group test cases, we can give any name instead of smoke
# using xfail mark, the test case will run, but it won't report any failing error
@pytest.mark.smoke
@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    print(msg)
    assert msg == "Hi", "Test failed strings did not match"


# it is a predefined mark in python, when we mark any test case with skip then python will skip that test case
@pytest.mark.skip
def test_SecondProgram():
    print("Second Method file 2")
