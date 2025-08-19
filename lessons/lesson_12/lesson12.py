import logging


def division (a, b):
    res = 0
    try:
        if b % 2 == 0:
            raise ValueError("Odd forbiden!")
        res = a / b
    except ZeroDivisionError:
        print("Zerro deivision !")

    except Exception as e:
        logging.error((f"Error: {e}"))
    else:
        print("Well Done")
    finally:
        print("Finishe")

    return res

try:
    print(division(10, 2))
except ValueError:
    print("Valu error has been raised")
# print(division(10, "5"))
