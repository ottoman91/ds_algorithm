def reverse_order(list_characters):


left_index = 0
right_index = len(list_characters) - 1

while left_index < right_index:
  list_characters[left_index], list_characters[right_index] =
  list_characters[right_index], list_characters[left_index]

  left_index += 1
  right_index -= 1
