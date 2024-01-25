import converter


# input csv header: id|title|creationDate
# output csv header: ~id,title,creationDate
def forum(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path)


# input csv header: Forum.id|Post.id
# output csv header: ~id,~from,~to
def forum_containerOf_post(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Forum.id", "Post.id", "containerOf")


# input csv header: Forum.id|Person.id
# output csv header: ~id,~from,~to
def forum_hasMember_person(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Forum.id", "Person.id", "hasMember")


# input csv header: Forum.id|Person.id
# output csv header: ~id,~from,~to
def forum_hasModerator_person(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Forum.id", "Person.id", "hasModerator")


# input csv header: Forum.id|Tag.id
# output csv header: ~id,~from,~to
def forum_hasTag_tag(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Forum.id", "Tag.id", "hasTag")
