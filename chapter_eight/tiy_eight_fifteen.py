# Patrick 12.11.2025.
# 8-15 Printing Models.

from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

unprinted_designs = ['laptop stand', 'charging dock', 'badge']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)