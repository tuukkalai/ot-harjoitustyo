class Entry:
    def __init__(
        self,
        entry_id: int,
        heading: str,
        content: str,
        categories: str,
        created: str,
        updated: str
    ) -> None:
        self.__id = entry_id
        self.__heading = heading
        self.__content = content
        if categories:
            self.__categories = list(categories.split(','))
        else:
            self.__categories = []
        self.__created = created
        self.__updated = updated

    @property
    def id(self):
        return self.__id

    @property
    def heading(self):
        return self.__heading

    @heading.setter
    def heading(self, new_heading: str):
        self.__heading = new_heading

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, new_content: str):
        self.__content = new_content

    @property
    def categories(self) -> list:
        return list(self.__categories)

    @categories.setter
    def categories(self, category_list: str):
        if category_list:
            self.__categories = list(category_list.split(','))
        else:
            self.__categories = []

    @property
    def created(self):
        return self.__created

    @property
    def updated(self):
        return self.__updated

    def __str__(self) -> str:
        short_content = self.__content[:50]
        return f'{self.__id}: {self.__heading} - {short_content} {list(self.__categories)}'
