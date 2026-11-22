"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import marktweak


def test_version_is_set() -> None:
    assert marktweak.__version__
