
from portfolio_engine import calculate_progress, customer_health


def test_progress_75_percent():
    assert calculate_progress(3, 4) == 75


def test_progress_zero_tasks():
    assert calculate_progress(0, 0) == 0


def test_progress_half_complete():
    assert calculate_progress(2, 4) == 50


def test_customer_fully_onboarded():
    assert customer_health(100) == "Fully onboarded"


def test_customer_on_track():
    assert customer_health(75) == "On track"


def test_customer_needs_attention():
    assert customer_health(50) == "Needs attention"


def test_customer_at_risk():
    assert customer_health(25) == "At risk"
