import os
import sys

# Add project root to sys.path so tests can import modules from app root.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go HIGHER!")

def test_guess_string_secret_regression():
    # Previously a type-comparison problem occurred when secret is str
    result = check_guess(50, "50")
    assert result[0] == "Win"


def test_get_range_for_difficulty_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_difficulty_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_get_range_for_difficulty_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_get_range_for_difficulty_unknown_falls_back():
    assert get_range_for_difficulty("Unknown") == (1, 50)

