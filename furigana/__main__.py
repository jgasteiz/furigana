import argparse

import furigana

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Furigana",
        description="Adds furigana to the given Japanese text",
    )
    parser.add_argument("text")
    parser.add_argument(
        "-f",
        "--format",
        help="Output format",
        default="html",
        dest="format",
        choices=["html", "plaintext", "anki"],
    )
    args = parser.parse_args()

    if args.format == "html":
        output = furigana.get_html(args.text)
    elif args.format == "plaintext":
        output = furigana.get_plaintext(args.text)
    elif args.format == "anki":
        output = furigana.get_plaintext_for_anki(args.text)
    else:
        raise ValueError(f"Unknown format: {args.format}")

    print(output)
