Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Note:
...     def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
...         self.id = id
...         self.title = title
...         self.body = body
...         self.date = date
...         def get_id(note):
...             return note.id
...         def get_title(note):
...             return note.title
...         def get_body(note):
...             return note.body
...         def get_date(note):
...             return note.date
...         def set_id(note):
...             note.id = str(uuid.uuid1())[0:3]
...             def set_title(note, title):
...                 note.title = title
...                 def set_body(note, body):
...                     note.body = body
...                      def set_date(note):
...                          
SyntaxError: unexpected indent
>>> def set_date(note):
...     note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
...     ef to_string(note):
...         
SyntaxError: invalid syntax
>>> def to_string(note):
...     return note.id + ';' + note.title + ';' + note.body + ';' + note.date
... def map_note(note):
...     
SyntaxError: invalid syntax
>>> def map_note(note):
...     return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date
