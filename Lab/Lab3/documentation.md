+----------------+ +----------------+ +------------------+
| Scanner | | SymbolTable | | Pif |
+----------------+ +----------------+ +------------------+
| - st: SymbolTable| | - hashTable: HashTable | | - table: List[Tuple[str, int]]|
| - pif: Pif | +----------------+ +------------------+
| - tokens: List[str] | - insert(element: str) : Tuple[int, int] | | + add(token: str, pos: int): None |
| - operators: List[str] | | + init(self) : None | | + size(): int |
| - separators: List[str] | | + insert(element: str): Tuple[int, int] | | + get_item(index: int): Tuple[str, int] |
| - reserved_words: List[str]| +----------------+ | + get_all(): List[Tuple[str, int]] |
| - __identifier_regex: str | | + search(value: str) : Tuple[int, int] | +------------------+
| - __constant_regex: str | | + __hash_function(key: str) : int |
| - _is_identifier(token): bool| +----------------+
| - _is_constant(token): bool | +----------------+
| - __read_tokens(file_path): List[str] | | HashTable |
| - __read_file_content(file_path): str| +----------------+
| - scan_file(file_path, print_tokens): None| - size: int |
| - get_tokens(content_string): List[str]| - table: List[List[str]] |
+-----------------------------+ | + _hash_function(key: str): int |
| + insert(value: str): Tuple[int, int]|
| + search(value: str): Tuple[int, int]|
| + remove(value: str): None |
+-----------------------------+