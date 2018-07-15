def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    a=''.join(l)
    return a
