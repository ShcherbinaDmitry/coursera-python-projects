"""
Clone of 2048 game. Modules random and poc_2048_gui work from CodeSkulptor (https://py2.codeskulptor.org/)
"""
import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    prev = 0    #the last compared nonzero value
    merge_list = []   #the merge list
    for tile in line:
        if tile == prev and prev !=0: #merges
            prev = 0
            merge_list.pop()
            merge_list.append(tile*2)
        elif tile != 0:
            prev = tile
            merge_list.append(tile)
    return merge_list + [0 for dummy_x in range(len(line)-len(merge_list))]
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        
        #setting up indices for directions
        upind = [ (0, dummy_up) for dummy_up in range(self._grid_width)]
        downind = [ (self._grid_height - 1, dummy_down) for dummy_down in range(self._grid_width)]
        rightind = [ (dummy_right, self._grid_width - 1) for dummy_right in range(self._grid_height)]
        leftind = [ (dummy_left, 0) for dummy_left in range(self._grid_height)]
        self._dummy_dictionary = {UP:upind, DOWN:downind, RIGHT: rightind, LEFT: leftind}
        
        #starting initial board
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [ [0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = '['
        for row in range(self._grid_height):
            string += '['
            for col in range(self._grid_width):
                string += str(self._grid[row][col])
                if col != self._grid_width - 1:
                    string += ', '
            string += ']'
            if row != self._grid_height - 1:
                string += '\n'
        string += ']'
        return string
        
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        changed = False
        indice_list = self._dummy_dictionary[direction]
        if direction == UP or direction == DOWN:
            size = self._grid_height
        elif direction == LEFT or direction == RIGHT:
            size = self._grid_width
        for indice in indice_list:
            temp_grid = []
            
            for dummy_num in range(size):
                row = OFFSETS[direction][0]*dummy_num + indice[0]
                col = OFFSETS[direction][1]*dummy_num + indice[1]
                temp_grid.append(self._grid[row][col])
            temp_grid = merge(temp_grid)
            for dummy_num in range(size):
                row = OFFSETS[direction][0]*dummy_num + indice[0]
                col = OFFSETS[direction][1]*dummy_num + indice[1]
                if self._grid[row][col] != temp_grid[dummy_num]:
                    changed = True                
                self._grid[row][col] = temp_grid[dummy_num]
        if changed == True:
            self.new_tile()
        if self.victory_conditions() == 2:
            print "You have won!"
            self.reset()
        #elif self.victory_conditions() == 0:
            #print "You have lost!"
            #self.reset()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        while True:
            new_tile_height = random.randrange(0, self._grid_height)
            new_tile_width = random.randrange(0, self._grid_width)
            if self._grid[new_tile_height][new_tile_width] == 0:
                self._grid[new_tile_height][new_tile_width] = (2 if random.random() < 0.9 else 4)
                break      
            elif self.victory_conditions() == 0:
                print 'You lost'
                break
                
    def victory_conditions(self):
        '''
        Check if there is a tile with a value equal to 2048 
        or if there is any empty tile to make a move
        '''
        loss_result = 1
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                loss_result = loss_result * self._grid[row][col]
                if self._grid[row][col] == 2048:
                    return 2
        if loss_result == 0:
            return 1
        else:
            return 0
                
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

poc_2048_gui.run_gui(game = TwentyFortyEight(4, 4))
