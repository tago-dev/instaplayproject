def format_title(title):
    new_title = ''
    for ch in title:
        if ch in 'áãâéêóõôúûÁÃÂÉÊÓÕÔÚÛabcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ0123456789-_()[]{} ':
            new_title += ch
    return new_title
