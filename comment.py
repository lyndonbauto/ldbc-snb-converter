import converter


# input csv header: id|creationDate|locationIP|browserUsed|content|length
# output csv header: ~id,creationDate,locationIP,browserUsed,content,length
def comment(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path, "Comment")

# input csv header: Comment.id|Person.id
# output csv header: ~id,~from,~to
def comment_hasCreator_person(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Comment.id", "Person.id", "hasCreator")


# input csv header: Comment.id|Tag.id
# output csv header: ~id,~from,~to
def comment_hasTag_tag(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Comment.id", "Tag.id", "hasTag")


# input csv header: Comment.id|Place.id
# output csv header: ~id,~from,~to
def comment_isLocatedIn_place(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Comment.id", "Place.id", "isLocatedIn")


# input csv header: Comment.id|Post.id
# output csv header: ~id,~from,~to
def comment_replyOf_comment(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Comment.id", "Comment.id", "replyOf")


# input csv header: Comment.id|Post.id
# output csv header: ~id,~from,~to
def comment_replyOf_post(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Comment.id", "Post.id", "replyOf")