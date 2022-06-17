
import pytest

@pytest.fixture
def first_video_info():
    return {
        "path": "SomePath",
        "name": "First Video",
        "time": "SomeTime"
    }