# Patrick 17.10.2025.
# 6-3 Glossary / 6-4 Glossary 2.

glossaries = {
    'slicing': 'A process of taking out portions of a list, tuple or string.',
    'tuple': 'An unmodifiable list.',
    'list': 'Stores data seperated with commas, inside brackets.',
    'built-in function': 'Performs one dedicated task.',
    'float': 'Numbers with decimals.',
    'sorting': 'Sorting in alphabetical order and more. Permanent or not.',
    'variable': 'Something defined with a name and contains data.',
    'range': 'Range has 3 main values: start, end and step.',
    'comment': 'Comments are used to explain code or make it more readable.',
    'for loop': '"loops" for each item in lists, tuples and more.',
    }

# Looping through the dictionary.
for glossary, meaning in glossaries.items():
    print(f"\n{glossary.title()}:")
    print(f"{meaning}")