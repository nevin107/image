inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Add a key 'pocket' with a list as its value
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sort the items in the list under the 'backpack' key
inventory['backpack'].sort()

# Remove 'dagger' from the list under the 'backpack' key
inventory['backpack'].remove('dagger')

# Add 50 to the value stored under the 'gold' key
inventory['gold'] += 50

# Print the updated inventory
print("Updated Inventory:")
for key, value in inventory.items():
    print(key, ":", value)
