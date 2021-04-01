def test_einfugen(guest_list, length):
    assert length + 1 == len(guest_list)


def valid_name(name):
    if name != "":
        nr = 0
        while nr < len(name) and name[nr] in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
            nr += 1
        if nr < len(name):
            raise ValueError("Invalider name")
        else:
            return name
    else:
        raise ValueError("Invalider name")
