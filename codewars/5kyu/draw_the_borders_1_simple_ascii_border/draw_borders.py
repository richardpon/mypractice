from typing import Tuple, Set

class Solution:

    def draw_borders(self, shape):
        #convert each shape[] into squares and borders
        # output = borders is set of tuples representing border

        borders = self.get_borders(shape)

        #donut detection   
        borders = self.remove_donut(borders)

        #draw
        return self.draw(borders)

        

    def get_borders(self, shape) -> Set[Tuple[int,int]]:
        # maintain set of borders
        borders = set()

        for block in shape:
            
            # add all borders if not already in the shape
            # for each of possible 8 border squares surrounding block:
            possible_borders = self.get_surrounding_coordinates(block)
            for cur_coordinate in possible_borders:
                if cur_coordinate not in shape:
                    borders.add(cur_coordinate)

        return borders
            

    def get_surrounding_coordinates(self,coordinate_tuple) -> Set[Tuple[int,int]]:
        x = coordinate_tuple[0]
        y = coordinate_tuple[1]
        
        return {(x-1,y+1), (x,y+1), (x+1,y+1), \
            (x-1,y),(x+1,y), \
            (x-1,y-1), (x,y-1), (x+1,y-1)    }

    def up_down_neighbors(self,coordinate_tuple) -> Set[Tuple[int,int]]:
        x = coordinate_tuple[0]
        y = coordinate_tuple[1]
        
        return {(x-1,y),(x+1,y), (x,y+1), (x,y-1)}


    def remove_donut(self,borders) -> Set[Tuple[int,int]]:
        # identify a known border on the outside
        # single pass, what is block with lowest x? This is starting point

        #from starting point, mark adjacent blocks as outside

        #identify a block with the lowest x
        min_x = 100
        starting_block = None 
        for block in borders:
            if block[0] < min_x:
                min_x = block[0]
                starting_block = block

        #from min block, mark adjacent blocks as outside
        
        outside = {starting_block} # known outside borders
        borders_to_check = borders
        borders_to_check.remove(starting_block) #already checked starting block
        
        #iteratively mark adjacent blocks of known outside blocks as outside
        squares_to_check = self.up_down_neighbors(starting_block)
        while(squares_to_check):
            cur_square = squares_to_check.pop()
            if cur_square in borders:
                #found another outside border
                outside.add(cur_square)
                borders_to_check.remove(cur_square)
                squares_to_check |= self.up_down_neighbors(cur_square)
        
        return outside


        

    def draw(self,shape) -> str:
        # find the min/max x/y
        #start printing characters with a raster scan from top left

        output = ""

        (min_x, max_x, min_y, max_y) = self.get_min_max(shape)
        
        # print characters
        for y in range(max_y, min_y - 1, -1):
            line = ""
            for x in range(min_x, max_x + 1):
                line += self.get_char(x, y, shape)
            
            output += line + "\n"
    
        return output[0:-1]

    def get_char(self, x, y, shape) -> str: 
        # borders with only top/down neighbors are vertical
        # borders with only L/R neighbors are horizontal
        # otherwise, +

        if (x,y) not in shape:
            return " "
        if (x,y-1) in shape and (x,y+1) in shape and \
            (x-1,y) not in shape and (x+1,y) not in shape:
            return("|")
        elif (x-1,y) in shape and (x+1,y) in shape and \
            (x,y+1) not in shape and (x, y-1) not in shape:
            return("-")
        else:
            return("+")

    def get_min_max(self, shape) -> (int, int, int, int):
        min_x = 100
        max_x = -100
        min_y = 100
        max_y = -100
        for square in shape:
            x = square[0]
            y = square[1]
            
            min_x = min(min_x, x)
            max_x = max(max_x, x)

            min_y = min(min_y, y)
            max_y = max(max_y, y)

        return (min_x, max_x, min_y, max_y)


s = Solution()
print(s.draw_borders({(1,1)}))