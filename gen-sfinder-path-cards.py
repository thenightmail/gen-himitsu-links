#!/usr/bin/env python3

import anki
import genanki
import random


def parse_path():
    queues = []
    f = open("path.csv", "r")
    for line in f.readlines():
        queues.append(line[:7])

def parse_last():
    pass

def create_link(queue, board):
    pass

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
                '{{back}}',
            }
        ],
    )
    my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31), name + '_deck'
    )
    # cli argument and folder directory
    # if -r argument generate decks recursively.
    # else just generate deck for the folder specified
    # parse path, get the queues and saves
    # parse_last last_output, get the board state
    # create the himitsu links from the queues and the board state
    # add each himitsu link to a deck


main()
