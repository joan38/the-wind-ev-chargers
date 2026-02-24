#!/usr/bin/env python3
import csv
from datetime import datetime, timedelta
from collections import defaultdict

# Read both CSV files
left_sessions = []
right_sessions = []

with open('Previous 12 months charge sessions left charger.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        left_sessions.append(row)

with open('Previous 12 months charge sessions right charger.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        right_sessions.append(row)

# Combine all sessions
all_sessions = left_sessions + right_sessions

# Filter to last 30 days (from 2026-02-24)
from datetime import timezone
end_date = datetime(2026, 2, 24, 23, 59, 59, tzinfo=timezone(timedelta(hours=-5)))
start_date = end_date - timedelta(days=30)

filtered_sessions = []
for session in all_sessions:
    # Parse the datetime
    start_time_str = session['Charging Start Time']
    start_time = datetime.fromisoformat(start_time_str)

    if start_date <= start_time <= end_date:
        filtered_sessions.append({
            'start_time': start_time,
            'duration_minutes': float(session['Charging Duration (minutes)']),
            'energy_kwh': float(session['Energy Delivered (kWh)'])
        })

# Sort by start time
filtered_sessions.sort(key=lambda x: x['start_time'])

# Question 1: How many charging sessions happened?
total_sessions = len(filtered_sessions)
print(f"Total charging sessions in last 30 days: {total_sessions}")
print()

# Questions 2-4: Sessions over 3h, 4h, 5h
sessions_over_3h = [s for s in filtered_sessions if s['duration_minutes'] > 180]
sessions_over_4h = [s for s in filtered_sessions if s['duration_minutes'] > 240]
sessions_over_5h = [s for s in filtered_sessions if s['duration_minutes'] > 300]

print(f"Sessions over 3h: {len(sessions_over_3h)} ({len(sessions_over_3h)/total_sessions*100:.1f}%)")
print(f"Sessions over 4h: {len(sessions_over_4h)} ({len(sessions_over_4h)/total_sessions*100:.1f}%)")
print(f"Sessions over 5h: {len(sessions_over_5h)} ({len(sessions_over_5h)/total_sessions*100:.1f}%)")
print()

# Question 5: ASCII graph by hour of day
hour_counts = defaultdict(int)
for session in filtered_sessions:
    hour = session['start_time'].hour
    hour_counts[hour] += 1

# Find max for scaling
max_count = max(hour_counts.values()) if hour_counts else 1

print("Charging sessions by hour of day:")
for hour in range(24):
    count = hour_counts[hour]
    bar_length = int((count / max_count) * 10)
    bar = '█' * bar_length
    print(f"{hour:02d}:00 [{count:3d}] {bar}")
print()

# Question 6: Cost calculation
total_energy_kwh = sum(s['energy_kwh'] for s in filtered_sessions)
cost_per_kwh = 0.14
total_cost = total_energy_kwh * cost_per_kwh

print(f"Total energy delivered: {total_energy_kwh:.1f} kWh")
print(f"Total cost at $0.14/kWh: ${total_cost:.2f}")
print()

# Additional statistics for suggestions
avg_duration = sum(s['duration_minutes'] for s in filtered_sessions) / total_sessions
median_duration = sorted([s['duration_minutes'] for s in filtered_sessions])[total_sessions // 2]

print(f"Average session duration: {avg_duration:.1f} minutes ({avg_duration/60:.2f} hours)")
print(f"Median session duration: {median_duration:.1f} minutes ({median_duration/60:.2f} hours)")
print()

# Overnight sessions (10pm to 6am)
overnight_sessions = [s for s in filtered_sessions if s['start_time'].hour >= 22 or s['start_time'].hour < 6]
print(f"Overnight sessions (10pm-6am): {len(overnight_sessions)} ({len(overnight_sessions)/total_sessions*100:.1f}%)")