# AttributeError: 'NoneType' object has no attribute 'append'

### Error Traceback

When I ran the script, Python pointed directly to the line where I called `.append()` on `None`.

```text
File "reproduce.py", line 4, in <module>
    data.append("new item")
AttributeError: 'NoneType' object has no attribute 'append'

### Why it happened

The function I used didn't find anything, so it returned `None`.  
Python is strict about this: `NoneType` doesn't have an `.append()` method.

### My observation

I keep forgetting that `None` and an empty list `[]` are completely different things.  
Added a simple check so the script doesn't crash next time.