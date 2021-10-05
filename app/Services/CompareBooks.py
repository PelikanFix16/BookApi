def CompareBooks(book1,book2):
    not_equal = False
    if book1.title != book2.title:
        not_equal = True
    if book1.authors != book2.authors:
        not_equal = True
    if book1.published_date != book2.published_date:
        not_equal = True
    if book1.categories != book2.categories:
        not_equal = True
    if book1.average_rating != book2.average_rating:
        not_equal = True
    if book1.ratings_count != book2.ratings_count:
        not_equal = True
    if book1.thumbnail != book2.thumbnail:
        not_equal = True
    
    return not_equal



def CompareArraysBooks(arrBook1,arrBook2):
    new_arr = []
    for i in arrBook1:
        for j in arrBook2:
            if not CompareBooks(i,j):
                print(i)
                new_arr.append(i)
    return new_arr
