import multiprocessing
import time
import threading
from multiprocessing.pool import ThreadPool
import os


def process(key, path, filename, output_directory, mappings, _type):
    file_output_directory = os.path.join(output_directory, _type, filename.split("_")[0])
    if not os.path.exists(file_output_directory):
        try:
            os.makedirs(file_output_directory)
        except:
            pass
    output_file_path = os.path.join(file_output_directory, filename)
    mappings[key](os.path.join(path, filename), output_file_path)


def attempt_to_process(edge_mapping, vertex_mapping, filename, path, output_directory):
    for key in edge_mapping:
        if filename.startswith(key):
            process(key, path, filename, output_directory, edge_mapping, "edge")
            return
    for key in vertex_mapping:
        if filename.startswith(key):
            process(key, path, filename, output_directory, vertex_mapping, "vertex")


class ProcessQueue:
    __cpu_count = multiprocessing.cpu_count()
    __pool = ThreadPool(__cpu_count)
    __failures = []
    __futures = []
    __events = []
    __lock = threading.Lock()

    def __init__(self):
        pass

    def get_failures(self):
        for f in self.__futures:
            f.wait()
        return self.__failures


    def submit(self, edge_mapping, vertex_mapping, filename, path, output_directory):
        self.__futures = [future for future in self.__futures if not future.ready()]
        while len(self.__futures) >= self.__cpu_count:
            # Need to block until a thread is finished
            time.sleep(0.1)
            self.__futures = [future for future in self.__futures if not future.ready()]

        self.__futures.append(
            self.__pool.apply_async(
                attempt_to_process,
                args=(edge_mapping, vertex_mapping, filename, path, output_directory),
                error_callback=self.__error_callback)
        )

    def __error_callback(self, e):
        self.__failures.append(e)
