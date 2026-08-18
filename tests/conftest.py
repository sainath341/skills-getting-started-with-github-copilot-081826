from copy import deepcopy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def restore_activities():
    initial_activities = deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_activities))
