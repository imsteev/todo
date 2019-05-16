from dataclasses import dataclass

@dataclass
class TodoItem:
    text: str
    when: str = ""
    complete: bool = False

    def to_json(self):
        return {
            'text': self.text,
            'when': self.when,
            'complete': self.complete
        }