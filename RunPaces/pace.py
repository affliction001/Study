import math

distance = float(input("Distanse: "))
start_pace = 4  # 3:00 min/km
current_pace = start_pace
end_pace = 5  # 5:00 min/km
step = 0
step_counter = 5  # 10 seconds


def get_pace(current_step):
    return round(current_step / 60, 2)


while current_pace < end_pace:
    current_pace = start_pace + get_pace(step)
    speed = 60 / current_pace
    time = round(distance / speed * 60)

    pace = str(start_pace + (math.floor(step / 60)))
    pace_fraction = str(step % 60)
    if len(pace_fraction) == 1:
        pace_fraction = "0" + pace_fraction
    pace = pace + ":" + pace_fraction

    fraction = time % 60
    if len(str(fraction)) == 1:
        fraction = "0" + str(fraction)

    step += step_counter

    print(pace, " min/km = ", math.floor(time / 60), ":", fraction, sep="")
