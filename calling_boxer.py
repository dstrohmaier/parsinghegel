from subprocess import Popen, PIPE

import logging
import nltk

def parse(tokenized):
    parser_options = ['--models', 'parser/models/boxer',
                      '--candc-printer', 'boxer'] # depends on installation
    
    parser = ['parser/bin/candc'] # depends on installation

    process = Popen(parser + parser_options,
                               shell=False,
                               stdin=PIPE,
                               stdout=PIPE,
                               stderr=PIPE)
    out, err = process.communicate(tokenized.encode("utf-8"))
    
    if err:
        # ignores info C&C writes to stderr
        if not err.startswith(b'#'):
            logging.error('Parser error: {0}'.format(err))
    parsed = out.decode('utf-8')
    return parsed


def box(parsed, out_format="xml"):
    boxer = ['parser/bin/boxer'] # depends on installation
    
    boxer_options = ['--stdin',
                     '--instantiate', 'true',
                     '--resolve', 'true',
                     '--semantics', 'drs',
                     '--theory', 'drt',
                     '--roles', 'verbnet',
                     '--format', out_format]


    process = Popen(boxer + boxer_options,
                               shell=False,
                               stdin=PIPE,
                               stdout=PIPE,
                               stderr=PIPE)
    out, err = process.communicate(parsed.encode("utf-8"))

    if err:
        # we ignore an error Boxer throws wrongly
        if not b"No source location" in err:
            logging.error('Boxer error: {0}'.format(err))
    boxed = out.decode('utf-8').encode("utf-8")

    return boxed


def box_sent(sent):
    tokenized = " ".join(nltk.word_tokenize(sent))
    tokenized += "\n<EOF>"
    #print(tokenized)
    parsed = parse(tokenized)
    #print(parsed)
    boxed_xml = box(parsed)
    boxed_latex = box(parsed, out_format="latex")
    
    return boxed_xml, boxed_latex
