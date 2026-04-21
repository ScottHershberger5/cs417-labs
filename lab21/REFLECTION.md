1. Which section gave you a bug mypy caught that you wouldn’t have caught by reading the code? Be specific — what was the error message, what was the underlying mistake, and why is that kind of mistake easy to make in Python?

Section 4 gave me a message and caught the typo bug that I definetely would have been looking for for a while. Its easy to make a typo, everyone does, but its nice to have mypy to catch that kind of stuff.

2. Runtime cost. Type hints don’t run at runtime — Python ignores them. Mypy is a separate tool you choose to run. What’s the cost and benefit of that design choice? What would change if Python enforced types at runtime the way Java does?

The benefit of that design choice is that running your code is faster and more efficent as it skips type hints at runtime. The downsides is that if you dont specifically install mypy and run it seperately, your type hints are ignored and your code could run with unwanted errors. If python enforced the type hints at runtime like java, it would take your program longer to run, but everytime you ran your code you would get a result closer to what you intended, you wouldnt get any silly little bugs like typos or type mismatches.

3. TypedDict vs plain dict. A dict can play two roles: a record with a fixed set of named fields (like Lab 18’s roster row), or a mapping from variable keys to values (like Lab 20’s completed dict that maps submission IDs to results). For each of these two cases, would you reach for TypedDict or dict[K, V], and why?

Use TypedDict when your dict has a fixed type fields (like a roster row with name, email, and grade), because it lets mypy verify that you're accessing only valid keys with the correct types. Use dict[K, V] when your dict is a mapping with a variable number of keys you don't know ahead of time (like submission IDs mapped to results), because the keys are dynamic and can be any type.