# (1-1) flatten() 함수를 이중 for 문을 이용하여 구현
def flatten(org_list):
    flat_list = []
    for sublist in org_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

org_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(f"org_list = {org_list}")
result_1 = flatten(org_list)
print(f"new_list = {result_1}")

# (1-2) flatten() 함수를 람다 함수와 리스트 축약문을 이용하여 def 사용 없이 한 줄로 구현
result_2 = lambda org_list: [item for sublist in org_list for item in sublist]
print(f"new_list = {result_2(org_list)}")


