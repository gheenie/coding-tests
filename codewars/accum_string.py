def accum(s):
    buildup = ''
    
    for i, letter in enumerate(s):
        current_buildup = letter * (i + 1)
        buildup += current_buildup.capitalize() + '-'
    
    return buildup[:-1]
