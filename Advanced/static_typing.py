"""
    1. Type Hinting : 
        def fun(a: int, b: str) -> int:
            pass
    2. Variable annotation :
        a: str = "Shubhi"
        b: int = 26
    3. Type Hinting and Variable annotation do not enforce type checking
    4. To enforce Type checking we must install mypy package
    5. For type hinting of complex datatypes such as List of string, Dictionary of string key and int value,
    we have a Package called  -"typing"
        from typing import List, Dict
        names: List[str] = ["Shubhi", "Ekta"]
        map: Dict[str, int] = {"x":1, "y": 2}
    6. Procs of Type Hinting - 
        a. They help to document your code - not a replacement of docstrings though
        b. Helps in maintaing cleaner codebase
        c. Improve linting capabilities if your code editor
    7. Cons - 
        a. can be tedious to add.
    8. Python will always remain dynamically typed language.
"""