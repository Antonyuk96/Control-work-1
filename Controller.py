Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def run():
...     input_from_user = ''
...     while input_from_user != '7':
...         ui.menu()
...         input_from_user = input().strip()
...         if input_from_user == '1':
...             f.show('all')
...             if input_from_user == '2':
...                 f.add()
...                 if input_from_user == '3':
...                     f.show('all')
...                     f.id_edit_del_show('del')
...                     if input_from_user == '4':
...                         f.show('all')
...                         f.id_edit_del_show('edit')
...                         if input_from_user == '5':
...                             f.show('date')
...                             if input_from_user == '6':
...                                 f.show('id')
...                                 f.id_edit_del_show('show')
...                                 if input_from_user == '7':
...                                     ui.goodbuy()
...                                     break
