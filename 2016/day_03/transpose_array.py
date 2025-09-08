# transpose_array.py

def transpose_array(arr:list[list], verbose=False):

  """Ex:
  arr = [
    [1, 2, 3, 4]
    [5, 6, 7, 8],
    [9,10,11,12]
  ]

  new_arr = [
    [1,5,9],
    [2,6,10],
    [3,7,11],
    [4,8,12]
  ]

  """
  num_rows = len(arr)
  num_cols = len(arr[0])

  def validate_arr(arr, num_rows, num_cols):
    for row in arr[1:]:
      if len(row) != num_cols:
        return False
    return True

  arr_is_valid = validate_arr(arr, num_rows, num_cols)
  if not arr_is_valid:
    return "Error: Invalid array structure. Array should be a list of lists, and each row (sublist) should have equal number of columns (items) for each row."

  new_arr = [[] for i in range(num_cols)]

  for i in range(num_rows):
    for j in range(num_cols):
      num = arr[i][j]
      new_arr[j].append(num)

  if verbose:
    v = f"""
OLD ARRAY:
{arr}

NEW ARRAY:
{new_arr}
"""
    return v

  else:
    return new_arr


if __name__ == "__main__":
  arr = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9,10,11,12]]

  new_arr = transpose_array(arr)
  print(new_arr)
