import random

# 전체 문자열 30개
strings = ['string1', 'string2', 'string3', 'string4', 'string5', 'string6', 'string7', 'string8', 'string9', 'string10',
           'string11', 'string12', 'string13', 'string14', 'string15', 'string16', 'string17', 'string18', 'string19', 'string20',
           'string21', 'string22', 'string23', 'string24', 'string25', 'string26', 'string27', 'string28', 'string29', 'string30']

# 첫 번째 랜덤 샘플
n1 = random.sample(strings, 15)

# 두 번째 랜덤 샘플 (중복되지 않게)
n2 = random.sample(list(set(strings) - set(n1)), 15)

# 결과 출력
print("월요일에 면접 볼 사람: ", n1)
print("화요일에 면접 볼 사람: ", n2)
