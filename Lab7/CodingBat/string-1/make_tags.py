def make_tags(tag, word):
    open_tag = '<' + tag + '>'
    close_tag = '</' + tag + '>'
    return open_tag + word + close_tag