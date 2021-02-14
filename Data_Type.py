### Data Type In Python

## Standard Data Type

# 1. Integer

integer_data = 10
print("Data : ", integer_data)
print("- Has Type : ", type(integer_data))

# 2. Float

float_data = 11.5
print("Data : ", float_data)
print("- Has Type : ", type(float_data))

# 3. String

string_data = "This String"
print("Data : ", string_data)
print("- Has Type : ", type(string_data))

# 4. Boolean

bool_data = True
print("Data : ", bool_data)
print("- Has Type : ", type(bool_data))

## Special Data Type

# 1. Complex

complex_data = complex(5, 6)
print("Data : ", complex_data)
print("- Has Type : ", type(complex_data))

# 2. Hexadecimal

hexadecimal_data = hex(0xFF88DDEE)
print("Data : ", hexadecimal_data)
print("- Has Type : ", type(hexadecimal_data))

# 3. List

list_data = ['data', 'data', 2]
print("Data : ", list_data)
print("- Has Type : ", type(list_data))

# 4. Tuple

tuple_data = ('senin', 'kamis', 4)
print("Data : ", tuple_data)
print("- Has Type : ", type(tuple_data))

# 5. Dictionary

dictionary_data = {'name': "Budi", 'umur': 15}
print("Data : ", dictionary_data)
print("- Has Type : ", type(dictionary_data))

# 6. Set

set_data = {1,2,3,3}
print("Data : ", set_data)
print("- Has Type : ", type(set_data))

## C Language Data Type

from ctypes import c_double

data_c_double = c_double(10.5)
print("Data : ", data_c_double)
print("- Has Type : ", type(data_c_double))