from pathlib import Path

from calling_boxer import box_sent

BASE_DIR = Path(__file__).resolve().parent()
DATA_DIR = BASE_DIR.join("data")


def parse_intro():
    intro_path = DATA_DIR.join("first_sentences.txt")
    with open(intro_path) as in_file:
        text = in_file.read() # It is just one line

    intro_parsed = box_sent(text)
    return intro_parsed



if __name__ == "__main__":
    parse_intro()
