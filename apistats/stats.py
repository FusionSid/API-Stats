import json
import inspect
import functools

class Stats:
    file_name = "stats.json"

    @classmethod
    def update_stats(cls, *args, **kwargs):
        global name
        try:
            name = kwargs["name"]
        except KeyError:
            name = None


        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                global name
                if name is None:
                    name = str(func.__name__)

                try:
                    with open(cls.file_name) as f:
                        data = json.load(f)
                except FileNotFoundError:
                    stuff = {}
                    with open(cls.file_name, 'w') as f:
                        json.dump(stuff, f, indent=4)
                    data = {}

                try:
                    data[name] += 1
                except KeyError:
                    data[name] = 1

                with open(cls.file_name, 'w') as f:
                    json.dump(data, f, indent=4)
                
                if inspect.iscoroutinefunction(func):
                    return await func(*args, **kwargs)
                else:
                    return func(*args, **kwargs)

            return wrapped
        return wrapper