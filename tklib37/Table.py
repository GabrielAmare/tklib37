from tkinter import Frame, NSEW


class Table(Frame):
    def __init__(self, root, **cfg):
        super().__init__(root, **cfg)
        self.widgets = {}

        self.row_weights = {}
        self.col_weights = {}

    def set_widget(self, row, col, cls, **cfg):
        widget = cls(self, **cfg)
        widget.grid(row=row, column=col, sticky=NSEW)
        self.widgets[(row, col)] = widget

        if row not in self.row_weights:
            self.row_weights[row] = 1
            self.rowconfigure(row, weight=1)

        if col not in self.col_weights:
            self.col_weights[col] = 1
            self.columnconfigure(col, weight=1)

        return widget

    def upd_widget(self, row, col, **cfg):
        widget = self.get_widget(row, col)
        if widget:
            widget.configure(**cfg)

    def get_widget(self, row, col):
        return self.widgets.get((row, col), None)

    def del_widget(self, row, col):
        widget = self.get_widget(row, col)
        if widget:
            widget.grid_forget()
            widget.destroy()
            del self.widgets[(row, col)]
