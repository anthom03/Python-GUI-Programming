import tkinter as tk
from tkinter import ttk
from chapter04a.validated_mixin import ValidatedMixin


class ValidatedCombobox(ValidatedMixin, ttk.Combobox):

    def _key_validate(self, proposed, action, **kwargs):
        valid = True
        # if the user tries to delete, just clear the field
        if action == '0':
            self.set('')
            return True

        # get our values list
        values = self.cget('values')
        # Do a case-insensitive match against the entered text
        matching = [
            x for x in values
            if x.lower().startswith(proposed.lower())
        ]
        if len(matching) == 0:
            valid = False
        elif len(matching) == 1:
            self.set(matching[0])
            self.icursor(tk.END)
            valid = False
        return valid

    def _focusout_validate(self, **kwargs):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid
