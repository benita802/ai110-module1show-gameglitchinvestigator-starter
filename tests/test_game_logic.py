from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_direction_points_the_right_way():
    """Regression test for the swapped high/low hint bug.

    A guess that is too high must tell the player to go LOWER, and a
    guess that is too low must tell the player to go HIGHER. The bug
    returned these messages reversed.
    """
    _outcome_high, message_high = check_guess(60, 50)
    assert "LOWER" in message_high
    assert "HIGHER" not in message_high

    _outcome_low, message_low = check_guess(40, 50)
    assert "HIGHER" in message_low
    assert "LOWER" not in message_low
