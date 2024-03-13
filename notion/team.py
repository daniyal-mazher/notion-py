from .records import Record


class Team(Record):
    _type = "team"
    _table = "team"
    _str_fields = "name", "domain"
    _child_list_key = "pages"

    name = field_map("name")
