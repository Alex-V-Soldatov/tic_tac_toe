class Board:
    """Класс, который описывает игровое поле."""
    
    

    def __init__(self):
       # self.field_size = 3
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        ) 
        
    def field_size(self):
        self.field_size = 3
        return self.field_size 