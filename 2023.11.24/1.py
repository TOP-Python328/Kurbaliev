class ClassBuilder:
    def __init__(self, name):
        self.name = name
        self.class_fields = []
        self.inst_attrs = []

    def add_cls_field(self, field_name, value):
        self.class_fields.append((field_name, value))
        return self

    def add_inst_attr(self, attr_name, value):
        self.inst_attrs.append((attr_name, value))
        return self

    def __str__(self) -> str:
        class_def = f"class {self.name}:\n"

        if self.class_fields:
            for field_name, value in self.class_fields:
                class_def += f"    {field_name} = {value}\n"

        if self.inst_attrs:
            class_def += "    def __init__(self):\n"
            for attr_name, value in self.inst_attrs:
                class_def += f"\tself.{attr_name} = {value}\n"
        else:
            class_def += "    pass"
        return class_def


cb = ClassBuilder("Person").add_inst_attr("name", "''").add_inst_attr("age", \
    0)
print(cb)

cb = ClassBuilder("Test").add_cls_field("__protected", []).add_inst_attr(\
    "foo", "'bar'")
print(cb)

cb = ClassBuilder("Foo")
print(cb)
