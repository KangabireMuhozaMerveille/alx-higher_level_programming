#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if my_list_1 is None or my_list_2 is None:
        for i in range(list_length):
            new_list[i] = 0
        return new_list
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            continue
    return new_list
