import pytest


@pytest.mark.usefixtures("dataload")
class TestExample2:

    def test_editProfile(self, dataload):
        print(dataload)  # if we want print any index then print(dataload[0])
        print(dataload[2])


# @pytest.mark.usefixtures("crossBrowser")
def test_crossBrowser(crossBrowser):
    print(crossBrowser)  # print chrome, IE-> from conftest file crossBrowser fixture


def test_crossBrowser2(crossBrowser2):
    print(crossBrowser2["name"])  # it will print ('shubham', 'paddu') and then fail for two iteration bcz they are tuples not map




