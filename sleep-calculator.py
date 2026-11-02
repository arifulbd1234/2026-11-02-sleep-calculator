# Day 27 (2026-11-02): Sleep Cycle Calculator
# What it does: calculates ideal bedtimes and wake-up times based on the
# natural 90-minute sleep cycle, so you wake up feeling fresh instead of
# groggy. Useful for anyone who wants better sleep without an app.
# No external libraries needed - plain Python only.

MINUTES_PER_CYCLE = 90   # one full sleep cycle is about 90 minutes
FALL_ASLEEP_MINUTES = 15  # average time it takes to fall asleep


def _minutes_to_clock(total_minutes):
    """Convert minutes since midnight to a 'HH:MM' 24-hour clock string."""
    total_minutes %= 24 * 60
    return "{:02d}:{:02d}".format(total_minutes // 60, total_minutes % 60)


def bedtimes_for_wake(wake_hour, wake_minute=0, cycles=(4, 5, 6)):
    """Return the best times to go to bed if you must wake up at a given time.

    Gives one bedtime per sleep cycle count (default: 4, 5 or 6 full cycles),
    already counting 15 minutes to fall asleep.
    """
    wake = wake_hour * 60 + wake_minute
    results = []
    for n in cycles:
        bedtime = wake - (n * MINUTES_PER_CYCLE + FALL_ASLEEP_MINUTES)
        results.append((n, _minutes_to_clock(bedtime)))
    return results


def wake_times_for_bed(bed_hour, bed_minute=0, cycles=(4, 5, 6)):
    """Return the best times to wake up if you go to bed at a given time.

    Gives one wake-up time per sleep cycle count (default: 4, 5 or 6 cycles),
    already counting 15 minutes to fall asleep.
    """
    bed = bed_hour * 60 + bed_minute + FALL_ASLEEP_MINUTES
    results = []
    for n in cycles:
        wake = bed + n * MINUTES_PER_CYCLE
        results.append((n, _minutes_to_clock(wake)))
    return results


def sleep_hours(bed_hour, bed_minute, wake_hour, wake_minute):
    """Return how many hours of sleep you get between a bedtime and a wake time."""
    bed = bed_hour * 60 + bed_minute
    wake = wake_hour * 60 + wake_minute
    slept = (wake - bed) % (24 * 60)
    return round(slept / 60, 2)


if __name__ == "__main__":
    # Example 1: I must wake up at 6:30 AM for work - when should I sleep?
    print("You must wake up at 06:30. Best bedtimes:")
    for cycles, time in bedtimes_for_wake(6, 30):
        print("  {} full cycles -> sleep at {}".format(cycles, time))

    # Example 2: I am going to bed now at 11:15 PM - when should I wake up?
    print("\nYou sleep at 23:15. Best wake-up times:")
    for cycles, time in wake_times_for_bed(23, 15):
        print("  {} full cycles -> wake at {}".format(cycles, time))

    # Example 3: How much sleep do I get from 11:45 PM to 6:00 AM?
    print("\nSleep from 23:45 to 06:00: {} hours".format(
        sleep_hours(23, 45, 6, 0)))
