import pandas
import time
import numpy
import os


def convert_vertex(input_file_path, output_file_path, _label):
    print("Processing " + input_file_path)
    start = time.time()
    df_iter = pandas.read_csv(input_file_path, delimiter="|", quotechar="\"", escapechar="\\")
    df_iter.rename(columns={"id": "~id"}, inplace=True)
    df_iter["~label"] = _label
    df_iter.to_csv(output_file_path, sep=",", encoding='utf-8', index=False)
    print("Finished processing " + input_file_path.split("/")[-1] + " in " + str(time.time() - start) + " seconds")


def convert_vertex_with_concatenation(input_file_path, output_file_path, other_file_prefixs, _label):
    print("Processing " + input_file_path + " with concatenation of " + str(other_file_prefixs))
    start = time.time()
    print("!!!Start")
    df_iter_main = pandas.read_csv(input_file_path, delimiter="|", quotechar="\"", escapechar="\\")
    print("!!!rename")
    df_iter_main.rename(columns={"id": "~id"}, inplace=True)
    print("!!!???")
    # To merge these, we need to set out ~id as the index. This is because the merge function will use the index to
    # match rows. We can't use the default index because it will be different.
    # Additionally, we need to go through the other files and merge the ~id column internally, since it is something like
    # ~id, email
    # 1, foo@foo.com
    # 1, bar@foo.com
    # and we want it like
    # ~id, email
    # 1, [foo@foo,com,bar@foo,com]

    for filename, groupby_key in other_file_prefixs.items():
        print("!!!split1 " + filename)
        input_file_directory = input_file_path.rsplit("/", 1)[0]
        print("!!!split2 " + filename)
        file_concat_0 = input_file_path.split("/")[-1].split("_")[-1]
        file_concat_1 = input_file_path.split("/")[-1].split("_")[-2]
        other_file_path = os.path.join(input_file_directory, filename + "_" + file_concat_1 + "_" + file_concat_0)
        print("!!!Processing " + other_file_path)
        df_iter_other = pandas.read_csv(other_file_path, delimiter="|", quotechar="\"", escapechar="\\")
        print("!!!Renaming " + other_file_path)
        df_iter_other.rename(columns={df_iter_other.columns[0]: "~id"}, inplace=True)
        print("!!!Grouping " + other_file_path)
        df_iter_other[groupby_key] = df_iter_other.groupby(df_iter_other['~id'])[groupby_key].\
            transform(lambda x : [x.tolist()]*len(x))
        print(df_iter_other)
        print("!!!Merging " + other_file_path)
        df_iter_main = pandas.merge(df_iter_main, df_iter_other, on="~id")
    df_iter_main["~label"] = _label
    df_iter_main = df_iter_main.drop_duplicates(subset=['~id'])
    print("!!!Writing " + output_file_path)
    df_iter_main.to_csv(output_file_path, sep=",", encoding='utf-8', index=False)#, quoting=csv.QUOTE_NONE, escapechar="\\", quotechar="\"", doublequote=True)
    print("Finished processing " + input_file_path.split("/")[-1] + " in " + str(time.time() - start) + " seconds")



def convert_edge(input_file_path, output_file_path, _from, _to, _label):
    # Hack to not rework entire thing...
    # Remove filename from output_file_path
    output_file_name = output_file_path.split("/")[-1]
    output_file_path_dir = os.path.join(output_file_path.rsplit("/", 1)[0], _label)
    if not os.path.exists(output_file_path_dir):
        try:
            os.makedirs(output_file_path_dir)
        except:
            pass
    output_file_path = os.path.join(output_file_path_dir, output_file_name)

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
