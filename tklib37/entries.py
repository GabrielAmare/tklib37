from tkinter import Entry, Checkbutton, IntVar, DoubleVar, StringVar, BooleanVar
from datetime import date, datetime


class IntEntry(Entry):
    def __init__(self, master, **cfg):
        self.var = IntVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, textvariable=self.var, **cfg)

    def get(self):
        return int(self.var.get())

    def set(self, value: int):
        self.var.set(str(value))

    def add(self, delta: int):
        self.set(self.get() + delta)

    def sub(self, delta: int):
        self.set(self.get() - delta)


class FloatEntry(Entry):
    def __init__(self, master, **cfg):
        self.var = DoubleVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, textvariable=self.var, **cfg)

    def get(self):
        return float(self.var.get())

    def set(self, value: float):
        self.var.set(str(value))

    def add(self, delta: float):
        self.set(self.get() + delta)

    def sub(self, delta: float):
        self.set(self.get() - delta)


class StrEntry(Entry):
    def __init__(self, master, **cfg):
        self.var = StringVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, textvariable=self.var, **cfg)

    def get(self):
        return self.var.get()

    def set(self, value: str):
        self.var.set(value)

    def add(self, delta):
        self.set(self.get() + delta)


class BoolEntry(Checkbutton):
    def __init__(self, master, **cfg):
        self.var = BooleanVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, variable=self.var, **cfg)

    def get(self):
        return self.var.get()

    def set(self, value: bool):
        self.var.set(value)

    def toggle(self):
        self.set(not self.get())


class DateEntry(Entry):
    def __init__(self, master, **cfg):
        self.var = StringVar(master, name=cfg.pop("name", None))
        self.set(cfg.pop("value", None))
        super().__init__(master, textvariable=self.var, **cfg)

    def get(self):
        return date.fromisoformat(self.var.get())

    def set(self, value: date):
        if isinstance(value, date):
            self.var.set(value.isoformat())


class DateTimeEntry(Entry):
    def __init__(self, master, **cfg):
        self.var = StringVar(master, name=cfg.pop("name", None))
        self.set(cfg.pop("value", None))
        super().__init__(master, textvariable=self.var, **cfg)

    def get(self):
        return datetime.fromisoformat(self.var.get())

    def set(self, value: datetime):
        if isinstance(value, datetime):
            self.var.set(value.isoformat())


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
