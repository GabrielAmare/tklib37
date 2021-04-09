from tklib37 import *


def popup_login(root, on_confirm):
    tl = Toplevel(root)
    tl.transient(root)

    def confirm(data):
        on_confirm(data)
        tl.destroy()

    tl.resizable(False, False)
    tl.title("Créer un compte")
    tl.focus_force()

    row_config = dict(padx=2, pady=4, font="Helvetica 12")
    confirm_config = dict(font="Helvetica 10 italic", padx=2, pady=4, bd=1, bg="#64e647")
    cancel_config = dict(font="Helvetica 10 italic", padx=2, pady=4, bd=1, bg="#e65247")

    form = SimpleForm(tl, padx=50, pady=50)

    form.add_entry(name="username", label="Nom d'utilisateur", type_=str, **row_config)
    form.add_entry(name="password", label="Mot de passe", type_=str, **row_config)
    form.add_entry(name="subscribe", label="Recevoir la newsletter", type_=bool, **row_config)

    form.set_handler(
        confirm=dict(text="Confirmer", command=confirm, **confirm_config),
        cancel=dict(text="Annuler", command=tl.destroy, **cancel_config),
        padx=2, pady=4
    )

    form.pack(side=TOP, fill=BOTH, expand=True)


if __name__ == '__main__':
    tk = Tk()

    popup_login(tk, lambda data: print(data))

    tk.mainloop()
