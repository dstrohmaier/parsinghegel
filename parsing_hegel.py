from pathlib import Path

from calling_boxer import box_sent

BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR.joinpath("data")


def parse_intro():
    intro_path = DATA_DIR.joinpath("first_sentences_intro.txt")
    with intro_path.open(mode="r") as in_file: # accommodates versions <3.6
        text = in_file.read() # It is just one line

    intro_parsed = box_sent(text)
    return intro_parsed



if __name__ == "__main__":
    print(parse_intro())
    
