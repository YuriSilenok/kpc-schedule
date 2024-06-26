from peewee import SqliteDatabase, Model, ForeignKeyField, CharField, DateField, IntegerField

db = SqliteDatabase('db.db', pragmas={
    'foreign_keys': 1,
    'journal_mode': 'wal',
})

class BModel(Model):
    class Meta:
        database = db

class Group(BModel):
    name = CharField(max_length=10)

class SubGroup(BModel):
    name = CharField(max_length=10)
    group = ForeignKeyField(model=Group)

class Auditorium(BModel):
    name = CharField(max_length=5)

class Discipline(BModel):
    name = CharField(max_length=100)

class Teacher(BModel):
    fullname = CharField(max_length=255)

class Lesson(BModel):
    date = DateField()
    number = IntegerField()

class LessonGroup(BModel):
    lesson = ForeignKeyField(Lesson)
    group = ForeignKeyField(Group)

class LessonSubGroup(BModel):
    lesson = ForeignKeyField(Lesson)
    sub_group = ForeignKeyField(SubGroup)

class LessonAuditorium(BModel):
    lesson = ForeignKeyField(Lesson)
    auditorium = ForeignKeyField(Auditorium)

class LessonTeacher(BModel):
    lesson = ForeignKeyField(Lesson)
    teacher = ForeignKeyField(Teacher)

db.connect()
db.create_tables(
    [
        Group, 
        SubGroup, 
        Auditorium, 
        Discipline, 
        Teacher, 
        Lesson, 
        LessonAuditorium, 
        LessonGroup, 
        LessonSubGroup, 
        LessonTeacher
    ], 
    safe=True)
db.close()