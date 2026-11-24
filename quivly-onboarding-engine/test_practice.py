
def calculate_progress(completed, total):
    if total == 0:
        return 0
    return (completed / total) * 100


def test_progress():
    assert calculate_progress(3, 4) == 75
    assert calculate_progress(2, 4) == 50
    assert calculate_progress(4, 4) == 100
    assert calculate_progress(0, 0) == 0


def test_zero_completed():
    assert calculate_progress(0, 5) == 0


def test_half_completed():
    assert calculate_progress(5, 10) == 50
