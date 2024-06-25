from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('db.db', pragmas={
    'foreign_keys': 1,
    'journal_mode': 'wal',
})

class BModel(Model):
    class Meta:
        database = db

class Group(BModel):
    name = CharField(max_length=10)

class Auditorium(BModel):
    name = CharField(max_length=5)

class Discipline(BModel):
    name = CharField(max_length=100)

db.connect()
db.create_tables(
    [Group], safe=True)
db.close()