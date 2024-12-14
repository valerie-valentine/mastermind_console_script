import pytest
from model.game import Game
from model.guess import Guess


def test_game_initialization():
    # arrange & act
    game = Game(4)

    # assert
    assert game.lives == 10
    assert game.previous_guesses == []
    assert game.game_status == "In Progress"


def test_game_generates_answer_for_different_levels():
    # arrange
    levels = {"easy": 4, "medium": 6, "hard": 8}

    # act
    for level_digits in levels.values():
        game = Game(level_digits)
        game.generate_answer()

        # assert
        assert len(game.answer) == level_digits
        assert isinstance(game.answer, str)


def test_submit_wrong_guess():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("1111")
    initial_lives = game.lives

    # act
    game.submit_user_guess(guess)

    # assert
    assert any(guess.guess_value == "1111" for guess in game.previous_guesses)
    assert game.lives == initial_lives - 1
    assert game.game_status == "In Progress"


def test_judge_guess_all_correct():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("1234")

    # act
    guess.judge_guess(game.answer)

    # assert
    assert guess.correct_number == 4
    assert guess.correct_location == 4
    assert isinstance(guess.correct_number, int)
    assert isinstance(guess.correct_location, int)
    assert guess.correct_number is not None
    assert guess.correct_location is not None


def test_judge_guess_not_all_correct():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("0000")

    # act
    guess.judge_guess(game.answer)

    # assert
    assert guess.correct_number == 0
    assert guess.correct_location == 0
    assert isinstance(guess.correct_number, int)
    assert isinstance(guess.correct_location, int)
    assert guess.correct_number is not None
    assert guess.correct_location is not None


def test_judge_guess_partially_correct():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("7130")

    # act
    guess.judge_guess(game.answer)

    # assert
    assert guess.correct_number == 2
    assert guess.correct_location == 1
    assert isinstance(guess.correct_number, int)
    assert isinstance(guess.correct_location, int)
    assert guess.correct_number is not None
    assert guess.correct_location is not None


def test_judge_guess_with_repeated_digits_only():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1135"
    guess = Guess("2211")

    # act
    guess.judge_guess(game.answer)

    # assert
    assert guess.correct_number == 2
    assert guess.correct_location == 0
    assert isinstance(guess.correct_number, int)
    assert isinstance(guess.correct_location, int)
    assert guess.correct_number is not None
    assert guess.correct_location is not None


def test_judge_guess_with_repeated_digits_only_and_correct_location():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1135"
    guess = Guess("1122")

    # act
    guess.judge_guess(game.answer)

    # assert
    assert guess.correct_number == 2
    assert guess.correct_location == 2
    assert isinstance(guess.correct_number, int)
    assert isinstance(guess.correct_location, int)
    assert guess.correct_number is not None
    assert guess.correct_location is not None


def test_judge_guess_correct_digits_wrong_location():
    # arrange
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("4321")

    # act
    guess.judge_guess(game.answer)

    # assert
    assert guess.correct_number == 4
    assert guess.correct_location == 0
    assert isinstance(guess.correct_number, int)
    assert isinstance(guess.correct_location, int)
    assert guess.correct_number is not None
    assert guess.correct_location is not None


def test_game_is_won():
    # act
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("1234")

    # arrange
    game.submit_user_guess(guess)

    # assert
    assert game.game_status == "Won"


def test_game_is_loss():
    # act
    level = 4
    game = Game(level)
    game.answer = "1234"
    guess = Guess("7130")
    game.lives = 1

    # arrange
    game.submit_user_guess(guess)

    # assert
    assert game.game_status == "Loss"
    assert game.lives == 0
