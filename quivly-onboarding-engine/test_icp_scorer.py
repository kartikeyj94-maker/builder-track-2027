from icp_scorer import score_company_size, score_industry,  score_geography, score_buying_signal, calculate_icp_score, classify_lead

def test_minimum_company_size():
    assert score_company_size(50) == 30


def test_maximum_company_size():
    assert score_company_size(500) == 30


def test_company_below_minimum():
    assert score_company_size(49) == 0


def test_company_above_maximum():
    assert score_company_size(501) == 0

def test_target_industry():
    assert score_industry("B2B SaaS") == 30

def test_non_target_industry():
    assert score_industry("Manufacturing") == 0

def test_target_geography():
    assert score_geography("United States") == 20

def test_non_target_geography():
    assert score_geography("India") == 0

def test_hiring_signal_present():
    assert score_buying_signal(True) == 20

def test_hiring_signal_absent():
    assert score_buying_signal(False) == 0

def test_perfect_icp_match():
    score = calculate_icp_score(
        120, "B2B SaaS", "United States", True
    )
    assert score == 100

def test_no_icp_match():
    score = calculate_icp_score(
        1000, "Manufacturing", "India", False
    )
    assert score == 0

def test_high_priority_boundary():
    assert classify_lead(80) == "High"

def test_medium_priority_boundary():
    assert classify_lead(50) == "Medium"

def test_low_priority_boundary():
    assert classify_lead(49) == "Low"