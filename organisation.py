import converter


# input csv header: id|name|type
# output csv header: ~id,name,type
def organisation(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path, "Organisation")


# input csv header: Organisation.id|Place.id
# output csv header: ~id,~from,~to
def organisation_isLocatedIn_place(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Organisation.id", "Place.id", "isLocatedIn")
