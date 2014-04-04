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
    _col = None

    def __init__(self, col = 72):
        self.set_columns(col)

    def set_columns(self, col):
        if type(col) == int and col > 0:
            self._col = col
        else:
            raise ValueError('The number of columns should be a positive integer. Given: ' + str(col))

    def get_columns(self):
        return self._col

    def format_text(self, txt):
        return self.format_para(txt)

    def format_para(self, txt):
        rgx = re.compile("(\S+)")
        result = ' '.join([str(x) for x in rgx.findall(txt)])   # find works and concatenate them using space
        return result


if __name__ == '__main__':
    text = """y money's in that office, right? If she start giving me some bullshit about it ain't there, and we got to go someplace else and get it, I'm gonna shoot you in the head then and there. Then I'm gonna shoot that bitch in the kneecaps, find out where my goddamn money is. She gonna tell me too. Hey, look at me when I'm talking to you, motherfucker. You listen: we go in there, and that nigga Winston or anybody else is in there, you the first motherfucker to get shot. You understand?


Normally, both your asses would be dead as fucking fried chicken, but you happen to pull this shit while I'm in a transitional period so I don't wanna kill you, I wanna help you. But I can't give you this case, it don't belong to me. Besides, I've already been through too much shit this morning over this case to hand it over to your dumb ass."""
    para = Para(40)
    print para.format_text(text)
