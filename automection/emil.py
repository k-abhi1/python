def generate_permutations(username, domain, current="", index=0, count=[0], max_permutations=1000):
    # If reached the end of username or maximum permutations, print the current combination with domain appended
    if index == len(username):
        if count[0] < max_permutations:
            print(current + "@" + domain)
            count[0] += 1
        return

    # If max_permutations is reached, stop further recursion
    if count[0] >= max_permutations:
        return

    # Include current character without a dot
    generate_permutations(username, domain, current + username[index], index + 1, count, max_permutations)

    # Include current character with a dot, if it's not the last character
    if index < len(username) - 1:
        generate_permutations(username, domain, current + username[index] + ".", index + 1, count, max_permutations)

# Main
email="nischalchandraprakash47568@gmail.com"
username, domain = email.split("@")
generate_permutations(username, domain)