from gameparts import Board
# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError.
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    game.display()
    while True:
        try:
            # Пользователь вводит номер строки.
            row = int(input('Введите номер строки: '))
            # Если введённое значение меньше нуля или больше или равно
            # field_size (это значение равно трём, оно хранится в модуле
            # parts.py)...
            if row < 0 or row >= 3:
                # ...выбросить исключение FieldIndexError.
                raise FieldIndexError
            column = int(input("Введите номер строки: "))
            if column < 0 or column >= 3:
                # ...выбросить исключение FieldIndexError.
                raise FieldIndexError
        except FieldIndexError:
            
        #     print (f'Значение должно быть не отрицательным и меньше трех')
        #     print('Пожалуйста, введите значения для строки и столбца заново.')
            continue
        
        except ValueError:
            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
            continue
        
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            continue
        else:
            break
        
        
            
    
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()
    


if __name__ == '__main__':
    main() 