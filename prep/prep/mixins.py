class PlaceHolderMixin:

    def get_placeholder(self):
        for field_name, field in self.fields.items():
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_placeholder()


class ReadOnlyMixin:
    readonly_fields = []

    def make_readonly_fields(self):
        for field in self.readonly_fields:
            if field in self.fields:
                self.fields[field].widget.attrs['readonly'] = True

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_readonly_fields()
