import converter


# input csv header: id|title|creationDate
# output csv header: ~id,title,creationDate
def post(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path, "Post")


# input csv header: Post.id|Person.id
# output csv header: ~id,~from,~to
def post_hasCreator_person(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Post.id", "Person.id", "hasCreator")


# input csv header: Post.id|Tag.id
# output csv header: ~id,~from,~to
def post_hasTag_tag(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Post.id", "Tag.id", "hasTag")


# input csv header: Post.id|Place.id
# output csv header: ~id,~from,~to
def post_isLocatedIn_place(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Post.id", "Place.id", "isLocatedIn")
