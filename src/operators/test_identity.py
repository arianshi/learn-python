"""Identity operators

@see: https://www.w3schools.com/python/python_operators.asp

Identity operators are used to compare the objects, not if they are equal, 
but if they are actuallythe same object, with the same memory location.
"""


def test_identity_operators():
    """Identity operators"""

    # Let's illustrate identity operators based on the following lists.
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # Returns true if both variables are the same object.

    # Example:
    # first_fruits_list and third_fruits_list are the same objects.
    print(first_fruits_list is third_fruits_list)       # True
    assert first_fruits_list is third_fruits_list

    print(first_fruits_list is second_fruits_list)      # False

    # is not
    # Returns true if both variables are not the same object.

    # Example:
    # first_fruits_list and second_fruits_list are not the same objects, even if they have
    # the same content
    print(first_fruits_list is not second_fruits_list)  # True
    assert first_fruits_list is not second_fruits_list

    # "is" checks same memory location (identity); "==" checks same value (equality).
    # second_fruits_list has the same content but is a different object in memory.
    print(first_fruits_list is second_fruits_list)      # False  (different objects)
    print(first_fruits_list == second_fruits_list)      # True   (same content)
    assert first_fruits_list is not second_fruits_list
    assert first_fruits_list == second_fruits_list
