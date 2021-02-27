from .Table import Table


class KeyTable(Table):
    def __init__(self, root, **cfg):
        super().__init__(root, **cfg)
        self.row_map, self.col_map = {}, {}

    def _get_row(self, row):
        return self.row_map.get(row, row)

    def _get_col(self, col):
        return self.col_map.get(col, col)

    def _get_key(self, row, col):
        return self._get_row(row), self._get_col(col)

    def bind_row(self, key, row):
        self.row_map[key] = row

    def bind_col(self, key, col):
        self.col_map[key] = col

    def set_widget(self, row, col, cls, **cfg):
        """Set a widget at a row & column"""
        return self._set_widget(*self._get_key(row, col), cls, **cfg)

    def get_widget(self, row, col):
        """Get a widget by it's row & column"""
        return self._get_widget(*self._get_key(row, col))

    def upd_widget(self, row, col, **cfg):
        """Update a widget config"""
        return self._upd_widget(*self._get_key(row, col), **cfg)

    def del_widget(self, row, col):
        """Delete a widget"""
        return self._del_widget(*self._get_key(row, col))

    def invert_widgets(self, old_row, old_col, new_row, new_col):
        """Invert two widgets"""
        return self._invert_widgets(*self._get_key(old_row, old_col), *self._get_key(new_row, new_col))

    def invert_rows(self, old_row, new_row):
        """Invert two rows"""
        return self._invert_rows(self._get_row(old_row), self._get_row(new_row))

    def invert_cols(self, old_col, new_col):
        """Invert two columns"""
        return self._invert_rows(self._get_row(old_col), self._get_row(new_col))
