import aquerytest
import pytest
import time


def test_aquerytest():
    """Test aquerytest."""
    tester = aquerytest.AQueryTest()
    table = tester.run()
    print(table)

    with pytest.raises(RuntimeError):
        _ = tester.run_fail()

    time.sleep(600)

    table = tester.run()
    print(table)
