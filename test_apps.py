from tuesday.commands import apps
import time

print("Testing open_app logic...")
# 1. Known App
print("1. Testing Known App (notepad)...")
apps.open_app("open notepad")
time.sleep(1)

# 2. Executable
print("2. Testing Executable (calc.exe)...")
apps.open_app("calc.exe")
time.sleep(1)

# 3. Protocol
print("3. Testing Protocol (calculator:)...")
apps.open_app("calculator:") # Windows Calculator protocol
time.sleep(1)

# 4. Search
print("4. Testing Search (mspaint)...")
apps.open_app("mspaint")
time.sleep(1)

print("Tests initiated.")
