import random

def generate_indian_girls_names(count):
    # List of popular Indian girls' names
    names = [
        "Aaradhya", "Aarya", "Aditi", "Ananya", "Anika", "Anjali", "Aparna", "Bhavna", 
        "Charvi", "Diya", "Esha", "Gauri", "Ishita", "Jhanvi", "Kavya", "Lata", "Meera", 
        "Neha", "Nikita", "Pari", "Priya", "Rhea", "Saanvi", "Sakshi", "Shruti", 
        "Tara", "Uma", "Vani", "Vidya", "Yamini", "Zara", "Ragini", "Simran", "Pooja",
        "Nandini", "Kiran", "Radhika", "Swara", "Tanvi", "Veena", "Lakshmi", "Radha",
        "Sita", "Chitra", "Devika", "Rekha", "Malini", "Madhavi", "Harini", "Ira",
        # Add more names as desired
    ]

    generated_names = [random.choice(names) for _ in range(count)]
    return generated_names

# Generate 1000 random Indian girls' names
indian_girls_names = generate_indian_girls_names(100)

# Print the generated names
for name in indian_girls_names:
    print(name)
