#!/usr/bin/env python3
import typing
import unicodedata

import fugashi
import jaconv
import unidic


def get_html(text: str) -> str:
    html = ""
    for chars, furigana in _split_furigana(text):
        if furigana:
            html = f"{html}<ruby><rb>{chars}</rb><rt>{furigana}</rt></ruby>"
        else:
            html = f"{html}{chars}"
    return html


def get_plaintext(text: str) -> str:
    plaintext = ""
    for chars, furigana in _split_furigana(text):
        if furigana:
            plaintext = f"{plaintext}{chars}({furigana})"
        else:
            plaintext = f"{plaintext}{chars}"
    return plaintext


def get_plaintext_for_anki(text: str) -> str:
    plaintext = ""
    for chars, furigana in _split_furigana(text):
        if furigana:
            plaintext = f"{plaintext}{chars}[{furigana}]"
        else:
            plaintext = f"{plaintext}{chars}"
    return plaintext


class _UnableToSplitOkurigana(Exception):
    """
    Exception raised when something bad happens trying to split an okurigana.
    """


def _split_okurigana_reverse(
    text: str, hiragana: str
) -> typing.Iterator[tuple[str, str | None]]:
    """
    tested:
      お茶(おちゃ)
      ご無沙汰(ごぶさた)
      お子(こ)さん
    """
    yield text[0], None
    yield from _split_okurigana(text[1:], hiragana[1:])


def _split_okurigana(
    text: str, hiragana: str
) -> typing.Iterator[tuple[str, str | None]]:
    """送り仮名 processing
    tested:
       * 出会(であ)う
       * 明(あか)るい
       * 駆(か)け抜(ぬ)け
    """
    original_text_ = text
    if _is_hiragana(text[0]):
        yield from _split_okurigana_reverse(text, hiragana)
    if all(_is_kanji(_) for _ in text):
        yield text, hiragana
        return
    text = list(text)
    ret = (text[0], [hiragana[0]])
    for hira in hiragana[1:]:
        for char in text:
            if hira == char:
                text.pop(0)
                if ret[0]:
                    if _is_kanji(ret[0]):
                        yield ret[0], "".join(ret[1][:-1])
                        yield ret[1][-1], None
                    else:
                        yield ret[0], None
                else:
                    yield hira, None
                ret = ("", [])
                if text and text[0] == hira:
                    text.pop(0)
                break
            else:
                if _is_kanji(char):
                    if ret[1] and hira == ret[1][-1]:
                        text.pop(0)
                        yield ret[0], "".join(ret[1][:-1])
                        yield char, hira
                        ret = ("", [])
                        try:
                            text.pop(0)
                        except IndexError:
                            raise _UnableToSplitOkurigana(original_text_)
                    else:
                        ret = (char, ret[1] + [hira])
                else:
                    # char is also hiragana
                    if hira != char:
                        break
                    else:
                        break


def _split_furigana(text: str) -> typing.Iterator[tuple[str, str | None]]:
    """
    Split the text into tuples of kanji/furigana
    """
    node_list = _get_tagger().parseToNodeList(text)

    for node in node_list:
        if not node.surface:
            continue

        if node.feature.kana and any(_is_kanji(_) for _ in node.surface):
            hiragana = jaconv.kata2hira(node.feature.kana)

            # If something fails while trying to split the okurigana,
            # return the node and its hiragana as-is.
            node_split = []
            try:
                for pair in _split_okurigana(node.surface, hiragana):
                    node_split.append(pair)
            except _UnableToSplitOkurigana:
                yield node.surface, hiragana
            else:
                yield from node_split
        else:
            yield node.surface, None


def _is_kanji(ch: str) -> bool:
    return "CJK UNIFIED IDEOGRAPH" in unicodedata.name(ch)


def _is_hiragana(ch: str) -> bool:
    return "HIRAGANA" in unicodedata.name(ch)


_tagger: fugashi.Tagger | None = None


def _get_tagger() -> fugashi.Tagger:
    global _tagger
    if _tagger is None:
        _tagger = fugashi.Tagger(f"-d {unidic.DICDIR}")
    return _tagger
