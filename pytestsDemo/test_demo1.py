# Any pytest file should start with test_
#pytest method names should start with test
import pytest


#py.test test_demo2.py -v -s
#py.test -v -s
#py.test -k CreditCard -v -s

# -k stands for method names execution ,-s logs in out put -v stands for more info metadata
#you can run specific file with py.test <filename>
# you can mark (tag)  tests @pytest.mark.smoke and then run with -m
#py.test -m smoke -v -s
# you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
# fixtures are used for setup and tear down methods for test cases --conftest file to generalize
#fixture will be available to all test cases (fixture name into parameters of method)
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only , it will run once before class is initiated and at the end
# xfail is for running but not reporting

#  @pytest.fixture()    related to Hooks

# conftest.py is global file


@pytest.fixture()
def setup():
    print("I will execute first")


def test_fixturedemo(setup):
    print("I will execute steps in fixtureDemo method")

@pytest.mark.smoke
@pytest.mark.skip
@pytest.mark.xfail
def test_firstprogram():
    print("Hello")


def test_firstprogram1():
    print("Hello")
    msg = "Hello"
    assert msg == "test"


def test_crossbrowser(crossbrowser):
    print(crossbrowser)
