import sys
import os
import mappings
import time
from process_queue import ProcessQueue


def process_files(input_directory, output_directory):
    static_edge_mapping = mappings.populate_static_edge_mapping()
    static_vertex_mapping = mappings.populate_static_vertex_mapping()
    dynamic_edge_mapping = mappings.populate_dynamic_edge_mapping()
    dynamic_vertex_mapping = mappings.populate_dynamic_vertex_mapping()

    print("walking input directory: " + input_directory)
    process_queue = ProcessQueue()
    for path, dirs, files in os.walk(os.path.abspath(input_directory)):
        if path.endswith("static"):
            for filename in files:
                process_queue.submit(static_edge_mapping, static_vertex_mapping, filename, path, output_directory)
        elif path.endswith("dynamic"):
            for filename in files:
                process_queue.submit(dynamic_edge_mapping, dynamic_vertex_mapping, filename, path, output_directory)
    print("waiting for processing to complete")
    failures = process_queue.get_failures()
    if len(failures) > 0:
        print("Failed to process the following files:")
        for failure in failures:
            print(failure)
        sys.exit(1)


def main(argv):
    start = time.time()
    input_directory = argv[1]
    output_directory = argv[2]

    if not os.path.exists(input_directory):
        print("Input directory does not exist: " + input_directory)
        return 1

    if not os.path.exists(output_directory + "/vertex"):
        os.makedirs(output_directory + "/vertex")

    if not os.path.exists(output_directory + "/edge"):
        os.makedirs(output_directory + "/edge")

    process_files(input_directory, output_directory)
    print("Total processing time " + str(time.time() - start) + " seconds")


if __name__ == "__main__":
    main(sys.argv)
