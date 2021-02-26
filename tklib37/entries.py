from tkinter import Entry, Checkbutton, IntVar, DoubleVar, StringVar, BooleanVar
from datetime import date, datetime, timedelta


class IntEntry(Entry):
    def __init__(self, master, step=None, callback=None, name=None, value=None, **cfg):
        self.value = value
        self.callback = callback
        self.var = IntVar(master, value=value, name=name)
        super().__init__(master, textvariable=self.var, **cfg)

        if isinstance(step, int):
            self.bind("<KeyPress-Up>", lambda _: self.add(step))
            self.bind("<KeyPress-Down>", lambda _: self.sub(step))

        if hasattr(callback, "__call__"):
            self.var.trace("w", self.on_change)

    def on_change(self, name, index, mode):
        value = self.get()
        if self.value != value:
            self.value = value
            self.callback(value)

    def get(self) -> int:
        return int(self.var.get())

    def set(self, value: int):
        self.var.set(str(value))

    def add(self, delta: int):
        self.set(self.get() + delta)

    def sub(self, delta: int):
        self.set(self.get() - delta)


class FloatEntry(Entry):
    def __init__(self, master, step=None, callback=None, name=None, value=None, **cfg):
        self.value = value
        self.callback = callback
        self.var = DoubleVar(master, value=value, name=name)
        super().__init__(master, textvariable=self.var, **cfg)

        if step is not None and isinstance(step, int):
            self.bind("<KeyPress-Up>", lambda _: self.add(step))
            self.bind("<KeyPress-Down>", lambda _: self.sub(step))

        if hasattr(callback, "__call__"):
            self.var.trace("w", self.on_change)

    def on_change(self, name, index, mode):
        value = self.get()
        if self.value != value:
            self.value = value
            self.callback(value)

    def get(self) -> float:
        return float(self.var.get())

    def set(self, value: float):
        self.var.set(str(value))

    def add(self, delta: float):
        self.set(self.get() + delta)

    def sub(self, delta: float):
        self.set(self.get() - delta)


class StrEntry(Entry):
    def __init__(self, master, callback=None, name=None, value=None, **cfg):
        self.value = value
        self.callback = callback
        self.var = StringVar(master, value=value, name=name)
        super().__init__(master, textvariable=self.var, **cfg)

        if hasattr(callback, "__call__"):
            self.var.trace("w", self.on_change)

    def on_change(self, name, index, mode):
        value = self.get()
        if self.value != value:
            self.value = value
            self.callback(value)

    def get(self) -> str:
        return self.var.get()

    def set(self, value: str):
        self.var.set(value)

    def add(self, delta):
        self.set(self.get() + delta)


class BoolEntry(Checkbutton):
    def __init__(self, master, callback=None, name=None, value=None, **cfg):
        self.value = value
        self.callback = callback
        self.var = BooleanVar(master, value=value, name=name)
        super().__init__(master, variable=self.var, **cfg)

        if hasattr(callback, "__call__"):
            self.var.trace("w", self.on_change)

    def on_change(self, name, index, mode):
        value = self.get()
        if self.value != value:
            self.value = value
            self.callback(value)

    def get(self) -> bool:
        return self.var.get()

    def set(self, value: bool):
        self.var.set(value)

    def toggle(self):
        self.set(not self.get())


class DateEntry(Entry):
    def __init__(self, master, step=None, callback=None, name=None, value=None, **cfg):
        self.value = value
        self.callback = callback

        self.var = StringVar(master, name=name)
        self.set(value)
        super().__init__(master, textvariable=self.var, **cfg)

        if hasattr(callback, "__call__"):
            self.var.trace("w", self.on_change)

    def on_change(self, name, index, mode):
        value = self.get()
        if self.value != value:
            self.value = value
            self.callback(value)

    def get(self) -> date:
        return date.fromisoformat(self.var.get())

    def set(self, value: date):
        if isinstance(value, date):
            self.var.set(value.isoformat())


class DateTimeEntry(Entry):
    def __init__(self, master, step=None, callback=None, name=None, value=None, **cfg):
        self.value = value
        self.callback = callback

        self.var = StringVar(master, name=name)
        self.set(value)
        super().__init__(master, textvariable=self.var, **cfg)

        if isinstance(step, timedelta):
            self.bind("<KeyPress-Up>", lambda _: self.add(step))
            self.bind("<KeyPress-Down>", lambda _: self.sub(step))

        if hasattr(callback, "__call__"):
            self.var.trace("w", self.on_change)

    def on_change(self, name, index, mode):
        value = self.get()
        if self.value != value:
            self.value = value
            self.callback(value)

    def get(self) -> datetime:
        return datetime.fromisoformat(self.var.get())

    def set(self, value: datetime):
        if isinstance(value, datetime):
            self.var.set(value.isoformat())

    def add(self, delta: timedelta):
        self.set(self.get() + delta)

    def sub(self, delta: timedelta):
        self.set(self.get() - delta)


def TypedEntry(root, type_, **cfg):
    if type_ is str:
        return StrEntry(root, **cfg)
    elif type_ is int:
        return IntEntry(root, **cfg)
    elif type_ is float:
        return FloatEntry(root, **cfg)
    elif type_ is bool:
        return BoolEntry(root, **cfg)
    elif type_ is date:
        return DateEntry(root, **cfg)
    elif type_ is datetime:
        return DateTimeEntry(root, **cfg)
    else:
        raise Exception(f"TypedEntry doesn't handle {type_.__name__} type !")
