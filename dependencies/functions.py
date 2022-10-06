from re import sub


def format_title(title):
    new_title = ''
    for ch in title:
        if ch in 'aáàâãäåbcçdeéèêëfghiíìîïjklmnoóòôõöpqrstuúùûüvwxyzAÁÀÂÃÄÅBCÇDEÉÈÊËFGHIÍÌÎÏJKLMNOÓÒÔÕÖPQRSTUÚÙÛÜVWXYZ0123456789-_()[]{} ':
            new_title += ch
    new_title = sub(' +', ' ', new_title)
    new_title = new_title.strip()
    return new_title
