___author__ = 'Ahmed Hani Ibrahim'

import time
from sys import platform
import psutil
import os


class Usage(object):
    def __init__(self):
        self.__start_time = None
        self.__end_time = None
        self.__memory_usage = None

    def start(self):
        self.__start_time = time.time()

    def end(self):
        self.__end_time = time.time()

    def get_execution_time(self):
        return self.__end_time - self.__start_time

    def get_memory_usage(self):
        if platform is "linux" or platform is "linux2":
            process = psutil.Process(os.getpid())

            return (process.memory_info().rss / 1024) / 1024
        else:
            process = psutil.Process(os.getpid())

            return (process.memory_info().rss / 1024) / 1024
