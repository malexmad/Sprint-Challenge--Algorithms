class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Selection Sort

        # while loop if robot can move right is true
        while self.can_move_right() == True:
            # pick the first item in the list
            self.swap_item()

            # while loop move right by 1 and checking if item is lesser value, to the end of the list
            while self.can_move_right() == True:
                self.move_right()

                # swap item if it's a lesser value
                if self.compare_item() == 1:
                   self.swap_item()

            # from the end of the list go left by until an index value = 'None'
            while self.compare_item() != None:
                self.move_left()

            # swap the the item with 'nooe
            self.swap_item()

            # repeat main while loop process starting from the next index
            self.move_right()

        # print(self._time)





if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, -18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)