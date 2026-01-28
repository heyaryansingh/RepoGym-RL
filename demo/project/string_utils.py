def kebab_to_camel(text):
    """
    Converts kebab-case to camelCase.
    Example: 'hello-world' -> 'helloWorld'
    """
    if not text:
        return ""
    parts = text.split("-")
    # BUG: Should capitalize all parts except the first.
    # Current implementation incorrectly capitalizes everything or fails on indexing.
    return "".join(p.capitalize() for p in parts) # BUG: Capitalizes the first word too
