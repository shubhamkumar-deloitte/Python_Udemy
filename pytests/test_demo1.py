import pytest


def test_firstProgram():
    print("Hello")


# smoke here is word used to group test cases, we can give any name instead of smoke
@pytest.mark.smoke
def test_SecondProgram():
    print("Second Method")
