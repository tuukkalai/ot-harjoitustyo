class Entry:
	def __init__(self, entry_id: int, heading: str, content: str) -> None:
		self._id = entry_id
		self._heading = heading
		self._content = content

	def __str__(self) -> str:
		return f'({self._id}) {self._heading} - {self._content[:30]}'