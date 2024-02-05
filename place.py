import converter


# input csv header: id|name|url|type
# output csv header: ~id,name,url,type

def place(input_file_path, output_file_path):
    converter.convert_vertex(input_file_path, output_file_path, "Place")


# input csv header: Place.id|Place.id
# output csv header: ~id,~from,~to
def place_isPartOf_place(input_file_path, output_file_path):
    converter.convert_edge(input_file_path, output_file_path, "Place.id", "Place.id", "isPartOf")
