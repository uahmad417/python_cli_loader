
from itertools import cycle
from threading import Thread
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
        _start_loader: Starts the loading animation
        start_loader: Starts the loading animation in a seperate thread
        stop_loader: stops the loading animation
    """

    def __init__(self, start_desc: str, end_desc: str) -> None:
        """Initializes the loader object

        Args:
            start_desc (str): The message to show while loading
            end_desc (str): The message to show when loading is completed
            stop (bool): flag to check when to stop loader
        """

        self.start_desc = start_desc
        self.end_desc = end_desc
        self.__stop = False

    def _start_loader(self):
        """Starts the loading animation. Should be run as a seperate thread
        """

        loading_animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        complete_animation = "\u2705" # heavy checkmark
        for character in cycle(loading_animations):
            print(f" {character} {self.start_desc}", end="\r")
            sleep(0.1)

            if self.__stop:
                print(f" {complete_animation} {self.end_desc}", end="\n")
                break

    def start_loader(self):
        thread = Thread(target=self._start_loader)
        thread.start()

    def stop_loader(self):
        """Stops the loading animation
        """
        self.__stop = True
