# furigana

Generate furigana(振り仮名) for Japanese text.

It uses [Fugashi](https://github.com/polm/fugashi),
a [MeCab](https://taku910.github.io/mecab/) wrapper,
to split Japanese into words, and superscript it with furigana (振り仮名).

This repository is forked from [MikimotoH/furigana](https://github.com/MikimotoH/furigana).

## Usage

From python:
```python
import furigana

furigana.get_html("食べる")
'<ruby><rb>食</rb><rt>た</rt></ruby>べる'

furigana.get_plaintext('澱んだ街角で僕らは出会った')
'澱(よど)んだ街角(まちかど)で僕(ぼく)らは出(で)会(あ)った'

furigana.get_plaintext_for_anki('澱んだ街角で僕らは出会った')
'澱[よど]んだ街角[まちかど]で僕[ぼく]らは出[で]会[あ]った'
```

From command line:

```shell
python -m furigana 食べる
<ruby><rb>食</rb><rt>た</rt></ruby>べる

python -m furigana 食べる -f plaintext
食(た)べる

python -m furigana 食べる -f anki
食[た]べる

python -m furigana 食べる -h
 usage: Furigana [-h] [-f {html,plaintext,anki}] text
 
 Adds furigana to the given Japanese text
 
 positional arguments:
   text
 
 options:
   -h, --help            show this help message and exit
   -f {html,plaintext,anki}, --format {html,plaintext,anki}
                         Output format
```
