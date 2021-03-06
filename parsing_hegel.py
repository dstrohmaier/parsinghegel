from pathlib import Path

from calling_boxer import box_sent

BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR.joinpath("data")


def parse_intro():
    intro_path = DATA_DIR.joinpath("first_sentences_intro.txt")
    with intro_path.open(mode="r") as in_file: # accommodates versions <3.6
        parse_results = [box_sent(line) for line in in_file]

    return parse_results



if __name__ == "__main__":
    for i, (parsed_xml, parsed_latex) in enumerate(parse_intro()):
        print("Sentence #{}".format(i)) # Would be nicer with f-string, but need to accommodate python versions <3.6
        print("\nXML-output")
        print(parsed_xml.decode("utf-8"))
        print("\nLaTex-output")
        print(parsed_latex.decode("utf-8"))
        print("********\n")
        
    
