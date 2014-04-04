#-------------------------------------------------------------------------------
# Name:        Para
# Purpose:
#
# Author:      anastass
#
# Created:     03-04-2014
# Copyright:   (c) anastass 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re


class Para():
    """Format text"""
    _col = None

    def __init__(self, col = 72):
        self.set_columns(col)

    def set_columns(self, col):
        """Set number of columns"""
        if type(col) == int and col > 0:
            self._col = col
        else:
            raise ValueError('The number of columns should be a positive integer. Given: ' + str(col))

    def get_columns(self):
        """Get number of columns"""
        return self._col

    def format_text(self, txt):
        """Format random text"""
        #result = ' '.join([str(x) for x in rgx.findall(txt)])   # find works and concatenate them using space
        #rgx = re.compile("\n([ \t]*\n)+")
        # TODO: Handle several CRLF and TABS between paragraphs
        return self.format_para(txt)

    def format_para(self, txt):
        """Format single paragraph"""
        columns = self._col
        cols_left = self._col

        rgx = re.compile("(\S+)")
        words = rgx.findall(txt)

        r = ''
        while len(words) > 0:
            word = words.pop(0)
            word_length = len(word)
            if cols_left > word_length:
                if cols_left < columns:
                    r += ' '
                r += word
                cols_left -= word_length
            elif word_length <= columns:
                r += '\n' + word
                cols_left = columns - word_length
            else:   # split
                n = columns - 1
                part = word[0:n]
                r += '\n' + part + '-\n'
                cols_left = columns
                words.insert(0, word[n:])
        return r


if __name__ == '__main__':
    text = """My money's in that office, right? If she start giving me some bullshit about it ain't there, and we got to go someplace else and get it, I'm gonna shoot you in the head then and there. Then I'm gonna shoot that bitch in the kneecaps, find out where my goddamn money is. She gonna tell me too. Hey, look at me when I'm talking to you, motherfucker. You listen: we go in there, and that nigga Winston or anybody else is in there, you the first motherfucker to get shot. You understand?


Normally, both your asses would be dead as fucking fried chicken, but you happen to pull this shit while I'm in a transitional period so I don't wanna kill you, I wanna help you. But I can't give you this case, it don't belong to me. Besides, I've already been through too much shit this morning over this case to hand it over to your dumb ass."""
    para = Para(40)
    print para.format_text(text)
