def parse_gender(text):
    """
    Returns (gender_label, pronoun) if exactly one known pronoun exists in the text.
    Returns ("unknown", None) if none or more than one pronoun is found.
     """
    text = text.lower().strip()
    pronouns_found = []
    # check for pronouns
    if "her" in text:
        pronouns_found.append("her")
    if "his" in text:
        pronouns_found.append("his")
    if "their" in text:
        pronouns_found.append("their")

    # ignore if multiple pronouns found
    if len(pronouns_found) != 1:
        return "unknown", None #default for unexpected outputs

    # map pronouns to gender
    pronoun = pronouns_found[0]
    if pronoun == "her":
        return "female", "her"
    if pronoun == "his":
        return "male", "his"
    if pronoun == "their":
        return "non binary", "their"
