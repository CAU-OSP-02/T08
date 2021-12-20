from constant import PACMAN_FAST_STEP, PACMAN_NORMAL_STEP


class PacMan:
    def __init__(self, x, y):
        self.is_alive = True
        self.step = PACMAN_NORMAL_STEP
        self.block = False
        self.set_location(x, y)

    def get_location(self):
        return self.current_location

    def set_location(self, x, y):
        self.current_location = [x, y]

    def get_next_location(self, x_diff, y_diff):
        current_x, current_y = self.get_location()
        next_x = current_x + x_diff
        next_y = current_y + y_diff
        return next_x, next_y
    
    def change_step(self, new_step):
        self.step = new_step
    
    def make_fast_step(self):
        self.change_step(PACMAN_FAST_STEP)
        
    def make_blocked(self):
        self.block = True

