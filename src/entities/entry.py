class Entry:
	def __init__(self, heading, content, owner) -> None:
		self._heading = heading
		self._content = content
		self._owner = owner

	def get_heading(self):
		return self._heading

	def get_content(self):
		return self._content