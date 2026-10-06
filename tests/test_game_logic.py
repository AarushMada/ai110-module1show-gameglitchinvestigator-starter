from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_guess_one_above_secret_is_too_high():
    """Regression test: a close guess must still receive the correct direction."""
    assert check_guess(51, 50) == "Too High"


def test_negative_guess_is_rejected():
    ok, value, error = parse_guess("-1", 1, 100)

    assert ok is False
    assert value is None
    assert error == "Guess must be between 1 and 100."


def test_decimal_guess_is_rejected():
    ok, value, error = parse_guess("12.5", 1, 100)

    assert ok is False
    assert value is None
    assert error == "Enter a whole number."


def test_extremely_large_guess_is_rejected():
    ok, value, error = parse_guess("999999999999999999999999", 1, 100)

    assert ok is False
    assert value is None
    assert error == "Guess must be between 1 and 100."
