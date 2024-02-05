import converter


# input csv header: id|creationDate|locationIP|browserUsed|content|length
# output csv header: ~id,creationDate,locationIP,browserUsed,content,length

def tag(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path, "Tag")


# input csv header: Tag.id|TagClass.id
# output csv header: ~id,~from,~to
def tag_hasType_tagclass(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Tag.id", "TagClass.id", "hasType")
