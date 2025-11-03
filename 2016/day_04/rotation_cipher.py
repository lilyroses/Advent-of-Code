from string import ascii_lowercase, printable


def rotation_cipher(s, rot, charset=ascii_lowercase):
  """
  s : str
   The string to rotate.

  rot : int
   The value to rotate each letter in the charset by.

  charset : str|list[str]
    The set of characters to rotate.
  """

  nums = range(len(charset))
  char_map = dict(zip(charset, nums))
  nums_map = dict(zip(nums, charset))

  rot_nums = [num+rot if num+rot <= nums[-1]
              else (num+rot) % len(charset)
              for num in nums]
  rot_chars = [nums_map[n] for n in rot_nums]
  rot_map = dict(zip(charset, rot_chars))

  rs = ""
  for char in s:
    if char in charset:
      rs += rot_map[char]
    else:
      rs += char

  return rs


if __name__ == "__main__":
  s = "Hello, World!"
  rot = 13
  charset = printable

  rs = rotation_cipher(s, rot, charset)
  print(f"\nOriginal message:\t{s}")
  print(f"Rotation:\t{rs}")


