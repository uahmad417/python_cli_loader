
from itertools import cycle
from time import sleep


class Loader:
    """An animated cli loader for you python programs.

    Loader that gives dynamic loading animation and output for tasks running
    in your python programs

    Attribute:
        start_desc (str): The message to show while loading
        end_desc (str): The message to show when loading is completed
        stop (bool): Flag to check when to stop the loader

    Methods:
        start_loader: Starts the loading animation
        stop_loader: stops the loading animation
    """

    def __init__(self, start_desc: str, end_desc: str) -> None:
        """Initializes the loader object

        Args:
            start_desc (str): The message to show while loading
            end_desc (str): The message to show when loading is completed
        """

        self._start_desc = start_desc
        self._end_desc = end_desc

    def start_loader(self):
        """Starts the loading animation
        """

        animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for character in cycle(animations):
            print(f" {character} {self._start_desc}", end="\r")
            sleep(0.1)

    def stop_loader(self):
        """Stops the loading animation
        """
        pass
