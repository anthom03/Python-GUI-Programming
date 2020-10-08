from tkinter import ttk

from chapter04a.validated_mixin import ValidatedMixin


class RequiredEntry(ValidatedMixin, ttk.Entry):

    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid
