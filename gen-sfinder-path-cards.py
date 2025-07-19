#!/usr/bin/env python3

import anki
import genanki
import random


# TODO take a directory with a path.csv and last_output and
# returns an anki deck named the name of the folder containing links for each
# row in the path.csv file.


def parse_path():
    queues = []
    f = open("path.csv", "r")
    for line in f.readlines():
        queues.append(line[:7])

def parse_last():

    f = open("last_output")
def main():
    # initialiaze the anki deck.
    name = "TODO"
    model_num = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        model_num, name + '_model',
        fields=[
            {
                'link': 'front',
            },
            {
                'link': 'back',
            },
        ],
        templates=[
            {
                'link': 'card1',
                'qfmt': '{{front}}',
                'afmt': '{{FrontSide}}'
                '<hr id="answer">'
                '{{media}}',
            }
        ],
    )
    my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31), name + '_deck'
    )
    # get the queues
    # get the board state
    # create the himitsu links from the queues and the board state
    # add each himitsu link to a deck


main()
