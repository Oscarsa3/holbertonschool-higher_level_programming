#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        if a == 0 or b == 0:
            div = None
        div = float(a // b)
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(div))
        return div
