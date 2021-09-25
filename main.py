from csv import DictReader
from art import *

yes_count = 0
no_count = 0
total = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

family = input("Enter which (Type) of your family : ")
age_grp = input("Enter your Age group: ")
incm_status = input("Enter your Income status: ")

with open("Book1.csv") as file:
    data = DictReader(file)
    for row in data:
        # print(row)
        if (row["Will they buy a car"] == "yes"):
            yes_count += 1
        if (row["Will they buy a car"] == "no"):
            no_count += 1
        total += 1

    yes_p = yes_count / total
    no_p = no_count / total

with open("Book1.csv") as file:
    data = DictReader(file)
    for row in data:
        if (row["Type of family"] == family  and row["Will they buy a car"] == "yes"):
            c1 += 1
        if (row["Type of family"] == family  and row["Will they buy a car"] == "no"):
            c2 += 1
        if (row["Age group"] == age_grp and row["Will they buy a car"] == "yes"):
            c3 += 1
        if (row["Age group"] == age_grp and row["Will they buy a car"] == "no"):
            c4 += 1
        if (row["Income Status"] == incm_status and row["Will they buy a car"] == "yes"):
            c5 += 1
        if (row["Income Status"] == incm_status and row["Will they buy a car"] == "no"):
            c6 += 1


    p1 = c1 / yes_count
    p2 = c2 / no_count
    p3 = c3 / yes_count
    p4 = c4 / no_count
    p5 = c5 / yes_count
    p6 = c6 / no_count


    p_classes_yes = p1 * p3 * p5
    p_classes_no = p2 * p4 * p6

    final_probability_yes = p_classes_yes * yes_p
    final_probability_no = p_classes_no * no_p

    if (final_probability_yes > final_probability_no):
        print("\nYou will buy a car")
    elif (final_probability_yes < final_probability_no):
        print("\nYou will not buy a car")
    else:
        print("\nThe output cannot be predicted or wrong inputs haveN been given")
