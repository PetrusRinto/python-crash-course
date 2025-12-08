# Patrick 08.12.2025.
# 11-3 Employee test file.

from employee import Employee

def test_give_default_raise():
    """Testing the default salary raise value."""
    employee = Employee('roberta', 'bot', 100000)
    default_raise = employee.give_raise()
    assert default_raise == 105000

def test_give_custom_raise():
    """Testing the custom salary raise."""
    employee = Employee('roberta', 'bot', 100000)
    custom_raise = employee.give_raise(100000)
    assert custom_raise == 200000