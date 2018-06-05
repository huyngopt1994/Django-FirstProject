command to handle with models in likes books:
###Create 3 different user accounts
####using objects.create to create user

`User.objects.create(first_name='huy',last_name='ngo',email='huyngo@gmail.com')`
`User.objects.create(first_name='minh',last_name='thu',email='minhthu@gmail.com')`
`User.objects.create(first_name='van',last_name='duc',email='vanducgmail.com')`

###Have the first user create/upload 2 books
####using objects.create and pass the object of first user to link one to many relationship

`Book.objects.create(name='book1',desc='this is book1',uploader=User.objects.get(id=1))`
`Book.objects.create(name='book2',desc='this is book2',uploader=User.objects.get(id=1))`
###Have the second user create/upload 2 other books.
`Book.objects.create(name='book3',desc='this is book3',uploader=User.objects.get(id=2))`
`Book.objects.create(name='book4',desc='this is book4',uploader=User.objects.get(id=2))`

###Have the third user create/upload 2 other books.
`Book.objects.create(name='book3',desc='this is book3',uploader=User.objects.get(id=3))`
`Book.objects.create(name='book4',desc='this is book4',uploader=User.objects.get(id=3))`

###Have the first user like the last book and the first book
1./ get object first user :
`a = User.objects.get(id=1)`
2./ Add 2 book objects ( the first and the last into user 1 )
`a.liked_books.add(Book.objects.first(),Book.objects.last())`
3./ Verify again :
`a.liked_books.all()`

###Have the second user like the first book and the third book
1./ get object first user :
`a = User.objects.get(id=2)`
2./ Add 2 book objects ( the first and the last into user 1 )
`a.liked_books.add(Book.objects.first(),Book.objects.get(id=3))`
3./ Verify again :
`a.liked_books.all()`
###Have the third user like all books
1./ get the third object user:
`a =User.objects.get(id=3)`
2./ Add all Book objects into third user (using *list)
`a.liked_books.add(*list(Book.objects.all()))`

###Display all users who like the first book
1./  `Book.objects.get(id=1).liked_users.all()`
###Display the user who uploaded the first book
1./ `Book.objects.get(id=1).uploader` (return User object as well)
###Display all users who like the second book
2./ `Book.objects.get(id=2).liked_users.all()`
###Display the user who uploaded the second book
    `Book.objects.get(id=2).uploader`