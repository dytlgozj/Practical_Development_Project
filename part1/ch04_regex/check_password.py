import re


def check_password(password):
    result = re.search(r".{8,}", password)
    if not result:
        print("최소 8글자 이상이어야 합니다.")
        return

    print(password)
    result = re.search(r"[a-z]+", password)
    if not result:
        print("최소 1개 이상의 소문자가 필요합니다.")
        return

    result = re.search(r"[A-Z]+", password)
    if not result:
        print("최소 1개 이상의 대문자가 필요합니다.")
        return

    result = re.search(r"[0-9]+", password)
    if not result:
        print("최소 1개 이상의 숫자가 필요합니다.")
        return

    result = re.search(r"[@#$%^&+=]", password)
    if not result:
        print("최소 1개 이상의 특수문자(@#$%^&+=)가 필요합니다.")
        return

    print("비밀번호 검증에 성공하였습니다.")


check_password("A@sdf1234")
