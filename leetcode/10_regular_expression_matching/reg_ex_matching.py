class BaseSymbol:
    pass


# regular char symbol
class CharacterSymbol(BaseSymbol):
    def __init__(self, char):
        self.char = char

    def __repr__(self):
        return "Char({0})".format(self.char)

    def __eq__(self, other):
        return isinstance(other, CharacterSymbol) and self.char == other.char


# match any single CharacterSymbol
class DotSymbol(BaseSymbol):
    def __repr__(self):
        return "Dot({0})".format(".")

    def __eq__(self, other):
        return isinstance(other, DotSymbol)


# match 0 or more of the preceding Symbols
class StarSymbol(BaseSymbol):
    def __init__(self, char):
        if char == "*":
            raise Exception("Can't have consecutive StarSymbols")
        self.char = char

    def __repr__(self):
        return "Star({0})".format(self.char)

    def __eq__(self, other):
        return isinstance(other, StarSymbol) and self.char == other.char



class Solution:

    def isMatch(self, s, p):
        symbols = self.get_symbols(p)

        symbols = self.de_dupe_stars(symbols)

        return self.is_match_recursive(s, symbols)

    def get_symbols(self, pat):
        return self.convert_pattern_to_symbols(pat[::-1], [], False)[::-1]

    def de_dupe_stars(self, symbols):

        if len(symbols) < 2:
            return symbols

        prev_symbol = symbols[0]
        de_duped = [symbols[0]]

        for s in symbols[1:]:
            # skip only consecutive star symbols
            if s == prev_symbol and isinstance(s, StarSymbol):
                pass
            else:
                de_duped.append(s)
                prev_symbol = s

        return de_duped


    def convert_pattern_to_symbols(self, pat, symbols = [], is_prev_star = False):

        if len(pat) == 0:
            if is_prev_star:
                raise Exception("StarSymbol can't be last symbol")
            else:
                return symbols

        p = pat[0]
        tail = pat[1:]

        if is_prev_star:
            return self.convert_pattern_to_symbols(tail, symbols + [StarSymbol(p)], False)

        # Non-Prev-Star
        if p == "*":
            return self.convert_pattern_to_symbols(tail, symbols, True)

        if p == ".":
            return self.convert_pattern_to_symbols(tail, symbols + [DotSymbol()], False)
        else:
            return self.convert_pattern_to_symbols(tail, symbols + [CharacterSymbol(p)], False)

    def is_match_recursive(self, chars, symbols):

        # print("is_match_recursive({0}, {1}".format(chars, symbols))

        if len(chars) == 0 and len(symbols) == 0:
            return True
        elif len(chars) == 0 and len(symbols) > 0 and isinstance(symbols[0], StarSymbol):
            return self.is_match_recursive(chars, symbols[1:])
        elif (len(chars) == 0 and len(symbols) > 0) or (len(chars) > 0 and len(symbols) == 0):
            return False

        head_symbol = symbols[0]
        tail_symbols = symbols[1:]

        head_char = chars[0]
        tail_chars = chars[1:]

        if isinstance(head_symbol, StarSymbol):
            
            # match 0 or more char
            matches_no_chars  = self.is_match_recursive(chars, tail_symbols)

            matches_first_char = self.does_symbol_match_char(head_symbol, head_char)

            #print("matches_first_char = {0}, {1}, {2}".format(matches_first_char, head_symbol, head_char))

            return matches_no_chars or (matches_first_char and self.is_match_recursive(tail_chars, symbols))

        elif isinstance(head_symbol, DotSymbol):
            return self.is_match_recursive(tail_chars, tail_symbols)
        elif isinstance(head_symbol, CharacterSymbol):
            if head_symbol.char == head_char:
                return self.is_match_recursive(tail_chars, tail_symbols)
            else:
                return False
        else:
            raise Exception("WTF???")

    # does not match the None case for stars.
    def does_symbol_match_char(self, symbol, char):
        if isinstance(symbol, CharacterSymbol):
            return symbol.char == char
        elif isinstance(symbol, StarSymbol):
            return symbol.char == "." or symbol.char == char
        else:
            return True
