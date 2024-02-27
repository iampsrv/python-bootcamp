# data_scientist={"python","tensorflow","sql","git","keras"}
# data_analyst= {"python","powerbi","pandas","sql","git"}

# skillsfor_ds_da = data_scientist.union(data_analyst)
# print(skillsfor_ds_da)
# common_skills=data_scientist.intersection(data_analyst)
# print("Common skills",common_skills)

# mydiff = data_scientist.difference(data_analyst)
# print(mydiff)
# mysdiff = data_analyst.symmetric_difference(data_scientist)
# print(mysdiff)

# my_list=[2,4,2,6,8,4,3,1,8,6,2,4]
# print(list(set(my_list)))

my_set = {1, 2, 3}
frozen_set = frozenset(my_set)
frozen_set.add(4) # Adding a single element to the set
frozen_set.update([5, 6, 7])
print(frozen_set)