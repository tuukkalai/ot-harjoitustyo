class Entry:
    def __init__(self, entry_id: int, heading: str, content: str) -> None:
        self._id = entry_id
        self._heading = heading
        self._content = content

    @property
    def id(self):
        return self._id

    @property
    def heading(self):
        return self._heading

    @property
    def content(self):
        return self._content

    def __str__(self) -> str:
        return f'({self._id}) {self._heading} - {self._content[:30]}'
