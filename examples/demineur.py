from tklib37 import *
import random

colors = ["black", "#1fcf19", "#1d9119", "#4b6b0f", "#7a630d", "#995711", "#802e05", "#800505", "#330202"]
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
hidden_cell_config = dict(bd=1, relief=RAISED, bg="lightgray", width=2, height=1, font="Helvetica 8 bold")


class Demineur(Table):
    def __init__(self, root, bomb_proba=0.1, n_rows=16, n_cols=20, **cfg):
        super().__init__(root, **cfg)

        self.bomb_proba = bomb_proba
        self.n_bombs = 0
        self.revealed = 0

        self.data = [[self.set_cell(row, col) for col in range(n_cols)] for row in range(n_rows)]
        self.n_cells = self.n_rows * self.n_cols

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                state = self.get_state(row, col)
                count = self.count(row, col)
                state['count'] = count

    def set_cell(self, row, col):
        """Init the cell as a widget and its state"""
        state = dict(bomb=random.random() <= self.bomb_proba, hidden=True)
        if state['bomb']:
            self.n_bombs += 1
        super().set_widget(row, col, Button, command=lambda: self.on_click(row, col), **hidden_cell_config)

        return state

    def get_state(self, row, col):
        """Get the cell state"""
        if 0 <= row < self.n_rows and 0 <= col < self.n_cols:
            return self.data[row][col]

    def count(self, row, col):
        """Count the number of bombs around the cell at (row, col)"""
        count = 0
        for dx, dy in deltas:
            state = self.get_state(row + dx, col + dy)
            if state and state['bomb']:
                count += 1

        return count

    def on_click(self, row, col):
        """Triggered when click on a cell"""
        state = self.get_state(row, col)
        if state and state['hidden']:
            if state['bomb']:
                self.game_over(win=False)
            else:
                self.reveal(row, col)

    def game_over(self, win):
        """Game end"""
        print("Well done !" if win else "You lose !")
        self.master.destroy()

    def reveal(self, row, col):
        """Reveal a cell (and propagates the reveal when cells have no bombs around)"""
        state = self.get_state(row, col)
        if state and state['hidden']:
            state['hidden'] = False
            self.revealed += 1
            count = state['count']
            self.upd_widget(row, col, text=count or '', relief=SUNKEN, bg="white", fg=colors[count])
            if not count:
                for dx, dy in deltas:
                    self.reveal(row + dx, col + dy)

            if self.revealed == self.n_cells - self.n_bombs:
                self.game_over(win=True)


if __name__ == '__main__':
    tk = Tk()

    Demineur(tk, n_rows=16, n_cols=20, bomb_proba=0.1).pack(side=TOP, fill=BOTH, expand=True)

    tk.mainloop()
