# Patrick 22.09.2025
# A program that lists countries I want to visit and not

# A regular list of three countries (it will increase).
countries = ['thailand', 'zanzibar', 'france']

# a message that prints the list:
print('This is the original list.') # Patrick 23.09.2025
print(f'Original: {countries}')

# Alphabetical order, but not permanent
print(f'\nSorted in alphabetical order, but not permanent.') # Patrick 23.09.2025
print(f'Sorted: {sorted(countries)}')

# Proving the change was temporary
print(f'\nThe original again to prove the temporary change.') # Patrick 23.09.2025
print(f'Original: {countries}')

# Sorting in alphabetical, but reversed
print(f'\nSorted in reverse-alphabetical order.') # Patrick 23.09.2025
print(f'Reversed alphabetically:{sorted(countries, reverse=True)}')

# Proving the temporary change by outputting the original
print(f'\nProving the temporary change.') # Patrick 23.09.2025
print(f'Original: {countries}')

# Using variables to sort diferentally and permanentally
print(f'\nCreating a variable to permanentally reverse the order.') # Patrick 23.09.2025
countries.reverse()
print(f'Reversed original: {countries}')

# Reverse again outputs the original format
print(f'\nTo revert back to the original we have to revere it again.') # Patrick 23.09.2025
countries.reverse()
print(f'Original: {countries}')

# Patrick 23.09.2025
# Permanently sorting in reversed-alphabetical order
print(f'\nPermanently changed the order in reversed-alphabetical order with a variable.')
countries.sort(reverse = True)
print(f'Reversed alphabetically: {countries}')

# Let us test adding a new country to the list and see how the code reacts
countries.append('japan')
print(f'\nAdded Japan to the list to check if the order changed.')
print(f'New list: {countries}') # Proved the sorting is not dynamic.

# Let's sort it in alphabetical order.
print(f'\nSorting the new list alphabetically.')
countries.sort()
print(f'Alphabetical order: {countries}')

# Using integer to identify my favorite country out of the current list. Using 'title' to capitalize.
print(f'\nCreating a variable to output my favorite country based on the current list using index.')
most_fav_int = countries[1]
print(f'Index 1 should be Japan, my favorite is: {most_fav_int.title()}!')

# Popping out and displaying my least favourite based on the current list.
print(f"\nCreating a 'pop' variable to output my least favorite in the current list.")
print(f'- Current list: {countries}')

least_fav_int = countries.pop(0)

print(f'- My least favorite country out of the list is: {least_fav_int.title()}')
print(f'\nFrance is therefore removed from the list.')
print(f'List without {least_fav_int}:')
print(f'{countries}')

# Adding China between Japan and Thailand
print(f'\nI want to add China between Japan and Thailand.')
countries.insert(1, 'china')
print(f'China added:')
print(f'{countries}')

# Removing Thailand with 'del' and adding South-Korea with 'insert'
print(f'\nRemoving {countries[2]} from the list.')
del(countries[2])
countries.insert(2,'south-korea')
print(f'Adding {countries[2]} to the list.')
print(f'- New list: {countries}')

# Removing zanzibar from the list so that there is only Asian countries left
print(f'\nRemoving {countries[-1].title()} from the list.')
countries.remove('zanzibar')
print(f'\nAsian countries only:\n{countries}')

# Sorting alphabetically again.
countries.sort()
print(f'\nSorted:\n{countries}')