string = "My name is Hwang Hyodong"

print("문자 수:", len(string))
print("10번 반복:", string * 10)
print("첫 번째 문자:", string[0])
print("처음 4문자:", string[:4])
print("마지막 4문자:", string[-4:])
print("거꾸로 출력:", string[::-1])
print("첫 번째와 마지막 문자 제거:", string[1:-1])
print("대문자로 변환:", string.upper())
print("소문자로 변환:", string.lower())
print("'a'를 'e'로 변경:", string.replace('a', 'e'))