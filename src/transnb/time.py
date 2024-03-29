"""
We want the toots to be posted at random time intervals
This module decides whether to post a toot
To run this analysis from root dir:
python src/transnb/time.py
"""
import datetime as dt
import secrets
from statistics import mean

from croniter import croniter

from transnb import messages

CRON_MINUTES_INTERVAL = 7  # every 7 minutes
DESIRED_TOOTS_PER_DAY = 7


def do_i_post_a_toot() -> bool:
    """
    7 minutes occurs 216 times per day
    desired toots per day is 7
    """
    probability = DESIRED_TOOTS_PER_DAY / 216  # 0.32 ish
    if secrets.randbelow(10000) / 10000 <= probability:
        return True
    return False


def analyse():
    # assuming no duplicates, how long would it take to toot everything?
    # obviously there are gonna be duplicates but this is a nice indication
    days_to_cycle_all = int(round(len(messages.get_all_messages()) / DESIRED_TOOTS_PER_DAY, 0))
    days_to_cycle_noadj = days_to_cycle_all

    # let's simulate that time period (plus a day for good measure)
    days_to_cycle_all += 1
    start_dt = dt.datetime(2020, 1, 1, 0, 0)
    end_dt = start_dt + dt.timedelta(days=days_to_cycle_all)
    cron_expr = f"*/{CRON_MINUTES_INTERVAL} * * * *"
    iter = croniter(cron_expr, start_dt)
    cron_dt = start_dt
    results = []
    while cron_dt < end_dt:
        cron_dt = iter.get_next(dt.datetime)
        results.append([cron_dt, do_i_post_a_toot()])
        # print(f"{cron_dt}  post_toot: {do_i_post_a_toot()}")

    # how many toots per day? 7ish is the goal (ballpark)
    toot_count = {}
    toots_per_day = {}
    for n in range(days_to_cycle_all):
        current_dt = (start_dt + dt.timedelta(n)).date()
        current_dt_str = current_dt.strftime("%Y-%m-%d")
        toots_per_day[current_dt_str] = sum([1 for x in results if x[0].date() == current_dt and x[1] is True])
        for i in range(0, toots_per_day[current_dt_str]):
            msg = messages.get_random_message()
            if msg in toot_count:
                toot_count[msg] += 1
            else:
                toot_count[msg] = 1

    # pp(toots_per_day)
    print(f"toots_per_day: {round(mean([v for v in toots_per_day.values()]),2)}")
    print(f"max toots/day: {max([v for v in toots_per_day.values()])}")
    print(f"min toots/day: {min([v for v in toots_per_day.values()])}")
    dupe_factor = round(mean([x for x in toot_count.values()]), 2)
    print(f"assuming no duplicates, all toots will be gone in {days_to_cycle_noadj} days")
    print(f"duplication factor: {dupe_factor}")
    print(f"accounting for duplicates, all toots will be gone in {days_to_cycle_all * dupe_factor} days")


if __name__ == "__main__":
    analyse()
