def Check_guess(guess,answer):
    return None

def test_check_guess_correct():
    guess = 9
    check=9

    result = Check_guess(guess,check)
    assert result == 0