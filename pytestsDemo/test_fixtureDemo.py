import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixturedemo(self):
        print("I will execute steps in fixtureDemo method")
    def test_fixturedemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixturedemo3(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixturedemo4(self):
        print("I will execute steps in fixtureDemo method")