unconfirmed_users = ['george', 'greg', 'john']
confirmed_users = []

while(unconfirmed_users):
    current_users = unconfirmed_users.pop()
    print("Verifying: " + current_users)

    confirmed_users.append(current_users)

print("\nVerified users:")

for verified in confirmed_users:
    print(verified)