class Question:
    def __init__(self, text: object, answer: object) -> object:
        self.text = text
        self.answer = answer

    def func(self):
        print(self.text, self.answer)


