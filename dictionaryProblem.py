semesterLectures = {'January':[5, 6, 5, 4, 5],
                    'February': [4, 5, 6, 5],
                    'March': [3, 4, 6, 4, 6],
                    'April':[2, 1, 5, 3],
                    'May':[5, 1, 6]
                    }

def totalAttendance(semLectures):
    finalSum = 0
    for keys in semesterLectures.keys():
        finalSum += sum(semesterLectures[keys])
    return finalSum

print('Total Attendances of this semester is',totalAttendance(semesterLectures))