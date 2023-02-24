import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from MTV.models import Board, Question, Answer

# def data_select():
#     print(Board.objects.all())
#     print("Object Conut: {}".format(Board.objects.count()))

#     print(Board.objects.filter(id=1))
#     print(Board.objects.filter(id=2))
#     print(Board.objects.get(id=1))
#     print(Board.objects.get(id=2))

    # print(Board.objects.filter(title__contains="Board"))
    # print(Board.objects.filter(title__contains="Django"))

# def data_create():
#     Board_data = Board(title='Django Project',content='Django Project Model Data Create Test')

#     Board_data.save()

#     print(Board.objects.all())

# def data_delete():
#     Board_data = Board.objects.get(title="Django Project")
#     Board_data.delete()
#     print(Board.objects.all())

# def data_modify():
#     Board_data = Board.objects.get(title='Django Project')
#     Board_data.title = 'Django Model Test'
#     Board_data.save()
#     print(Board.objects.all())

# def data_objects():
#     Board_object = Board.objects.get(title='Board Title')
#     print("ID(pk): {}".format(Board_object.id))
#     print("Title: {}".format(Board_object.title))
#     print("Content: {}".format(Board_object.content))
#     print("Create_Date: {}".format(Board_object.create_date))
#     print("Modify_Date: {}".format(Board_object.modify_date))

# def R_selete():
#     Q = Question.objects.get(id=1)
#     print("ID(pk): {}".format(Q.id))
#     print("Title: {}".format(Q.title))
#     print("Content: {}".format(Q.content))

#     print("Answer Count: {}".format(Q.answer_set.count()))
#     print("Answer List: {}".format(Q.answer_set.all()))
#     print("Answer Get: {}".format(Q.answer_set.get(content__contains='Professor')))
#     print("Answer Filter: {}".format(Q.answer_set.filter(content__contains='Soccer')))

# def R_create():
#     Q = Question.objects.get(id=1)
#     Q.answer_set.create(content='Office Worker')
#     print("Answer List: {}".format(Q.answer_set.all()))

# def R_delete():
#     Q = Question.objects.get(id=1)
#     A = Answer.objects.get(content__contains="Office Worker")
#     A.delete()
#     print("Answer List: {}".format(Q.answer_set.all()))


# if __name__ == '__main__':
    # data_select()
    # data_create()
    # data_delete()
    # data_modify()
    # data_objects()
    # R_selete()
    # R_create()
    # R_delete()