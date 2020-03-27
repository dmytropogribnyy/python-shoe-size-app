"""Create shoe size conversion from US to EU"""
# todo: 1. Create list of numbers with step 0.5 to get men`s shoe size chart:
import numpy as np
women_list1 = np.arange(4, 12.5, 0.5).tolist()
# => [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0]

men_list1 = np.arange(6, 12.5, 0.5).tolist()
# => [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5,
# 11.0, 11.5, 12.0]

# todo: 2. Create new list with floats .0 (for ex. 5.0) changed to integers:
women_list2 = []
for size in women_list1:
    if size % 1 == 0:
        women_list2.append(int(size))
    else:
        women_list2.append(size)
# => [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10,
# 10.5, 11, 11.5, 12]

men_list2 = []
for size in men_list1:
    if size % 1 == 0:
        men_list2.append(int(size))
    else:
        men_list2.append(size)
# => [6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5,
# 12]

# todo: 3. initialize a dictionary with only keys from a list:
# create dictionary with US men`s shoe sizes
women_chart = dict.fromkeys(women_list2)
# => {4: None, 4.5: None, 5: None, 5.5: None, 6: None, 6.5: None, 7: None, 7.5: None, 8: None, 8.5: None, 9: None, 9.5: None, 10: None, 10.5: None, 11: None, 11.5: None, 12: None}

# create dictionary with US men`s shoe sizes
men_chart = dict.fromkeys(men_list2)
# => {6: None, 6.5: None, 7: None, 7.5: None, 8: None, 8.5: None, 9: None, 9.5: None, 10: None, 10.5: None, 11: None, 11.5: None, 12: None}

# todo: add EU shoe sizes as values:
# Reference to shoe size chart: https://www.shoesizingcharts.com/

women_chart.update({4: "35", 4.5: "35", 5: "35-36", 5.5: "36", 6: "36-37", 6.5: "37", 7: "37-38", 7.5: "38",
                    8: "38-39", 8.5: "39", 9: "39-40", 9.5: "40", 10: "40-41", 10.5: "41", 11: "41-42", 11.5: "42", 12: "42-43"})


men_chart.update({6: "39", 6.5: "39", 7: "40", 7.5: "40-41", 8: "41", 8.5: "41-42", 9: "42", 9.5: "42-43",
                  10: "43", 10.5: "43-44", 11: "44", 11.5: "44-45", 12: "45", 13: "46", 14: "47", 15: "48", 16: "49"})


# a function to convert US shoe size to EU.
def get_eu_size():
    print("Hello! You can convert your shoe size from US to EU.")
    gender = input(
        "Please make your choice between man -\"m\" / woman - \"w\": \n")
    us_size = input("Please enter your US shoes size: ")
    if "." not in us_size:
        us_size = int(us_size)
    else:
        us_size = float(us_size)
    if gender == "m":
        for us, size in men_chart.items():
            if us_size == us:
                print("Your EU size is:", end=" ")
                return size
    if gender == "w":
        for us, size in women_chart.items():
            if us_size == us:
                print("Your EU size is:", end=" ")
                return us
    print("Have a nice day!")

# print(get_eu_size())


# a function to convert EU shoe size to US.
def get_us_size():
    print("Hello! You can convert your shoe size from EU to US.")

    gender = input(
        "Please make your choice between man -\"m\" / woman - \"w\": \n")
    # In this input we will not convert a string to integer (because our origin values in dict are strings).
    eu_size = input("Please enter your EU shoes size: ")
    if gender == "m":
        for us, size in men_chart.items():
            if eu_size == size:
                print("Your US size is:", end=" ")
                return us
            # if user`s input is for ex. 43.5 (but not 43-44 like in the chart dictionary):
            elif eu_size == size + ".5":
                print("Your US size is:", end=" ")
                return int(us + 0.5)
    if gender == "w":
        for us, size in women_chart.items():
            if eu_size == size:
                print("Your US size is:", end=" ")
                return us
            elif eu_size == size + ".5":
                print("Your US size is:", end=" ")
                return int(us + 0.5)


print(get_us_size())
