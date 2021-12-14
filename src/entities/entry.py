class Entry:
    def __init__(self, entry_id: int, heading: str, content: str, categories: list) -> None:
        self._id = entry_id
        self._heading = heading
        self._content = content
        if categories:
            self._categories = list(categories.split(','))
        else:
            self._categories = []

    @property
    def id(self):
        return self._id

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, new_heading):
        if 0 < len(new_heading) < 60:
            self._heading = new_heading

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_content):
        if 0 < len(new_content) < 500:
            self._content = new_content

    @property
    def categories(self) -> list:
        return list(self._categories)

    def __str__(self) -> str:
        short_content = self._content[:30]
        return f'{self._id}: {self._heading} - {short_content} {list(self._categories)}'
