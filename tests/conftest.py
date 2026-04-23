"""
Pytest configuration and shared fixtures for the Flask application tests.
"""
from config import TestingConfig
from run import create_app
import sys
from pathlib import Path

import pytest

# Add the parent directory to the path so we can import the app
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def app():
    """Create a Flask app configured for testing."""
    app = create_app()
    app.config.from_object(TestingConfig)

    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()
