import converter


# input csv header: id|title|creationDate
# output csv header: ~id,title,creationDate

def tagClass(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path)


# input csv header: TagClass.id|TagClass.id
# output csv header: ~id,~from,~to
def tagClass_isSubclassOf_tagclass(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "TagClass.id", "TagClass.id", "isSubclassOf")
