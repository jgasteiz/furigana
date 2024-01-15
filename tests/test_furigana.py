import furigana
import pytest


@pytest.mark.parametrize(
    "text,expected",
    [
        ["食べる", "食(た)べる"],
        # 聞き耳 is a problematic one, the current implementation fails
        # to split the okurigana, so we just return the whole thing
        # and its furigana rather than 聞(き)き耳(みみ)
        ["聞き耳", "聞き耳(ききみみ)"],
        ["聞き耳食べる", "聞き耳(ききみみ)食(た)べる"],
    ],
)
def test_get_plaintext(text: str, expected: str):
    assert furigana.get_plaintext(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ["食べる", "食[た]べる"],
    ],
)
def test_get_plaintext_for_anki(text: str, expected: str):
    assert furigana.get_plaintext_for_anki(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ["食べる", "<ruby><rb>食</rb><rt>た</rt></ruby>べる"],
    ],
)
def test_get_html(text: str, expected: str):
    assert furigana.get_html(text) == expected
