# Common Python Errors

This is a small collection of Python errors I've encountered while learning.  
I'm saving minimal examples and fixes as I go.

Each folder contains:
- reproduce.py
- fix.py
- README explanation

---

## Common Questions

- [Why does Python say "No such file or directory"?](./os-filenotfounderror-no-such-file-or-directory/)
- [Why do I get "AttributeError: 'dict' object has no attribute 'append'"?](./attributeerror-dict-object-has-no-attribute-append/)
- [Why can't Python find my module?](./modulenotfounderror-no-module-named-requests/) (ModuleNotFoundError, example case)
- [Why does Python say "list index out of range"?](./indexerror-list-index-out-of-range/) (IndexError)
- [Why do I get "TypeError" when working with data?](./typeerror-unsupported-operand-type-int-and-list/) (common case)
- [Why does json.loads() fail to parse my data?](./json-jsondecodeerror-expecting-value/) (JSON Errors)
- [Why does Python say "No module named 'my_utils'" even though the file exists?](./modulenotfounderror-local-module-not-found/) (local module case)
- [Why do I get "TypeError: '>' not supported between instances of 'str' and 'int'?](./typeerror-not-supported-between-instances-of-str-and-int/)
- [Why does Python fail when I just press enter on input()?](./valueerror-invalid-literal-empty-string/)
- [Why does Python say "cannot import name" even though the module exists?](./importerror-cannot-import-name-specific/)
- [Why can't Python find my file even though it's in the same folder? (working directory issue)](./os-filenotfounderror-wrong-relative-path/) (relative path issue)

---

## Error Archive

### NameError
- [NameError: name '...' is not defined](./nameerror-name-is-not-defined/)

### UnboundLocalError
- [UnboundLocalError: local variable referenced before assignment](./unboundlocalerror-local-variable-referenced-before-assignment/)

### TypeError
- [TypeError: 'NoneType' object is not subscriptable](./typeerror-nonetype-object-not-subscriptable/)
- [TypeError: list indices must be integers or slices, not str](./typeerror-list-indices-must-be-integers/)
- [TypeError: 'int' object is not callable](./typeerror-int-object-not-callable/)
- [TypeError: can only concatenate str (not "int") to str](./typeerror-can-only-concatenate-str-not-int-to-str/)
- [TypeError: string indices must be integers](./typeerror-string-indices-must-be-integers/)
- [TypeError: object of type 'int' has no len()](./typeerror-object-of-type-int-has-no-len/)
- [TypeError: unhashable type: 'list'](./typeerror-unhashable-type-list/)
- [TypeError: 'int' object is not subscriptable](./typeerror-int-not-subscriptable/)
- [TypeError: greet() missing 1 required positional argument](./typeerror-missing-1-required-positional-argument/)
- [TypeError: unsupported operand type(s) for +: 'int' and 'list'](./typeerror-unsupported-operand-type-int-and-list/)
- [TypeError: write() argument must be str, not dict](./typeerror-write-argument-must-be-str-not-dict/)
- [TypeError: '>' not supported between instances of 'str' and 'int'](./typeerror-not-supported-between-instances-of-str-and-int/)

### IndexError
- [IndexError: list index out of range](./indexerror-list-index-out-of-range/)
- [IndexError: tuple index out of range](./indexerror-tuple-index-out-of-range/)
- [IndexError: list assignment index out of range](./indexerror-list-assignment-index-out-of-range/)
- [IndexError: string index out of range](./indexerror-string-index-out-of-range/)

### AttributeError
- [AttributeError: 'list' object has no attribute 'add'](./attributeerror-list-object-has-no-attribute-add/)
- [AttributeError: 'NoneType' object has no attribute 'append'](./attributeerror-nonetype-append/)
- [AttributeError: 'NoneType' object has no attribute 'split'](./attributeerror-nonetype-object-has-no-attribute-split/)
- [AttributeError: 'tuple' object has no attribute 'append'](./attributeerror-tuple-object-has-no-attribute-append/)
- [AttributeError: 'str' object has no attribute 'append'](./attributeerror-str-object-has-no-attribute-append/)
- [AttributeError: 'dict' object has no attribute 'append'](./attributeerror-dict-object-has-no-attribute-append/)

### ImportError
- [ImportError: cannot import name '...' from '...'](./importerror-cannot-import-name-from/)
- [ImportError: cannot import name 'squareroot' from 'math' (typo)](./importerror-cannot-import-name-specific/)

### ModuleNotFoundError
- [ModuleNotFoundError: No module named 'requests'](./modulenotfounderror-no-module-named-requests/)
- [ModuleNotFoundError: No module named 'numpy'](./modulenotfounderror-no-module-named-numpy/)
- [ModuleNotFoundError: No module named 'yaml'](./modulenotfounderror-no-module-named-yaml/)
- [ModuleNotFoundError: No module named 'pandas'](./modulenotfounderror-no-module-named-pandas/)
- [ModuleNotFoundError: No module named 'my_utils'](./modulenotfounderror-local-module-not-found/)

### OS / File Errors
- [FileNotFoundError: [Errno 2] No such file or directory](./os-filenotfounderror-no-such-file-or-directory/)
- [PermissionError: [Errno 13] Permission denied](./os-permissionerror-errno-13-permission-denied/)
- [PermissionError: [Errno 13] Permission denied: directory](./permissionerror-errno-13-permission-denied-directory/)
- [NotADirectoryError: Not a directory](./os-notadirectoryerror-not-a-directory/)
- [IsADirectoryError: expected file but got directory](./os-isadirectoryerror-expected-file-but-got-dir/)
- [FileNotFoundError: wrong relative path (same folder issue)](./os-filenotfounderror-wrong-relative-path/)

### FileExistsError
- [FileExistsError: [Errno 17] File exists](./fileexistserror-file-exists/)

### JSON Errors
- [JSONDecodeError: Expecting value](./json-jsondecodeerror-expecting-value/)
- [JSONDecodeError: Expecting property name enclosed in double quotes](./jsondecodeerror-expecting-property-name-enclosed-in-double-quotes/)
- [JSONDecodeError: Extra data](./json-jsondecodeerror-extra-data/)
- [TypeError: the JSON object must be str, bytes or bytearray](./json-typeerror-the-json-object-must-be-str-bytes-or-bytearray/)

### UnicodeDecodeError
- [UnicodeDecodeError: 'utf-8' codec can't decode byte](./unicodedecodeerror-utf-8-codec-cant-decode-byte/)

### Pandas Errors
- [UnicodeDecodeError: 'utf-8' codec can't decode byte (read_csv)](./pandas-read-csv-unicodedecodeerror-utf-8-codec-cant-decode/)
- [ParserError: Error tokenizing data](./pandas-read-csv-parsererror-error-tokenizing-data/)
- [KeyError: column not found](./pandas-keyerror-column-not-found/)
- [ValueError: Length mismatch](./pandas-valueerror-length-mismatch/)
- [IndexError: single positional indexer is out-of-bounds](./pandas-indexerror-single-positional-indexer-is-out-of-bounds/)

### SyntaxError
- [SyntaxError: invalid syntax](./syntaxerror-invalid-syntax/)

### IndentationError
- [IndentationError: unexpected indent](./indentationerror-unexpected-indent/)

### KeyError
- [KeyError Guide](./keyerror/)
- [KeyError: 'age' (Python Dictionary)](./keyerror-dictionary-key-not-found/)
- [KeyError: 'age' (JSON Data)](./keyerror-missing-key-in-json/)

### ValueError
- [ValueError: invalid literal for int() (non-numeric string)](./valueerror-invalid-literal-for-int/)
- [ValueError: too many values to unpack](./valueerror-too-many-values-to-unpack/)
- [ValueError: not enough values to unpack](./valueerror-not-enough-values-to-unpack/)
- [ValueError: could not convert string to float](./valueerror-could-not-convert-string-to-float/)
- [ValueError: could not convert string to float](./valueerror-invalid-literal-for-float/)
- [ValueError: invalid literal for int() (empty input)](./valueerror-invalid-literal-empty-string/)

### RecursionError
- [RecursionError: maximum recursion depth exceeded](./recursionerror-maximum-recursion-depth-exceeded/)

### ZeroDivisionError
- [ZeroDivisionError: division by zero](./zerodivisionerror-division-by-zero/)

---

More error cases will be added as I encounter them while learning Python.

---

## Related Mini Projects

- [Contact Log](./mini-projects/contact-log/): `TypeError`, `AttributeError`
- [File Log Reader](./mini-projects/file-log-reader/): `FileNotFoundError`, `PermissionError`
- [User Data Processor](./mini-projects/user-data-processor/): `ModuleNotFoundError`, `IndexError`, `TypeError`
- [JSON Config Loader](./mini-projects/json-config-loader/): `JSONDecodeError`, `KeyError`, `TypeError`, `ValueError`

