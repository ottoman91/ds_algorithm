def reverse_words(message):
  reverse_characters(message)

  starting_index = 0
  for i in xrange(len(message) + 1):
    if(i == len(message)) or (message[i] == ' '):
      reverse_characters(message, starting_index, i - 1)
      starting_index = i + 1

def reverse_characters(message, start_index, end_index):
  while start_index < end_index:
    message[start_index], message[end_index] = \
    message[end_index], message[start_index]

  start_index += 1
  end_index -= 1
