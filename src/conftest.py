import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: Tests that are very slow.")


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        return

    skip_slow = pytest.mark.skip(reason="it takes time")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
