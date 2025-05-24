import anki
import genanki
from py_fumen_py import *
import subprocess
from pathlib import Path
import os
my_model = genanki.Model(
  234567, 'pc-run-fumen-flashcard',
  fields=[
    {
        'name': 'front',
    },
    {
        'name': 'media'
    },

  ],
  templates=[
    {
        'name': 'card1',
        'qfmt': '{{front}}',
        'afmt': '{{FrontSide}}'
        '<hr id="answer">'
        '{{media}}',
    }
  ],
)
my_deck = genanki.Deck(
    1520042884,
'genanki-fumen-deck')
my_package = genanki.Package(my_deck)
# TODO ask user for fumen or fumen file
# TODO ask user for 2 line pc indexes
fumen = 'v115@vh/XKYoSFLDmClcJSAVDEHBEooRBToAVBsnFgCqOOM?CKNMgC63/wCPd9VCsHcgCp/lPCJHmFDMdNPCTHWWC6X+tCv?SNPCUeLuCqyCMCat/VCvubMCzOUPCve9VCv3ntC0yCMCzfz?PCvOstCauytC6eNPCs3/VCp+bgCUuTWCvfzFDs+jPCPONPC?z+KWCan/wCzn9VC0HkPCJHEWCUtPFDPe/VCadFgCUnntCpO?UFDs+ytCpfjxCKtrgCpyTxCpXUPCPdNPCvXWWCJ3jFDqOEW?CJtPFDU3TxCsvaFDpyTxCvPNFDvPltC6CegCaNWWCp/7LC0?fLuCvybgCK+lFDpyTxCv3HgC6/rtCpuLuCU+TPCvnltCKHE?xCz+aPC6SltCK+VWCvXOMCvintC6CmFDJnntCzS9wCKnjxC?aNUPCP+lPCpirgCT+9tCqirgCziHgC0n9VCat/wCJn3LCPN?UFDUd9wCqirgCP+lPC6yLMCv+TWC6fHgCUeLuCMHExCqHMM?CauTxCqyKxCat3LCMnzPCU+LgCzuLuCvP9VCzvKxCsnNPCv?yTxCa+TFDzPFgCUuaPC6yTxCK9KWCa+dgCMuTxCqHkPCMej?xCv3/wCMXltC6+jPCMuaPCvyLMC6+TxCv33LCMHstCqubMC?UdFgCsfLuCqSNFDv+KWC6+jPCpS9wCPtzPCU+TFDK9ytC0/?LgCaeLuCPe/VCUNUFDJn/wCpXExCTn/wCJ9aPCsnNFDqybg?CUuKxC6intCz+aPCMeLuCvS9wC6PFgCMNmPCauaPCzijxC0?vjFDpyaPCvn9wCzibMC0iHgCzujWCJ9aPCaH+tCqSNPCUuT?WCan/VCJH+tCadNFD0iHgCsHLxCKdFgC6/7LCz+TxCs3HgC?pujWCJtHgCvuntCsnFgCMe/wCat/wCsHMMCPtzPCJHExCqy?jFDp+ytCqHDMC0yjFDpyaPCU+9tCs3HgCp+jFDqySgCsXmP?CJNUFDz/NMCPNegCsnNPCzXmPCMuCMCMnzPCzeNFDvvTxCM?njxCpintCPuTWCqXegC6OUPCJtPFDU+LgCTNMgCUezPCvyT?xCKeLuCs/NMCvXOMCKHstC6/dgCpyjFDzHLxCqSNFDUentC?vyjPCpCmFDv/TFDU3LMCJnntC6C+tC03/VCPOFgCqXWWCT+?lPCvyjFDpybgC0fLuCPe/VC03ntCaX9VC0ibMCz/dgCPNOM?CqiLuCUXNPC6irgCzO8LCqiPFDT+dgCMnLuCp/VxCpiLuCv?/NMCPtjWCqXmPCP+rtCpOUFDPt/VCq+bgCp3zPCMuKxCzu3?LCviLuCKHOMCzizPC0HztCpSFgCqyTxC6vCMCzujWCJtjxC?MnntC6u/VCJnPFDTX9wCMNmFDqyCMCMuTxCan3LCqC+tCaH?MgCat/wCp+LMCsHbPCaentCvOUFDMHOMCKdNFDsuHgCTeLu?Cvu/VC0HDMCz/DWCauKxCz/DxCJnPFDT+DxCvHkPCa9KxCM?pBifBpoB2xBVwBzsBlrBRsBnqBSyB2uBMsBzqBMoBurBzlB?vpBRnBaqBVyB0iBXsB6oBJkBzpBtmBerBuqBzpBxuBUrBKk?BPlBxgBGmBXtBTnB9tBisBMpBVvBUrB3gBTsBlmBifBGiBp?oBJoB0sBvtBGjBqrBdrBhuBEnB3lBTpBmpBTtBKpBlfBxwB?vh/EqB9qBSxBXnBToBOrBJkBSyBzpBMoBWwBFsBFrB3sBzp?BRwBPrBKpBWxBEqBmgBTtBCtBPsBkpBxxBTpB1vB0rBXhBd?nBmkBxfBSyBMtBusBRvBipBvlBTfB9tBBxBXoBarBzrBGsB?UtBVxB0iB6oBtmB2uBTlBvkBZmBGqBpoB3rBTpByxBsnBFi?B2kBFmBvh/3lBEqBpoByxBTpBsnBXiB2rBhvBTkBKqBCrB1?uBXgBOkB0qBFmBpoBzsBynB0mBHsBxuBTtB2pBTjBGlBXsB?xfBNrB6sBkrBVyB6oBzpBXsBJkBWlB0iB1mBllBHrBOpBzp?B0lBxfBvmBSyBBwBMtBasBusBTpBvtB1xBxvBTkBGoB1wBE?nBKqBzqBxxB3rBvh/+oBsnBimBNpBxhBHqB6qBkpBGtBlqB?nrBTpBiqBGsBTkBMtBxqBisB1vBXhBTpBOlBpoBkrBTfB9s?BJoBHsB2uB0kBSyBFsBMoBzqB3nByqBxkBurBSyB1uBRsBO?kB0qBXgBTjBdmBXsBCsBGtBRxBTjBMnB1vBxkB3hBKpBzpB?ErB2uBzkB0sB9tBifBXjBvh/5lBNrB0mBHsB2uBpoBifBet?BzkBUnBliBBwBXmBWwBSyBTpB1wB3qBTkBNqBUmBasBWtBH?tBxxB+oBJkBKnBziBtpBUgBhvB9rBzqBSyBXsBMrBuqByuB?MtBRmBTpBmpBnsBPsBSyBVwBxhBllBOpBknBTjB0kBHqBSy?BGjBznBJkB1wBWvB1vBasBErBzpBvh/3pBpoB1vBXgBOkBy?xBxrBznBsrBHrB2uBzkBifBsqB1wBChBEnBHtBGtBxxBxxB?TpBVtBGjBTfBHnBKqBErBlqBnrBxxBJkB+oBCsBtpBziBzh?BZmB9lBEqB2uB0qBvkB6tBzsBJnBvrBCtBUqBGrB+tBVxBz?nBxiBkhBXrByuBtqBKpBzpB2uB0qBvkBpoBvh/UgBJoBvrB?NsBGmB6sBTpB1vB0rBXhBOlBpoBVnBTfBaoBksBVyBJkB6o?BzpBXsB1mBkiBHrBzkBuqBxxBKpBPqB+oBzqBurByqBssBx?pBFsBTtB2uBvkBalBtqBxnBUhBCoBnrBEsBxuB2pBTtB9sB?TjBWrB0kBirBXsBxvB1vBXhBTpBmkB0rBxfBCtBdnBvh/Co?BTtBxxB3rB+oBsnBXiBOmBNpBxfBUlBSvBTtB1uB0qBOkBV?mBTjBpnBHgBanBkrBvtBGjBqsBZnBTrBVvBThB6lBnkBOpB?poBNpBXqB0fBzsBVwB0gBJnB6rBzsB2uBvkBalBVwBUsBul?B9nBnhBpoBJoBKpBTtBWxB3nBGjBUqB6lBkfBzhBZmBVxBT?tBvh/CoB0hBXrBtlBxiB6pBZlBOpB9tBXjB0sBTpBtmBmkB?yvBslBxpBHsBTtB3nBGjBWxBNpBzhBUlBZmB6qBkpBTtBxw?B3nBGjBNpB3mBihBUlBxkBSvB2uBVwBTtBUsBSvB9sB3rBT?tB2uBRvBRxBvtBTnBGjB1uBMrBihBUlBOkB6qBJkBXrBVxB?TtBTjBRlBvh/0hB6nBWqBHqB1vBXhBTpBmkBSyBxfBkrB1x?BTtBHsBJkBSyBMoBunB1wBzpBanBHmBRlBGqBMqBVwBTpB2?kB3hBRgBUsB9nB6tBOtBXqBMpBpoBifBzsBmrBznB0qBlrB?RwBXsBSyBMoB1vBdmBKpBurBzpBnsBxuBMpBifBpoBXqBzs?BmrBsrBznBlqBFrBvh/3pBOkBxvBWrByxBpoBHlBimBEsBz?sBVyB6oBJkBzpBWlBXsB0iBlmBXmBkqBJkBSyBGjBznBywB?VrBzhBEqBupBnqB1vBTpB0rBmkBxfBSyBXmBFsBHtBxxBSy?BMoBunBzrBZkBtpB0lByrBFqBHrBpoBzsBziBesBumB3pBN?kB0lBRlByvBipBRvBTfBVyBvh/0lBXsBmlB1sB6tBurBXrB?MqBTpBRxBMnBeoB3hBTfBigBpoBVyB6oBXsB0iBJkBlmBzp?BWlBXmBkqB2uBzkBpoBifB3rBsqBRnBChBdtBTsBVyBWvBJ?kBXsB6oB0iBtmB+lBzfBZmBvtB0sBGjBqrBzqBzgBipBEnB?lpBmpBJkBXsBSyBMoB3mBliB1vBOlBvh/5kBHrBTpBTfBSy?BMoBZlBunBXrBtlBdnBkrB2uBSwBTtBJnBpnBToBMrBWvB3?qBipB1vB0rBTpBmkBxfBXhBSyBFsBToBksBxxBStBOnBHjB?TrBNpBHqBCrBxqBkpB2uBzkB0sB9tBifB2wB5lBvrBFtBEs?B2uBpoBifBzkB3sBXnBtqBatBTrBRwBUtB9oBvh/zpBOpB3?iBVxBmfBqqBUmBnrBxuBypBGtBRrBTkBUrBdsBxlBGoBzsB?KpB3rBUqB+sBNtBzlBxlB6tBHsBkpB1vB0rBTpBXhBmkBVn?BpoBksBatBxuB2uBvkBTtBalBlnBGjB5lBirBvrBEsBTtB1?uBikB0qBlrBTjBXhBGnBxpBTsBxxB+oBsnB3rBKpBXiBvh/?FqB0fBOmB6qBTtB5nBJnBTjBOpBspBFrB6rBnqBxuB1uBOk?BTtBCoB9rBkqBXhBJnBHlBCtBTtB2uB0kB3rBTjBpnBtqBa?sBmpBErB1uBOkB0qBXgBpoByxBdmBzmBsnBCsBpoB2uBvkB?zsBziBvqBNrBJnBGlB6rB1vB0rBXhBTpBVyBmpBEsBxkB0n?B6tBvh/zsBXnB6tBxiB2wB1uBOkBElBCrBxvBXsBTpBSyBT?fBMoB3mBliB2vBlqBxvBxuBKkBUrBPlBTtB+sBllB1rBToB?HsBxxBSwB2uB0pB0qBOsBTmBxkBSyBHtBJkBVyB6oBkiBzp?BXsBWlBlmBOrB6qB3rBTpBhxBUiBUjBFmB2kBStBTqBRvBv?tB1xBGjBxuBvh/LrBNsBKpB3qBGrBzpBUrBhuB3gB1pBifB?UsB1mB+tB0nBHtBRvBipBTtBTsBGrBJkBSyBXsBMoBWvBli?BxqBPrBzpBkrBVyB6oBXsB0iBtmBarBZkBupB3lBEqBTtB2?uBSwBRqBTsB1uB0qBXgBOkBzsBFmBynBpoBXnBkrB2uBifB?zkBpoB1xBaoB3rB5lBvh/NrBEsBOpBzpBmfBSyB1sBBwBUr?BToBXnBCrBTtB3nBGjBsmBxwBFhB3qBtpBZkBEqBTpBSyBM?oB2vBunBvlBTfBlrBasBErBxxBznB6oBJkB2vBlrBvlBUhB?5kBFsB+tBTpB3sByvBUlBXjBzgBpmBOsBipBVyB0iBzpBZk?BXsBNrB6oBWlBkhB6qBTtBxwBvhP3nBGjBtqBlmBRhBzpBy?kBOpBUrBhuBKkBPlBlgBUsB3hBWcB'
pages = decode(fumen)

def two_line(queue: str) -> bool:
    i, j, l, o = 0, 0, 0, 0
    for char in queue:
        if char == 'I':
            i +=1
        elif char == 'J':
            j +=1
        elif char == 'L':
            l +=1
        elif char == 'O':
            o +=1

    total = i + j + l + o

    # Check if count is 6 or 5 as per problem statement
    if total not in (5,6):
        return False

    # For the case when count is 6:
    if total ==6:
        ij_mod2 = (i +j) %2
        il_mod2 = (i +l) %2

        possible_removals = []

        # Try removing an I or J based on which mod we're in for IJ
        if ij_mod2 ==0 and i>0:
            new_i, new_j = i-1, j
        elif ij_mod2 ==1 and j>0:
            new_i, new_j =i, j-1

        # Now check after removal whether IL mod is satisfied
        if (new_i + l) %2 == il_mod2:
            return True

    # For the case when count is5
    elif total ==5:
        ij_sum = i+j
        il_sum = i+l
        if ij_sum%2 ==0 and il_sum%2==0:
            return True

    return False

def create_note(i, page) -> None:
    queue = ','.join(page.comment.translate(translate_table)[:11]) # the queue
    save_text = pages[i+10].comment.translate(translate_table)[:1]
    queue_id = str(int(i + 10+two_line_count / 10+two_line_count)) # account for two_line_count
    queue = '<a href="https://himitsuconfidential.github.io/downstack-practice/usermode.html/=' + queue + '" > PC# ' + queue_id + '</a>'
    gif_name= queue + '.gif'
    my_note = genanki.Note(
        model=my_model,
        fields=[queue + " " + save_text, '<img src ="' + gif_name + '">'])
    my_deck.add_note(my_note)

def create_gif(start_index, end_index):
        gif_name = queue + ".gif"
        command = 'node ../fumen-canvas/fumen-canvas.js gif ' + fumen + ' ' + gif_name + ' --start ' + str(start_index) + ' --end ' + str(end_index)
        print('created  '+gif_name)
        os.system(command)
        my_package.media_files.append(gif_name)

remove_chars = {'#', 'Q', '[', ']', '=', '(', ')'}
translate_table = str.maketrans('', '', ''.join(remove_chars))
two_line_count = 0
for i, page in enumerate(pages):
    if i % 10 + two_line_count == 0 and i + 10 < len(pages):
        queue = ','.join(page.comment.translate(translate_table)[:11]) # the queue
        if two_line(queue[:11]):
            two_line_count += 5
            create_gif(i, i+two_line_count)
            #ask user if the file is a 2 line PC
            #if yes then add 5 to two_line_count and create the note
            create_note(i, page)

        else:
            create_gif(i, i+10+two_line_count)
            create_note(i, page)

genanki.Package(my_deck).write_to_file('output.apkg')
# Define the directory where your GIFs are stored

# Collect all .gif files in media_dir

print(f"Added {len(my_package.media_files)} media files.")
