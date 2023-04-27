import Note
import File_Operation
import ui
number = 6
def add():
    note = ui.create_note(number)
    array = File_Operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
            array.append(note)
            File_Operation.write_file(array, 'a')
            print('Добавление заметки')
            def show(text):
                logic = True
                array = File_Operation.read_file()
                if text == 'date':
                    date = input('Дата (день, месяц, год')
                    for notes in array:
                        if text == 'all':
                            logic = False
                            print(Note.Note.map_note(notes))
                            if text == 'id':
                                logic = False
                                print('ID: ' + Note.Note.get_id(notes))
                                if text == 'date':
                                    logic = False
                                    if date in Note.Note.get_date(notes):
                                        print(Note.Note.map_note(notes))
                                        if logic == True:
                                            print('Заметки отсутствуют')
                                            def id_edit_del_show(text):
                                                id = input('Id заметки: ')
                                                array = File_Operation.read_file()
                                                logic = True
                                                for notes in array:
                                                    if id == Note.Note.get_id(notes):
                                                        logic = False
                                                        if text == 'edit':
                                                            note = ui.create_note(number)
                                                            Note.Note.set_title(notes, note.get_title())
                                                            Note.Note.set_body(notes, note.get_body())
                                                            Note.Note.set_date(notes)
                                                            print('Добавлены изменения в заметку')
                                                            if text == 'del':
                                                                array.remove(notes)
                                                                print('Заметки больше нет')
                                                                if text == 'show':
                                                                    print(Note.Note.map_note(notes))
                                                                    if logic == True:
                                                                        print('Неверный ID')
                                                                        File_Operation.write_file(array, 'a')
                                                                        
                                                                    
                

