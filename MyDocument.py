documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
      '1': ['2207 876234', '11-2'],
      '2': ['10006'],
      '3': []
    }



def find_autor_document(document):
  '''P – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит'''
  
  number_doc = input('Введите номер документа, чтобы узнать владельца: ')
  document_id = None
  for id, doc in enumerate(document):
    if number_doc == doc['number']:
      document_id = id
  if document_id == None:
    print(f'Документ с номером {number_doc} не найден.')
  else:
    autor_document = document[document_id]['name']
    print(f'Документ {number_doc} принадлежит {autor_document}.') 
  return document_id



def find_shelf_document(directory):
  '''S – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится; Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ'''
  
  number_doc = input('Введите номер документа: ')
  shelf_id = None
  for id_sh, shelf in directory.items():
    if number_doc in shelf:
      shelf_id = id_sh
  if shelf_id == None:
    print(f'Документа с номером {number_doc} не найдено на полках.')
  else:
    print(f'Документ {number_doc} находится на полке {shelf_id}.')
  return shelf_id , number_doc



def move_doc(directory,func_result):
  '''m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку'''

  if func_result[0] != None:
    number_shelf = input('Введите номер полки, на котороую следует переместить документ: ')
    if number_shelf in directory.keys():
      print(f'Перемещено с полки {func_result[0]} на {number_shelf}')
      for key, val_dir in directory.items():
        if func_result[1] in val_dir:
          val_dir.remove(func_result[1])
        if number_shelf in key:
          val_dir.append(func_result[1])
      print(directory)
    else:
      print('Такой полки нет!')
      return
  else:
    return



def list_document(directory,document):
  '''l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"'''
  
  print('Перечень документов \n','\rТип', '\t',"'Номер документа'", '\t',"'Владелец:'")
  for doc_s in directory.values():
    for d in doc_s:
      for docs_d in document:
        if d in docs_d['number']:
          print(f'''{docs_d['type']}   "{docs_d['number']}"   "{docs_d['name']}"''')
          break
      else:
        print(f'Нет данных \t"{d}"')


    
def add_new_doc(directory,document):
  '''a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.'''
  
  new_doc_shelf = input('Введите полку для нового документа: ')
  if new_doc_shelf in directory.keys():
    new_doc_name = input('Введите номер нового документа: ')
    new_doc_type = input('Введите тип документа: ')
    new_doc_own = input('Введите владельца документа: ')
    for key, val in directory.items():
      if new_doc_shelf in key:
        val.append(new_doc_name)
        document.append({'type': new_doc_type, 'number': new_doc_name, 'name': new_doc_own})
  else:
    print('Такой полки нет!')
    return
  print('Документ добавлен на полки!','\n',directory,'\n','Документ добавлен в каталог!','\n',document)



def add_new_shell(directory):
  '''as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень'''

  new_shelf = input('Введите название/номер новой полки: ')
  if new_shelf not in directory.keys():
    directory[new_shelf] = list()
    print(f'Добавлена полка {new_shelf}')
    return
  else:
    print('Такая полка уже есть!')
    return



def del_shell(directory):
  '''ds – del shelf – команда, которая спросит номер полки и удалит её'''

  del_shelf = input('Введите название/номер полки, которую надо удалить: ')
  if del_shelf in directory.keys():
    del directory[del_shelf]
    print(f'Полка {del_shelf} удалена')
    return
  else:
    print('Такой полки нет!')
    return


    
def del_doc(document,directory):
  '''d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок'''
  
  del_document = str(input('Введите название документа, который необходимо удалить: '))     
  for id, val_doc in enumerate(document):
    if del_document == val_doc['number']:
      del document[id]
      print('Документ удален из каталога!','\n',document)
      break
  else:
    print((f'Документ с номером {del_document} не найден в каталоге'))
  for val_dir in directory.values():
    if del_document in val_dir:
      val_dir.remove(del_document)
      print('Документ удален с полок!','\n',directory)
      break
  else:
    print((f'Документ с номером {del_document} не найден на полках'))
    return
    


def main():
  while True:
    command = input('w  - Показать списки \nl  - Список всех документов \np  - Узнать автора документа по номеру \ns  - Узнать номер полки на которой хранится документ \na  - Добавить новый документ \nm  - Переместить документ на другую полку \nas - Добавить новую полку  \nd  - Удалить документ из каталога и полок \nds - Удалить полку \nq  - Выход из программы \nВведите команду: ')
    print('----------')
    if command == 'p':
      find_autor_document(documents)
      print()
    elif command == 'w':
      print('Каталог документов:\n',documents,'\nПолки:\n',directories,'\n')
    elif command == 's':
      find_shelf_document(directories)
      print()
    elif command == 'l':
      list_document(directories, documents)
      print()
    elif command == 'a':
      add_new_doc(directories,documents)
      print()
    elif command == 'm':
      func_shelf_r = find_shelf_document(directories)
      move_doc(directories,func_shelf_r)
      print()
    elif command == 'as':
      add_new_shell(directories)
      print()
    elif command == 'd':
      del_doc(documents,directories)
      print()
    elif command == 'ds':     
      del_shell(directories)
      print()
    elif command == 'q':
      print('Exit')
      break
main()
