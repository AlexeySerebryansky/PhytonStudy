def decorator_with_args(prefix):

    def decorator(func):

        def wrapper(*args, **kwargs):
            print(f"{prefix} Before func")
            result = func(*args, **kwargs)
            print(f"{prefix} After func")
            return result

        return wrapper

    return decorator


@decorator_with_args("DEBUG")
def say_hello(name: str):
    return f"Hello!, {name}!"


print(say_hello("Masha"))
