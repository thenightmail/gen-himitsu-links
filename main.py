import anki
import genanki
from py_fumen_py import *
import subprocess
import os
TEST_MODEL = genanki.Model(
  234567, 'foomodel',
  fields=[
    {
      'name': 'AField',
    },
    {
      'name': 'BField',
    },
  ],
  templates=[
    {
      'name': 'card1',
      'qfmt': '{{AField}}',
      'afmt': '{{FrontSide}}'
              '<hr id="answer">'
              '{{BField}}',
    }
  ],
)
fumen = 'v115@vh/SSYoBFLDmClcJSAVDEHBEooRBMoAVBznFgCqujx?CJ3TWCqyaPCpX+tC6vKWCJNOMCv+jFDsvytCqX8LCUXNFDK?NWWCvvTxC6SNFDKd9VCvujxCTXNPCsS9wCvvjFDq+bgCa+L?gCXsBMoBTpB2kBliBRmBMrBRlBTqB9tBKpBXjB6kB+qBOlB?xhB0sBNrBzrBvtBGjB0sBCrBZkBzpBFrBRmBzkBHsBvtB0s?BqrBGjBTpB3qBmkBdrBEsBxuBSyBznBNpB0fBGjBXqB9rBJ?nB6qBOrBXqBNpB0fBSyBznBJnBGjBUmBxlBSwB3pBNkBUgB?1vBvhPvrBTtBTjBGhBKsB6sBZkBpkBzqBOqBtrBUtBmgB9o?B3nBTfB'
pages = decode(fumen)

for i, page in enumerate(pages):
    #print(i)
    # let queue be page.comment
    # remove all 'Q', '#', '[', ']', '=', '(', ')' from the queue
    # remove all text after the 11th character
    # insert a comma after each letter
    # let link be the himitsu link with the queue appended to it
    # run the node command fumen-canvas.js gif fumen format(i + '.gif') --start i --end i+10
    # add to 10 to i.
    if i % 10 == 0:
        print(page.comment)
        command = 'echo node fumen-canvas.js gif ' + fumen + ' ' + str(i) + '.gif' + ' --start ' + str(i) + ' --end ' + str(i+10)
        os.system(command)
        queue = "TODO queue" # the queue
        print(queue)
        save = "TODO save" # the piece that we save into the next PC
        print(save)


# TODO figure out how to generate the gifs for each perfect clear
# TODO figure out how to add himitsu cards fo each perfect clear in a fumen
# TODO figure out how to add the correct gif to each card
# TODO figure out how to parse the comment and correctly format the link
# node fumen-canvas.js gif v115@vhKyOJDkBmfBksB9tBHjBplBNrBkmBHsBAAA pc.gif
# use --start and --end to get specific PCs
