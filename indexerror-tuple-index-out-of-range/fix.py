# fix.py

values = (10, 20, 30)
index = 3

print("Checking index boundaries before access...")

# len()을 사용하여 유효한 인덱스인지 먼저 검사
if index < len(values):
    print(values[index])
else:
    print(f"Error: Index {index} is out of range. Valid range: 0 to {len(values) - 1}")

# 대안: 올바른 인덱스 예시
print("\nAccessing valid index 2:")
print(values[2])