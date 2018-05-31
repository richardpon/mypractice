from enum import Enum

class SolutionOld:

    def convert(self, s, numRows):
        self.array = {}
        self.numRows = numRows

        # build array data structure to hold
        for i in range(0, numRows):
            self.array[i] = {}

        self.go_down(s, 0, 0, 0)

        return self.convert_array_to_string(self.array)

    # Attempts to put a character into the current position (row, col) and continue going down
    def go_down(self, s, pos, row, col):

        if pos < len(s):

            # add char and continue going down
            if row < self.numRows:
                self.array[row][col] = s[pos]
                self.go_down(s, pos + 1, row + 1, col)

            # already past last row, start diagonal (adjust row to be last)
            else:
                self.go_diagonal(s, pos, row - 2, col + 1)

        # no more characters left in string, done
        else:
            return

    # Attempts to put a character into the current position (row, col) and continue going diagonal
    def go_diagonal(self, s, pos, row, col):
        
            if pos < len(s):

                # add char and still keep going
                if row >= 0:
                    self.array[row][col] = s[pos]
                    self.go_diagonal(s, pos + 1, row - 1, col + 1)

                # past top row, start going down and adjust row to first
                else:
                    self.go_down(s, pos, 1, col)

            # done
            else:
                return

    def convert_array_to_string(self, array):

        s = ""

        for i in range(0, len(array)):
            row = array[i]
            for k in sorted(list(row.keys())):
                s += row[k]
        return s

class DIR(Enum):
    UP = 1
    DOWN = -1

class Solution:

    def convert(self, s, numRows):
        self.rows = []
        self.numRows = numRows

        for i in range(0, numRows):
            self.rows.append("")

        row = 0
        dir = DIR.DOWN
        for c in s:
            self.rows[row] += c


            if dir == DIR.DOWN:
                if row < self.numRows - 1:
                    row += 1
                else:
                    dir = DIR.UP
                    row -= 1
            else:
                if row > 0:
                    row -= 1
                else:
                    row += 1
                    dir = DIR.DOWN

        s = ""
        for row in self.rows:
            s += row

        return s
