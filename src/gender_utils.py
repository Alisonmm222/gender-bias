def parse_gender(text):
    """
    Returns (gender, pronoun) if exactly one known pronoun exists in the text.
    Returns (unknown) if none or more than one pronoun is found.
     """
    text = text.lower().strip()
    pronouns_found = []
    # check for pronouns
    if "her" in text:
        pronouns_found.append("her")
    if "his" in text:
        pronouns_found.append("his")

    # ignore if multiple pronouns found
    if len(pronouns_found) != 1:
        return "unknown", None #default for unexpected outputs

    # map pronouns to gender
    pronoun = pronouns_found[0]
    if pronoun == "her":
        return "female", "her"
    if pronoun == "his":
        return "male", "his"
