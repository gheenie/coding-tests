def minTime(start, end, q_start, q_end, k):
    student_timings = []

    for i in range(len(start)):
        student_timings.append(range(start[i], end[i] + 1))
    
    query_timings = []

    for i in range(len(q_start)):
        query_timings.append(range(q_start[i], q_end[i] + 1))

    counts = []

    for query in query_timings:
        count = 0

        for query_instance in query:
            students = 0

            for student_timing in student_timings:
                if query_instance in student_timing:
                    students += 1

            if students >= k:
                count += 1

        counts.append(count)
    
    return counts

print(minTime([1, 2, 4], [3, 4, 5], [2], [6], 2))
print(minTime([1, 2, 4], [4, 5, 5], [2, 5], [6, 6], 3))
