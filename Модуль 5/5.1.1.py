class StringVar:
    s = '***Default***'

    def set(self, new_string):
        self.s = new_string

    def get(self):
        return self.s


text_a = StringVar()
print(text_a.get())
text_a.set(input('Введите новое значение строки: '))
print(text_a.get())
