def make_abc():
    result = ["a", "b", "c"]
    return result

print("Demonstrate make_abc:")
print(make_abc())

def equal_edges(items):
    first = items[0]
    last = items[-1]
    if first == last:
     return True
    else:
        return False

print("Demonstrate equal_edges")
print("[1, 2, 3, 11] -> ", equal_edges([1, 2, 3, 11]))
print("[1, 2, 3, 1] -> ", equal_edges([1, 2, 3, 1]))

def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[2]
    last2 = list2[2]

    if first1 == first2 or first1 == last2 or last1 == first2 or last1 == last2:
        return True
    else: 
        return False

print("Demonstrate common_edge")
print("[1, 2, 4] & [3, 2, 1] -> ", common_edge([1, 2, 4], [3, 2, 1]))
print("[1, 2, 4, 5] & [2, 3, 2, 4] -> ", common_edge([1, 2, 4, 5], [2, 3, 2, 4]))

def all_the_same(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    if first == middle == last:
        return True
    else:
        return False
    
print("Demonstrate all_the_same")
print("[1, 2, 3] -> ", all_the_same([1, 2, 3]))
print("[3, 3, 3] -> ", all_the_same([3, 3, 3]))

def all_unique(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    if first == middle or middle == last or first == last:
        return False
    else:
        return True
    
print("Demonstrate all_unique")
print("[1, 2, 3] -> ", all_unique([1, 2, 3]))
print("[2, 3, 3] -> ", all_unique([2, 3, 3]))

def increasing(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    if first < middle and middle < last:
        return True
    else:
        return False
    
print("Demonstrate increasing")
print("[1, 2, 3] -> ", increasing([1, 2, 3]))
print("[6, 4, 5] -> ", increasing([6, 4, 5]))

def all_true(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    if first == middle == last == True:
        if first == True:
            return True
    else:
        return False
    
print("Demonstrate all_true")
print("[True, True, True] -> ", all_true([True, True, True]))
print("[True, False, True] -> ", all_true([True, False, True]))

def mostly_true(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
    counter = int(0)
    if first == True:
        counter = counter + 1
    if middle == True:
        counter = counter + 1
    if last == True:
        counter = counter + 1
    if counter >= 2:
        return True
    else:
        return False

    
print("Demonstrate mostly_true")
print("[False, False, True] -> ", mostly_true([False, False, True]))
print("[True, False, True] -> ", mostly_true([True, False, True]))

def make_copy(list1):
    original_list = list1
    new_list = list1
    return new_list

print("Demonstrate make_copy")
print("[1, 2, 1, 2] -> ", make_copy([1, 2, 1, 2]))
print("[1, 2, 4] -> ", make_copy([1, 2, 4]))

def repeat_thrice(number):
    return [number, number, number]

print("Demonstrate repeat_thrice")
print("1 -> ", repeat_thrice(1))
print("2 -> ", repeat_thrice(2))

def make_reversed_copy(list1):
    first = list1[0]
    second = list1[1]
    last = list1[2]
    return [last, second, first]

print("Demonstrate make_reversed_copy")
print("[1, 7, 6] -> ", make_reversed_copy([1, 7, 6]))
print("[4, 8, 9] -> ", make_reversed_copy([4, 8, 9]))

def reverse_in_place(list1):
    first = list1[0]
    second = list1[1]
    last = list1[2]
    list1 = [last, second, first]
    return list1

print("Demonstrate reverse_in_place")
print("[1, 7, 6] -> ", reverse_in_place([1, 7, 6]))
print("[4, 8, 9] -> ", reverse_in_place([4, 8, 9]))
