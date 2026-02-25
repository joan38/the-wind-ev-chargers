# The Wind Electric Vehicle Chargers ⚡ Usage and Rules Study

We have 2 Tesla chargers (10kW max output) in the building open to all residents. Those 2 chargers are not enough given
that the building has 489 condo units, but this is better than nothing. So we need to maximize the utilization
of those chargers while ensuring everyone has fair access to them.

## WhatsApp Group

We have a WhatsApp group for EV owners to coordinate charger usage. Members post "Freeing 1 charger" when they free up a
charger, so that others can use it ASAP. The goal of this group is to minimize the idle time of the chargers, maximize
usage of limited resources and make sure everyone gets a turn and no one is left unplugged 🚗🔌💚

This WhatsApp group contains 30 members at the time of this writing. Some might have 1 car for 2 members (husband and
wife), some might have 2 cars for 1 member, or some might not even be in the group at all! We will assume N members = N
EVs in the building.

> [!TIP]
> There is a QR code on each charger that links to the WhatsApp group, so that anyone with an EV can participate in
> maximizing the usage of the chargers.

The WhatsApp group has greatly changed how we use those chargers, since it eliminated the need to
repeatedly go downstairs physically to check if they are free.
However, if an EV owner is not in the group, it puts them at a significant disadvantage. As soon as a charger is
freed and announced in the WhatsApp group, its members will be aware well before an outsider even gets a chance at
claiming it.
Even though WhatsApp is free and accessible on all major platforms, we understand that some people might not be willing to
use it for various reasons: privacy concerns with a Meta-owned app, not wanting their phone number accessible to group
members, technology barriers, etc. We are open to suggestions to make sure everyone is included.

## Rules

In order to make sure everyone gets a turn, we have the following rules:

* A charge is limited to 3h usage. At which point the charger should be freed whether the car is charged or not.

These rules are set by the HOA and subject to change at any time. We, the members of the WhatsApp group, would like to
conduct a comprehensive study of the historical charger usage to petition for a rules change that better serves
residents and is grounded in data rather than being arbitrary.

## Charging History Study

For this study, we will use the charging history CSVs pulled from the Tesla chargers:

* [Left charger](Previous%2012%20months%20charge%20sessions%20left%20charger.csv)
* [Right charger](Previous%2012%20months%20charge%20sessions%20right%20charger.csv)

We will be using only the last 30 days' data.

### How many charging sessions happened?

**308 charging sessions** in the last 30 days (January 25 - February 24, 2026).

### Charge duration distribution by 30-minute buckets:

```
0:00-0:30    [ 12] ████████████
0:30-1:00    [ 31] ███████████████████████████████
1:00-1:30    [ 20] ████████████████████
1:30-2:00    [ 32] ████████████████████████████████
2:00-2:30    [ 38] ██████████████████████████████████████
2:30-3:00    [ 45] █████████████████████████████████████████████
             ─────────── 3h limit ───────────
3:00-3:30    [ 56] ████████████████████████████████████████████████████████
3:30-4:00    [ 23] ███████████████████████
4:00-4:30    [ 18] ██████████████████
4:30-5:00    [  9] █████████
5:00-5:30    [  6] ██████
5:30-6:00    [ 11] ███████████
6:00-6:30    [  0]
6:30-7:00    [  1] █
7:00-7:30    [  1] █
7:30-8:00    [  2] ██
8:00-8:30    [  0]
8:30-9:00    [  1] █
9:00-9:30    [  0]
9:30-10:00   [  2] ██
```

### Charging sessions start graph by hour of day:

```
00:00-01:00 [  6] ██████
01:00-02:00 [  6] ██████
02:00-03:00 [  6] ██████
03:00-04:00 [  2] ██
04:00-05:00 [  6] ██████
05:00-06:00 [  6] ██████
06:00-07:00 [ 10] ██████████
07:00-08:00 [  6] ██████
08:00-09:00 [ 25] █████████████████████████
09:00-10:00 [ 17] █████████████████
10:00-11:00 [ 12] ████████████
11:00-12:00 [ 19] ███████████████████
12:00-13:00 [ 16] ████████████████
13:00-14:00 [ 14] ██████████████
14:00-15:00 [ 16] ████████████████
15:00-16:00 [ 12] ████████████
16:00-17:00 [ 22] ██████████████████████
17:00-18:00 [ 19] ███████████████████
18:00-19:00 [ 17] █████████████████
19:00-20:00 [ 19] ███████████████████
20:00-21:00 [ 13] █████████████
21:00-22:00 [ 18] ██████████████████
22:00-23:00 [ 15] ███████████████
23:00-00:00 [  6] ██████
```

### Charger occupancy graph by hour of day (active sessions):

```
00:00-01:00 [ 47] ███████████████████████████████████████████████
01:00-02:00 [ 36] ████████████████████████████████████
02:00-03:00 [ 29] █████████████████████████████
03:00-04:00 [ 26] ██████████████████████████
04:00-05:00 [ 28] ████████████████████████████
05:00-06:00 [ 31] ███████████████████████████████
06:00-07:00 [ 37] █████████████████████████████████████
07:00-08:00 [ 31] ███████████████████████████████
08:00-09:00 [ 48] ████████████████████████████████████████████████
09:00-10:00 [ 53] █████████████████████████████████████████████████████
10:00-11:00 [ 57] █████████████████████████████████████████████████████████
11:00-12:00 [ 61] █████████████████████████████████████████████████████████████
12:00-13:00 [ 61] █████████████████████████████████████████████████████████████
13:00-14:00 [ 51] ███████████████████████████████████████████████████
14:00-15:00 [ 54] ██████████████████████████████████████████████████████
15:00-16:00 [ 53] █████████████████████████████████████████████████████
16:00-17:00 [ 61] █████████████████████████████████████████████████████████████
17:00-18:00 [ 64] ████████████████████████████████████████████████████████████████
18:00-19:00 [ 66] ██████████████████████████████████████████████████████████████████
19:00-20:00 [ 68] ████████████████████████████████████████████████████████████████████
20:00-21:00 [ 61] █████████████████████████████████████████████████████████████
21:00-22:00 [ 66] ██████████████████████████████████████████████████████████████████
22:00-23:00 [ 59] ███████████████████████████████████████████████████████████
23:00-00:00 [ 48] ████████████████████████████████████████████████
```

> [!NOTE]
> Peak usage hours is between 8am and 1am (next day) excluded.

> [!IMPORTANT]
> For the rest of the study, we will count a charging session as "peak hour" only if it started between
> 8am and 10pm excluded (3h before 1am) or ended between 8am and 1am (next day) excluded.

### How many charging sessions happened during peak hours only?

**270 charging sessions** during peak hours.

### Charge duration distribution by 30-minute buckets, during peak hours only:

```
0:00-0:30    [ 12] ████████████
0:30-1:00    [ 29] █████████████████████████████
1:00-1:30    [ 17] █████████████████
1:30-2:00    [ 28] ████████████████████████████
2:00-2:30    [ 36] ████████████████████████████████████
2:30-3:00    [ 44] ████████████████████████████████████████████
             ─────────── 3h limit ───────────
3:00-3:30    [ 46] ██████████████████████████████████████████████
3:30-4:00    [ 23] ███████████████████████
4:00-4:30    [ 13] █████████████
4:30-5:00    [  6] ██████
5:00-5:30    [  4] ████
5:30-6:00    [  6] ██████
6:00-6:30    [  0]
6:30-7:00    [  1] █
7:00-7:30    [  1] █
7:30-8:00    [  1] █
8:00-8:30    [  0]
8:30-9:00    [  1] █
9:00-9:30    [  0]
9:30-10:00   [  2] ██
```

## Claude Suggested Rule Changes:

> Can you suggest potential changes to the rules that would make the chargers more available to more people while still
> being fair and not too restrictive?
> For example, would a 4h limit be better than a 3h limit? Or 2h limit?
> Should we have a grace period overnight? Since people are not expected to wake up in the middle of the night.

**Key Findings:**

- Average session duration: 2.77 hours (median: 2.80 hours)
- 42.2% of sessions exceed the current 3-hour limit
- Peak usage hours: 8am (busiest), followed by 4pm and late evening
- 17.2% of sessions start overnight (10pm-6am)

**Recommendations:**

1. **Keep the 3-hour base limit during peak hours (8am-10pm)** - The current rule is reasonable since the average
   session is 2.77 hours. The 42% exceeding 3 hours suggests some enforcement issues, but the limit itself is
   appropriate for daytime hours when demand is highest.

2. **Extend to 5 hours overnight (10pm-8am)** - Only 17% of sessions start overnight, and people shouldn't be expected
   to wake up at 1am to move their car. This gives more flexibility when demand is low (only 2-10 sessions per hour
   overnight vs 25 at peak). This would reduce rule violations while maintaining fairness.

3. **Consider a graduated system:**
    - **2-3 consecutive uses = lower priority** for the next 24 hours (honor system via WhatsApp)
    - This ensures heavy users don't monopolize the chargers while still allowing everyone regular access

4. **Add a "courtesy disconnect" reminder at 2.5 hours via the app** - Since the median session is 2.8 hours, most cars
   are nearly done by then. A gentle reminder could reduce the 42% violation rate.

**Why not 4 hours?** With 16.6% already exceeding 4 hours and 308 sessions across 2 chargers (5+ sessions per charger
per day), extending to 4 hours would reduce availability for the 30-member community. The current 3-hour limit is
data-justified.

**Why not 2 hours?** The median session is 2.8 hours, so a 2-hour limit would frustrate most users and create more
violations than it solves.

## WhatsApp Group Discussion Summary

After sharing the data study with the group, 8 members (out of 30) highlighted several key points:

**On the 3-hour limit:**

- The 42.2% overage rate was seen as an enforcement problem more than a rules problem, since many violations are likely
  only slightly over the limit (3:05, 3:10). The 16.6% exceeding 4 hours is the more meaningful indicator of true abuse.
- There is agreement that the current 3-hour limit is reasonable in principle, and that reducing to 2 hours would be
  counterproductive — if people aren't following 3 hours, they won't follow 2 hours either.

**On overnight sessions:**

- Suggestion to simply remove the limit for cars plugged in after 12am, with a hard requirement to be unplugged by 8am,
  rather than a 5-hour window.

**On enforcement — the core problem:**

- Fines do not work. One resident (known Cybertruck owner with 3 cars) has been fined 40+ times and simply pays them, as
  management acknowledged.
- Management is reluctant to escalate, citing fear of legal action from this specific resident.
- The group strongly believes that **revoking charging privileges** and/or **booting/towing** after repeated
  violations (3–4 offenses) would be far more effective than financial penalties — the inconvenience matters more than
  the cost.
- Precedent exists: management already revokes access to other amenities for repeated abuse. Charging should be no
  different.

**On data-driven enforcement:**

- Suggestion to pull usage data regularly and provide it to management so they can cross-reference camera footage with
  license plates to identify repeat offenders.

## Conclusion

After conducting a poll in the WhatsApp group on the following proposed rule changes:
In favor:
Against:
Abstain:

The "In favor" EV owners of The Wind, are requesting The Wind Management to consider the following changes to the EV
charging rules based on the above data study and group discussion:

* Revert to the 3-hour limit during peak hours (5am–10pm), as a 2-hour limit is too inconvenient and does not solve the
  root problem of enforcement.
* Remove the time limit for any cars plugged in between 10pm and 5am, since we cannot expect people to wake up in the
  middle of the night to free a charger.
  This means: any car plugged in between 10pm and 5am must free the charger by 8am (3 hours after 5am), and any car
  plugged in before 10pm must free the charger by 1am (3 hours after 10pm) or when their 3-hour limit expires, whichever
  comes first.
* Keep the 1 car per unit per day limit.
* Work on ways to enforce the rules for repeated offenders rather than making the rules stricter for everyone.

- The Wind EV Owners Group led by Joan Goyeau
