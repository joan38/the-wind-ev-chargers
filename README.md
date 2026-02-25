# The Wind Electric Vehicle Chargers ⚡ Usage and Rules Study

We have 2 Tesla chargers (10kW max output) in the building open to all residents. Those 2 chargers are not enough given
the building is composed of 489 condo residences but this is better than nothing. So we need to maximize the utilization
of those chargers as well as making sure everyone has fair access to them.

## WhatsApp Group

We have a WhatsApp group for EV owners to coordinate charger usage. Members post "Freeing 1 charger" when they free up a
charger, so that others can use it ASAP. The goal of this group is to minimize the idle time of the chargers, maximize
usage of limited resources and make sure everyone gets a turn and no one is left unplugged 🚗🔌💚

This WhatsApp group contains 30 members at the time of this writing. Some might have 1 car for 2 members (husband and
wife) some might have 2 cars for 1 member? Or some might not even be in the group at all! We will assume N members = N
EV in the building.

There is a QR code on each charger that links to the WhatsApp group, so that anyone with an EV can participate in
maximizing the usage of the chargers.

The WhatsApp group changed a lot how we use those chargers, since it facilitated the access to them without the need to
repeatitively go downstairs phisically to check if they are free or not.
However, if an EV owner is not in the group, it put them at a significantly unfair disadvantage. As soon as a charger is
freed and annonced on the WhatsApp group, its members will be aware well before an outsider even gets a chance at
snatching it.
Even tho WhatsApp is free and accessible to all major platforms, we understand that some people might not be willing to
use it for whatever their reasons are: privacy concerns with a Meta owned app or phone number accessible to the members
of the group, technology barriere... But are open to suggestions to make sure everyone is included.

## Rules

In order to make sure everyone gets a turn, we have the following rules:

* A charge is limited to 3h usage. At which point the charger should be freed whether the car is charged or not.

These rules are set by the HOA and up for change anytime. But we, the members of the WhatsApp group, would like to
conduct a comprehensive study of the historical usage of the chargers to petition a change of the rules that is helping
its users and based on data rather than being arbitrary.

## Charging History Study

For this study, we will use the charging history CSVs pulled from the Tesla chargers:

* [Left charger](Previous%2012%20months%20charge%20sessions%20left%20charger.csv)
* [Right charger](Previous%2012%20months%20charge%20sessions%20right%20charger.csv)

We will be using only the last 30 days' data.

How many charging sessions happened?

**308 charging sessions** in the last 30 days (January 25 - February 24, 2026).

How many charging sessions went over 3h? What percentage of the total sessions?

**130 sessions (42.2%)** went over 3 hours.

How many charging sessions went over 4h? What percentage of the total sessions?

**51 sessions (16.6%)** went over 4 hours.

How many charging sessions went over 5h? What percentage of the total sessions?

**24 sessions (7.8%)** went over 5 hours.

Charging sessions start by hour of day:

```
00:00 [  6] ██████
01:00 [  6] ██████
02:00 [  6] ██████
03:00 [  2] ██
04:00 [  6] ██████
05:00 [  6] ██████
06:00 [ 10] ██████████
07:00 [  6] ██████
08:00 [ 25] █████████████████████████
09:00 [ 17] █████████████████
10:00 [ 12] ████████████
11:00 [ 19] ███████████████████
12:00 [ 16] ████████████████
13:00 [ 14] ██████████████
14:00 [ 16] ████████████████
15:00 [ 12] ████████████
16:00 [ 22] ██████████████████████
17:00 [ 19] ███████████████████
18:00 [ 17] █████████████████
19:00 [ 19] ███████████████████
20:00 [ 13] █████████████
21:00 [ 18] ██████████████████
22:00 [ 15] ███████████████
23:00 [  6] ██████
```

Charger occupancy by hour of day (active sessions):

```
00:00 [ 47] ███████████████████████████████████████████████
01:00 [ 36] ████████████████████████████████████
02:00 [ 29] █████████████████████████████
03:00 [ 26] ██████████████████████████
04:00 [ 28] ████████████████████████████
05:00 [ 31] ███████████████████████████████
06:00 [ 37] █████████████████████████████████████
07:00 [ 31] ███████████████████████████████
08:00 [ 48] ████████████████████████████████████████████████
09:00 [ 53] █████████████████████████████████████████████████████
10:00 [ 57] █████████████████████████████████████████████████████████
11:00 [ 61] █████████████████████████████████████████████████████████████
12:00 [ 61] █████████████████████████████████████████████████████████████
13:00 [ 51] ███████████████████████████████████████████████████
14:00 [ 54] ██████████████████████████████████████████████████████
15:00 [ 53] █████████████████████████████████████████████████████
16:00 [ 61] █████████████████████████████████████████████████████████████
17:00 [ 64] ████████████████████████████████████████████████████████████████
18:00 [ 66] ██████████████████████████████████████████████████████████████████
19:00 [ 68] ████████████████████████████████████████████████████████████████████
20:00 [ 61] █████████████████████████████████████████████████████████████
21:00 [ 66] ██████████████████████████████████████████████████████████████████
22:00 [ 59] ███████████████████████████████████████████████████████████
23:00 [ 48] ████████████████████████████████████████████████
```

Peak usage hours is between 8am and 11pm excluded.

How many charging sessions happened during peak usage hours only?

**262 charging sessions** during peak hours (8am–10pm).

How many charging sessions went over 3h during peak usage hours only? What percentage of the total peak usage sessions?

**104 sessions (39.7%)** went over 3 hours during peak hours.

How many charging sessions went over 4h during peak usage hours only? What percentage of the total peak usage sessions?

**34 sessions (13.0%)** went over 4 hours during peak hours.

How many charging sessions went over 5h during peak usage hours only? What percentage of the total peak usage sessions?

**18 sessions (6.9%)** went over 5 hours during peak hours.

Can you suggest potential changes to the rules that would make the chargers more available to more people while still
being fair and not too restrictive?
For example, would a 4h limit be better than a 3h limit? Or 2h limit?
Should we have a grace period overnight? Since people are not expected to wake up in the middle of the night.

## Claude Suggested Rule Changes:

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

After sharing the data study with the group, 9 members (out of 30) highlighted several key points:

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

The following EV owners of The Wind:

* Joan Goyeau (lead petitioner)
* Katerina Goyeau
* Sussi
* Andres
* Gabriela Pallares
* Brittany Nicole
* Tyler Eastridge
* Caro
* Maria Del Mar

Are requesting The Wind Management to consider the following changes to the EV charging rules based on the above data
study and group discussion:

* Revert to the 3 hours limit during peak hours (5am-10pm). Since 2h is too inconvenient and does not solve the root
  problem of enforcement.
* Remove the time limit for any cars plugged between 10pm and 5am. Since we don't expect people to wake up in the middle
  of the night to take a charger.
  This means: any cars plugged between 10pm and 5am will have to free the charger by 8am (3h after 5am). And any cars
  plugged before 10pm will need to free the charger by 1am (3h after 10pm) or before their 3h limit.
* Keep the 1 car per unit per day limit.
* Work on ways to enforce the rules for repeated offenders rather than making the rules stricter for everyone.
