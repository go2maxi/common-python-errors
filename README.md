# Common Python Errors

This is a small collection of Python errors I've encountered while learning.
I'm saving minimal examples and fixes as I go.

Each folder contains:
- reproduce.py
- fix.py
- README explanation

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
- [AttributeError: 'int' object has no attribute 'append'](./attributeerror-int-object-has-no-attribute-append/)
- [AttributeError: 'dict' object has no attribute 'append'](./attributeerror-dict-object-has-no-attribute-append/)


### ImportError
- [ImportError: cannot import name '...' from '...'](./importerror-cannot-import-name-from/)


### ModuleNotFoundError
- [ModuleNotFoundError: No module named 'requests'](./modulenotfounderror-no-module-named-requests/)
- [ModuleNotFoundError: No module named 'numpy'](./modulenotfounderror-no-module-named-numpy/)


### FileNotFoundError
- [FileNotFoundError: [Errno 2] No such file or directory](./filenotfounderror-no-such-file-or-directory/)


### FileExistsError
- [FileExistsError: [Errno 17] File exists](./fileexistserror-file-exists/)


### JSONDecodeError
- [JSONDecodeError: Expecting value](./jsondecodeerror-expecting-value/)
- [JSONDecodeError: Expecting property name enclosed in double quotes](./jsondecodeerror-expecting-property-name-enclosed-in-double-quotes/)


### UnicodeDecodeError
- [UnicodeDecodeError: 'utf-8' codec can't decode byte](./unicodedecodeerror-utf-8-codec-cant-decode-byte/)


### PermissionError
- [PermissionError: [Errno 13] Permission denied](./permissionerror-errno-13-permission-denied/)


### SyntaxError
- [SyntaxError: invalid syntax](./syntaxerror-invalid-syntax/)


### IndentationError
- [IndentationError: unexpected indent](./indentationerror-unexpected-indent/)


### KeyError
- [KeyError Guide](./keyerror/)
- [KeyError: 'age'](./keyerror-dictionary-key-not-found/)
- [KeyError: 'age'](./keyerror-missing-key-in-json/)


### ValueError
- [ValueError: invalid literal for int()](./valueerror-invalid-literal-for-int/)
- [ValueError: too many values to unpack](./valueerror-too-many-values-to-unpack/)
- [ValueError: not enough values to unpack](./valueerror-not-enough-values-to-unpack/)
- [ValueError: could not convert string to float](./valueerror-could-not-convert-string-to-float/)
- [ValueError: could not convert string to float](./valueerror-invalid-literal-for-float/)


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
