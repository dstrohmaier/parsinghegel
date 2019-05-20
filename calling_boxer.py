from subprocess import Popen, PIPE

import nltk

def parse(tokenized):
    parser_options = ['--models',
                      'parser/models/boxer'] # depends on installation
    
    parser = ['parser/bin/candc'] # depends on installation

    process = Popen(parser + parser_options,
                               shell=False,
                               stdin=PIPE,
                               stdout=PIPE,
                               stderr=PIPE)
    out, err = process.communicate(tokenized.encode("utf-8"))
    
    if err:
        # ignores info C&C writes to stderr
        if not err.startswith('#'):
            log.error('Parser error: {0}'.format(err))
    parsed = out.decode('utf-8').encode("utf-8")
    return parsed


def box(parsed):
    boxer = ['parser/bin/boxer'] # depends on installation
    
    boxer_options = ['--stdin',
                     '--instantiate', 'true',
                     '--resolve', 'true',
                     '--semantics', 'drs',
                     '--format', 'xml']


    process = Popen(boxer + boxer_options,
                               shell=False,
                               stdin=PIPE,
                               stdout=PIPE,
                               stderr=PIPE)
    out, err = process.communicate(parsed.encode("utf-8"))

    if err:
        # we ignore an error Boxer throws wrongly
        if not "No source location" in err:
            log.error('Boxer error: {0}'.format(err))
    boxed = out.decode('utf-8').encode("utf-8")

    return boxed


def box_sent(sent):
    tokenized = " ".join(nltk.word_tokenize(sent))
    parsed = parse(tokenized)
    boxed = box(parsed)
