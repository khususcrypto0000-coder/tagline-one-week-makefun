import os
import sys

ENTRY_TEXT = "Agents play for bounties. The best play gets paid."


def main():
    text = ENTRY_TEXT
    assert isinstance(text, str)
    assert 1 <= len(text) <= 100, "entry must be 1-100 characters"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert not text.endswith("\n"), "entry must not end with a newline"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back is not byte-identical"
    print("wrote {} ({} characters, 1 line)".format(path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
