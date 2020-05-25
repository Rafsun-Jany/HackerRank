def total_fine(returned_time,expected_time):
    fine = 0
    day_returned = returned_time[0]
    month_returned = returned_time[1]
    year_returned = returned_time[2]

    day_expected = expected_time[0]
    month_expected = expected_time[1]
    year_expected = expected_time[2]

    if year_returned==year_expected:
        if month_returned == month_expected:
            if day_returned == day_expected:
                fine = 0
                return fine
            else:
                    if day_returned > day_expected:
                        fine = 15 * (day_returned-day_expected)
                        return fine
                    else:
                        fine = 0
                        return fine
        else:
            if month_returned > month_expected:
                fine = 500 * (month_returned-month_expected)
                return fine
            else:
                if day_returned == day_expected:
                    pass
                else:
                    if day_returned > day_expected:
                        fine = 15 * (day_returned-day_expected)
                        return fine
                    else:
                        fine = 0
                        return fine
    else:
        if year_returned > year_expected:
            fine = 10000
            return fine
        else:
            fine = 0
            return fine


if __name__=='__main__':

    returned_time = list(map(int,input().split()))

    expected_time = list(map(int,input().split()))

    result = total_fine(returned_time,expected_time)
    print(result)
