from tkinter import Entry, Checkbutton, IntVar, DoubleVar, StringVar, BooleanVar
from datetime import date, datetime, timedelta


class IntEntry(Entry):
    def __init__(self, master, **cfg):
        self.step = cfg.pop("step", None)

        self.var = IntVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, textvariable=self.var, **cfg)

        if self.step is not None and isinstance(self.step, int):
            self.bind("<KeyPress-Up>", lambda _: self.add(self.step))
            self.bind("<KeyPress-Down>", lambda _: self.sub(self.step))

    def get(self) -> int:
        return int(self.var.get())

    def set(self, value: int):
        self.var.set(str(value))

    def add(self, delta: int):
        self.set(self.get() + delta)

    def sub(self, delta: int):
        self.set(self.get() - delta)


class FloatEntry(Entry):
    def __init__(self, master, **cfg):
        self.step = cfg.pop("step", None)

        self.var = DoubleVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, textvariable=self.var, **cfg)

        if self.step is not None and isinstance(self.step, int):
            self.bind("<KeyPress-Up>", lambda _: self.add(self.step))
            self.bind("<KeyPress-Down>", lambda _: self.sub(self.step))

    def get(self) -> float:
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

    def get(self) -> str:
        return self.var.get()

    def set(self, value: str):
        self.var.set(value)

    def add(self, delta):
        self.set(self.get() + delta)


class BoolEntry(Checkbutton):
    def __init__(self, master, **cfg):
        self.var = BooleanVar(master, value=cfg.pop("value", None), name=cfg.pop("name", None))
        super().__init__(master, variable=self.var, **cfg)

    def get(self) -> bool:
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

    def get(self) -> date:
        return date.fromisoformat(self.var.get())

    def set(self, value: date):
        if isinstance(value, date):
            self.var.set(value.isoformat())


class DateTimeEntry(Entry):
    def __init__(self, master, **cfg):
        self.step = cfg.pop("step", None)

        self.var = StringVar(master, name=cfg.pop("name", None))
        self.set(cfg.pop("value", None))
        super().__init__(master, textvariable=self.var, **cfg)

        if self.step is not None and isinstance(self.step, timedelta):
            self.bind("<KeyPress-Up>", lambda _: self.add(self.step))
            self.bind("<KeyPress-Down>", lambda _: self.sub(self.step))

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
