from prompts import build_prompt
from utils import is_valid_question


def test_build_prompt_contains_question():
    question = "What documents do I need to study in Canada?"

    prompt = build_prompt(question)

    assert question in prompt


def test_valid_question():
    assert is_valid_question("What is a student visa?")


def test_empty_question():
    assert not is_valid_question("")


def test_spaces_are_invalid():
    assert not is_valid_question("   ")