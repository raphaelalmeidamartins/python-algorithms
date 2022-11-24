def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    students_counter = 0

    for entrance_time, exit_time in permanence_period:
        if type(entrance_time) is not int or type(exit_time) is not int:
            return None

        elif entrance_time <= target_time <= exit_time:
            students_counter += 1

    return students_counter
