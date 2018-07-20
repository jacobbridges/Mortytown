import markdown


def render_markdown(sender, instance, *args, **kwargs):
    """
    Renders markdown from a text field to a dedicated html field.
    This is meant to be used with the pre_save signal.
    """
    md = markdown.Markdown(safe_mode='escape')

    for fieldname, _ in instance.__dict__.items():
        if fieldname.endswith("_html"):
            fieldname_raw = fieldname[:fieldname.find('_html')]
            field_raw = getattr(instance, fieldname_raw, None)

            if field_raw:
                setattr(instance, fieldname, md.convert(field_raw))
