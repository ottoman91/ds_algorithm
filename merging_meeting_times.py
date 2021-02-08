# sort the tuples by the start time of meetings
# between subsequent tuples, if the end time of the first meeting is greater than
# or equal to the start time of the second meeting, then, merge the two tuples.
#else, append the tuple

def merge_ranges(meeting_times):

  #sort the meeting time tuples
  sorted_meeting_times = sort(meeting_times)

  #declare the resultant tuple, called merged_tuples, with the first meeting
  merged_tuples = [sorted_meeting_times[0]]

  for current_start_time, current_end_time in sorted_meeting_times[1:]:
    last_meeting_start_time, last_meeting_end_time = merged_tuples[-1]
    if(current_start_time <= last_meeting_end_time):
      merged_tuples[-1] = (last_meeting_start_time,
                            max(current_end_time, last_meeting_end_time))
    else:
      merged_tuples.append(current_start_time, current_end_time)
