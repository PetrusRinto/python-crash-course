# Patrick 08.12.2025.
# 11-3 Employee test file.

from employee import Employee
import pytest

@pytest.fixture
def employee():
    """Representation of employee's name and annual salary."""
    employee = Employee('roberta', 'bot', 100000)
    return employee

def test_give_default_raise(employee):
    """Testing the default salary raise value."""
    default_raise = employee.give_raise()
    assert default_raise == 105000

def test_give_custom_raise(employee):
    """Testing the custom salary raise."""
    custom_raise = employee.give_raise(100000)
    assert custom_raise == 200000