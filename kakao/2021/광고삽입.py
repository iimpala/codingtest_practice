def solution(play_time, adv_time, logs):
    play_second = to_second(play_time)
    adv_second = to_second(adv_time)

    ps = [0 for _ in range(play_second + 1)]
    for log in logs:
        watch = log.split("-")
        start, end = map(to_second, watch)
        ps[start] += 1
        ps[end] -= 1

    for i in range(1, len(ps)):
        ps[i] += ps[i - 1]

    watch = [sum(ps[:adv_second])]
    for i in range(1, play_second - adv_second + 1):
        watch.append(watch[i - 1] - ps[i - 1] + ps[i + (adv_second-1)])

    print(watch)
    result = watch.index(max(watch))
    return to_time(result)


def to_second(time):
    h, m, s = map(int, time.split(":"))
    return 3600 * h + 60 * m + s


def to_time(second):
    h = second // 3600
    m = (second - 3600 * h) // 60
    s = second - 3600 * h - 60 * m
    return f'{h:0>2}:{m:0>2}:{s:0>2}'
