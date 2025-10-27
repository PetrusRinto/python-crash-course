# Patrick 27.10.2025.
# Nesting a list in a dictionary of favorite languages.

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    'dagny': [],
    }

# Show each person's favorite language.
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    elif len(languages) < 1:
        print(f"\n{name.title()} have not taken the poll.")
    elif len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")