# Why does this error happen?

This error occurs when a variable you expect to be a dictionary is actually `None`.

Common real-world causes:

- API call failure returning None
- Database query returning no result
- A function missing an explicit return statement

Since `None` is not subscriptable, this line:

    user["name"]

raises:

TypeError: 'NoneType' object is not subscriptable


# How to prevent it

## 1. Explicit validation

Always verify the object before accessing it:

    if user is not None:
        print(user.get("name"))

## 2. Short-circuit evaluation

Use Python’s short-circuit behavior:

    safe_user = user or {}
    print(safe_user.get("name", "Unknown"))

If `user` is None, an empty dictionary is used instead,
preventing the application from crashing.


# Practical Insight

In production systems, it is better to fix the root cause
(API reliability, DB consistency) rather than only masking the symptom.
Defensive coding should complement proper error handling,
not replace it.
