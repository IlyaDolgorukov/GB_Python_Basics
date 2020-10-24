from random import randrange, shuffle


class Player:
    def __init__(self, name):
        self.name = name
        self.digits = list(range(1, 91))
        self.card = []
        self.create_card()

    def create_card(self):
        for row in range(3):
            self.card.append(self.create_row())

    def create_row(self):
        row = [0 for x in range(9)]
        for col in range(5):
            while True:
                ind = randrange(len(self.digits))
                pos = 8 if self.digits[ind] == 90 else self.digits[ind] // 10
                if row[pos] == 0:
                    row[pos] = self.digits.pop(ind)
                    break
        return row

    def show_num(self, num):
        result = '  '
        if num > 0:
            result = str(num) if num > 9 else f' {num}'
        elif num < 0:
            result = ' -'
        return result

    def render_card(self):
        ln = (33 - len(self.name)) // 2
        head = f'{"-" * ln} {self.name} {"-" * ln}'
        print(f'{head}{"-" if len(head) < 35 else ""}')
        for row in self.card:
            for col in row:
                print(self.show_num(col), end='  ')
            print()
        print('-' * 35)
        print()

    def get_num(self, num):
        exist = False
        for i, row in enumerate(self.card):
            for j, col in enumerate(row):
                if num == col:
                    exist = True
                    self.card[i][j] = -1
        return exist

    def is_win(self):
        card_sum = 0
        for row in self.card:
            for col in row:
                if col > 0:
                    card_sum += col
        return card_sum == 0


class Game:
    def __init__(self, human_player, computer_player):
        self.human = human_player
        self.computer = computer_player
        self.digits = list(range(1, 91))
        shuffle(self.digits)

    def play(self):
        win = False
        while not win:
            win = self.next_turn()
        print(f'{win.name} выиграл!')

    def next_turn(self):
        result = False
        number = self.digits.pop()
        self.render(number)
        self.computer.get_num(number)
        if self.computer.is_win():
            result = self.computer
        else:
            strike = ''
            while strike != 'n' and strike != 'y':
                strike = input('Хотите зачеркнуть? (y/n): ')
            has_num = self.human.get_num(number)
            if strike == 'y':
                if not has_num:
                    result = self.computer
                elif self.human.is_win():
                    result = self.human
            elif has_num:
                result = self.computer
        return result

    def render(self, number):
        print()
        self.human.render_card()
        self.computer.render_card()
        print(f'Новый бочонок {number}, осталось {len(self.digits)}')


human = Player('Игорок')
computer = Player('Компьютер')
game = Game(human, computer)
game.play()
