def load_text(pathname):
    """Load tweets into a list object.

    Argument: pathname of a text file
    Returns: list object containing one line per row
    """
    text_file = open(pathname, "r")
    l = list()
    for line in text_file:
        l.append(line)
    return l

# Load positive tweets
postweets = load_text("data/postweets.txt")

# Load negative tweets
negtweets = load_text("data/negtweets.txt")
