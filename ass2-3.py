import numpy as np


array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

dot_product = np.dot(array1, array2)
print(f"내적 : {dot_product}")

cosine_similarity = dot_product / (np.linalg.norm(array1) * np.linalg.norm(array2))
print(f"코사인 유사도: {cosine_similarity}")

euclidean_distance = np.linalg.norm(array1 - array2)
print(f"유클리드 거리: {euclidean_distance}")

standardized_array1 = (array1 - np.mean(array1)) / np.std(array1)
print(f"표준화: {standardized_array1}")

outer_product = np.outer(array1, array2)
print(f"외적: \n{outer_product}")