import unicodedata

from .uni2latex import uni2latex 
from logger import Logger

def unicode_to_latex(s):
    """
    Convert unicode characters in the string `s` into latex escape sequences,
    according to the rules and options given to the constructor.
    """

    # s = unicode(s) # make sure s is unicode
    s = unicodedata.normalize('NFC', s)

    latex = []
    pos = 0

    while pos < len(s):
        # skip, we only want to convert non-ascii chars
        ch = s[pos]
        o = ord(ch)
        if (o >= 65 and  o <= 90) or (o >= 97 and o <= 122) or (ch in "\n\r\t"):
            if o == ord("_"): print("heeeeeeeeeeeeeeeeeeeeeeeeeeeeel")
            latex += ch
        elif o in uni2latex:
            # print("heeeeeeeeeel")
            latex += "{" + uni2latex.get(o) + "}"
        else: 
            do_warn_unknown_char(ch)
            ## add anyway
            latex += ch
        pos += 1
            
    return "".join(latex)

def do_warn_unknown_char(ch):
    pass
    # logger.
    # logger.info("No known latex representation for character: U+%04X - ‘%s’", ch)
