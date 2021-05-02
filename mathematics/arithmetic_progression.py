"""
average of given terms = sum of all terms / number of terms;

sum of all terms = average of given terms * number of terms;

if terms are evenly spaced, (e.g. 2, 4, 6, 8...), then
    sum of all terms = average of evenly spaced terms * number of terms;

average of evenly spaced terms = sum(first + last term) / 2

    sum of all terms = sum(first + last term) / 2 * number of terms;

General formula:
    sum = average * number of terms

"""

def sum_of_evenly_spaced_terms(terms):
    # sum = average * number of terms

    number_of_terms = len(terms)
    average = ((terms[0] + terms[number_of_terms - 1]) / 2) * number_of_terms
    return average

print(sum_of_evenly_spaced_terms([2, 4, 6, 8]))
    