import pandas
import time
import numpy


def convert_vertex(input_file_path, output_file_path):
    print("Processing " + input_file_path)
    start = time.time()
    df_iter = pandas.read_csv(input_file_path, delimiter="|", quotechar="\"", escapechar="\\")
    df_iter.rename(columns={"id": "~id"}, inplace=True)
    df_iter.to_csv(output_file_path, sep=",", encoding='utf-8')
    print("Finished processing " + input_file_path.split("/")[-1] + " in " + str(time.time() - start) + " seconds")


def convert_edge(input_file_path, output_file_path, _from, _to, _label):
    print("Processing " + input_file_path)
    start = time.time()
    df_iter = pandas.read_csv(input_file_path, delimiter="|", quotechar="\"", escapechar="\\")
    if _to == _from:
        df_iter.rename(columns={_from: "~from", _to + ".1": "~to"}, inplace=True)
    else:
        df_iter.rename(columns={_from: "~from", _to: "~to"}, inplace=True)
    df_iter.insert(0, "~id", numpy.nan)
    df_iter["~label"] = _label
    df_iter.to_csv(output_file_path, sep=",", encoding='utf-8', index=False)
    print("Finished processing " + input_file_path.split("/")[-1] + " in " + str(time.time() - start) + " seconds")
