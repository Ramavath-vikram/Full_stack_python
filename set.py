#Python set is an unordered collection of multiple items having different datatypes. 
# In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.



# Create a set
fruits = {"apple", "banana", "cherry", "orange"}

# Add an element to the set
fruits.add("kiwi")

# Remove an element from the set
fruits.remove("banana")

# Check if an element exists in the set
if "apple" in fruits:
    print("Apple is in the set")

# Display the set
print(fruits)

#operation in sets
#union  In Python, you can perform a union operation on sets to combine elements from multiple sets. The union() method or the | operator can be used to merge two or more sets, while automatically removing any duplicate elements.


set1={1,2,3,4,5} #int
set2={"a","b","c","d","e"} #string
set3={1.1,3.14,7.5,6.66,8.9} #float
set4={1,"apple",3.14,55} #mixed

# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union using the union() method
union_set = set1.union(set2)
print("Union using union() method:", union_set)

# Union using the | operator
union_set_operator = set1 | set2
print("Union using | operator:", union_set_operator)

# Create three sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# Union of all three sets
union_all = set1 | set2 | set3
print("Union of all three sets:", union_all)


#intersection    In Python, the intersection of two sets refers to the elements that are common to both sets. You can perform this operation using the intersection() method or the & operator.


# Intersection using the intersection() method
intersection_set = set1.intersection(set2)
print("Intersection using intersection() method:", intersection_set)

# Intersection using the & operator
intersection_set_operator = set1 & set2
print("Intersection using & operator:", intersection_set_operator)

# Create three sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set3 = {4, 6}

# Intersection of all three sets
intersection_all = set1 & set2 & set3
print("Intersection of all three sets:", intersection_all)

#difference method In Python, the difference method allows you to find the elements that are in one set but not in another. You can use the difference() method or the - operator to perform this operation.

# Difference using the difference() method
difference_set = set1.difference(set2)
print("Difference using difference() method:", difference_set)

# Difference using the - operator
difference_set_operator = set1 - set2
print("Difference using - operator:", difference_set_operator)

# Create two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Difference (elements in set1 but not in set2)
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)


#The symmetric difference between two sets refers to the elements that are in either of the sets, but not in both. This can be achieved using the symmetric_difference() method or the ^ operator in Python.
# Symmetric Difference using the symmetric_difference() method
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference using symmetric_difference() method:", sym_diff_set)

# Symmetric Difference using the ^ operator
sym_diff_set_operator = set1 ^ set2
print("Symmetric Difference using ^ operator:", sym_diff_set_operator)
