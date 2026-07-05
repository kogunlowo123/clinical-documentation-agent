"""Test configuration for Clinical Documentation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "clinical-documentation-agent", "category": "Healthcare"}
