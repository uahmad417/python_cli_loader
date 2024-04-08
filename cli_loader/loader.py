
from itertools import cycle
from threading import Thread
from time import sleep
from typing import Callable, List


class Loader:
    """An animated cli loader for you python programs.

    Loader that gives dynamic loading animation and output for tasks running
    in your python programs

    Attribute:
        start_desc (str): the message to show while loading
        end_desc (str): the message to show when loading is completed
        stop (bool): flag to check when to stop the loader
        target (Callable): task to execute with loader. Should be a callable function
        target (List): list of tasks to execute with loader. tasks should be a callable function

    Methods:
        _start_loader: Starts the loading animation
        start_loader: Starts the loading animation in a seperate thread
        stop_loader: stops the loading animation
    """

    def __init__(self, start_desc: str, end_desc: str, targets: List[Callable] = None) -> None:
        """Initializes the loader object

        Args:
            start_desc (str): the message to show while loading
            end_desc (str): the message to show when loading is completed
            stop (bool): flag to check when to stop loader
            target (List): list of tasks to execute with loader. tasks should be a callable function
        """

        self.start_desc = start_desc
        self.end_desc = end_desc
        self.__stop = False
        self.targets = targets

    def __animate(self):
        """Starts the loading animation. 
        Should be run as a seperate thread
        """

        loading_animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        complete_animation = "\u2705"  # heavy checkmark
        for character in cycle(loading_animations):
            print(f" {character} {self.start_desc}", end="\r")
            sleep(0.1)

            if self.__stop:
                print(f" {complete_animation} {self.end_desc}", end="\n")
                self.__stop = False
                break

    def start_loader_with_target(self):
        """Start the loader.
        Creates a thread and calls the `_start_loader` method
        """

        for target in self.targets:
            thread = Thread(target=self.__animate)
            thread.start()
            target()
            self.stop_loader()

    def start_loader_simple(self):
        """Start the loader without target context.
        This loader needs to be stopped manually by calling `stop_loader`
        """
        thread = Thread(target=self.__animate)
        thread.start()

    def stop_loader(self):
        """Stops the loading animation
        """

        self.__stop = True
