from datetime import datetime
import random

# Open log.txt to append a contribution entry
with open("log.txt", "a") as file:
    # 20% chance to skip contributions on some days
    if random.random() < 0.2:
        print("No contributions today!")
    else:
        # Write just one contribution
        file.write(f"New Contribution on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("1 contribution made today!")
