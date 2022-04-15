import pytest
from plain_python_package.incrementer import increment


def test_increment():
    """
    Show how the increment function operates.
    """
    # Show acceptable cases
    assert increment(1) == 2
    assert increment("1") == 2
    assert increment("-112") == -111

    # Show that we can gracefully handle an error.
    with pytest.raises(ValueError):
        increment("trash")
