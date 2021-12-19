from constant import GHOST_NORMAL_STEP, GHOST_SLOW_STEP


class Ghost:
    def __init__(self, x, y):
        self.is_alive = True
        self.step = GHOST_NORMAL_STEP
        self.big = False
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

    def make_slow_step(self):
        self.change_step(GHOST_SLOW_STEP)

    def make_size_big(self):
        self.big = True