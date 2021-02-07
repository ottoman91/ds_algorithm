def square_list_in_place(int_list):
  for index, element in enumerate(int_list):
    int_list[index] *= element


def square_list_out_of_place(int_list):
  squared_list = [None] * len(int_list)

  for index, element in enumerate(int_list):
    squared_list[index] = element ** 2


  return squared_list
