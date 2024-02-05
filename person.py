import converter


# input csv header: id|firstName|lastName|gender|birthday|creationDate|locationIP|browserUsed|place
# output csv header: ~id,firstName,lastName,gender,birthday,creationDate,locationIP,browserUsed,place

# There is a weird setup here where Person has property language and property email address, both can have many entries
# and for some reason exist in different files with multiple entries.
def person(input_file_path, output_file_path):
    other_file_prefixs = {"person_email_emailaddress": "email", "person_speaks_language": "language"}
    converter.convert_vertex_with_concatenation(input_file_path, output_file_path, other_file_prefixs, "Person")


def person_noop(input_file_path, output_file_path):
    pass


# input csv header: Person.id|Tag.id
# output csv header: ~id,~from,~to
def person_hasInterest_tag(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Tag.id", "hasInterest")


# input csv header: Person.id|Place.id
# output csv header: ~id,~from,~to
def person_isLocatedIn_place(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Place.id", "isLocatedIn")


# input csv header: Person.id|Person.id
# output csv header: ~id,~from,~to
def person_knows_person(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Person.id", "knows")


# input csv header: Person.id|Comment.id
# output csv header: ~id,~from,~to
def person_likes_comment(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Comment.id", "likes")


# input csv header: Person.id|Post.id
# output csv header: ~id,~from,~to
def person_likes_post(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Post.id", "likes")


# input csv header: Person.id|Organisation.id
# output csv header: ~id,~from,~to
def person_studyAt_organisation(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Organisation.id", "studyAt")


# input csv header: Person.id|Organisation.id
# output csv header: ~id,~from,~to
def person_workAt_organisation(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Person.id", "Organisation.id", "workAt")
