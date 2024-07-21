# PyTest
Testing framework for unit tests.

#### Install
Install with pip: ```% pip install -U pytest```

### Setup
pytest will run all files with the name “test_*.py” or “*_test.py” in the current and sub directories
- follow simple example: https://docs.pytest.org/en/7.3.x/getting-started.html

### Execute 
From command line
1. Execute all test cases in directory ```/dir/tests/ ~ % pytest```
2. Additional arguments ```% pytest —help```
3. Verbose ```% pytest -v```
4. Statements (from scripts) ```% pytest -s```
5. Execute specific test file ```% specifc_test.py```

## Marks
- Method to group tests.
- Allows execution of subsets of tests within a single directory
- Mark specific test with keyword
- Triggered in command line by argument -m
- Build-in marks  ```% pytest --help```
    1. skip: skip a test
    2. skipif(conditional)
    3. xfail: fail a specific tests
    4. xpass

```python
from pytest import mark

@mark.group_a
def test_A():
    print(‘one’)
```
Execute: ```% pytest -m group_a```

## Fixtures
- For setup and teardown of testing. Steps 1, 2, 4 below.
- Executed and pre and post conditions of fixture.
- Split by “yield” in function with @fixture decorator.

Testing breakdown
1. Arrange: setup steps for testing to occur.
2. Act: Action to be tested
3. Assert: Verify action completed successfully
4. Cleanup

```python
import pytest.fixture as fixture

@fixture
def setup():
    print(“startup”)
    yield
    print(“shutdown”)

def test_A(setup):
    print(“testing complete”)
```

### Conftest.py
- Separate configuration file for common methods across test cases. 
- Place to put @fixture methods which may be used by multiple files.
- To eliminate need to pass @fixture method as argument (autouse=True)
```python
# contents of conftest.py

@fixture(autouse=True)
def setup():  # will run without fixture name being passed
    print(“startup”)
    yield
    print(“shutdown”)
```

### Fixture scopes
- Fixtures are created when first requested by a test, and are destroyed based on their scope.
- Teardown is everything after “yield”

Scopes
1. function: default, destroyed at end of test
2. class: destroyed during teardown of the last test in the class
3. module: destroyed during teardown of the last test in the module
4. package: destroyed during teardown of the last test in the package
5. session: destroyed during teardown at end of test session

```python
# contents of conftest.py

@fixture(autouse=True, scope=session)
def setup():  # teardown only run at end of session.
print(“startup”)
yield
print(“shutdown”)
```

### Parameterize fixtures and test functions
Allows definition of parameters which can be used sequentially
Parametreize options:
    1. fixture
    2. marker
    3. generate_test

#### parameterize with fixture

```python
# contents of conftest.py
from pytest import mark

@fixture(params=["a", "b"])  # will execute with sequence of a and b parameters
def fixture_a(request)
    print(request.param)

# contents of test_file.py
def test_a(fixture_a):
    print("passed")
```

#### parameterize with mark

```python
# contents of test_file.py
from pytest import mark

@mark.parametrize(params=["a, b answer", [(2, 6, 8), (4, 1, 5)])  # will execute with sequence of a and b parameters
def test_a(a, b, answer):
    assert a + b == answer
```

#### pytest_generate_test
- continue if needed
