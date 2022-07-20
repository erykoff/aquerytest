import aquerytest
import pytest


def test_aquerytest():
    """Test aquerytest."""
    tester = aquerytest.AQueryTest()
    table = tester.run()
    print(table)

    with pytest.raises(RuntimeError):
        _ = tester.run_fail()
