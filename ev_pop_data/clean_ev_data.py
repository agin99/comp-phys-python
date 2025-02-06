ev_data = open('Electric_Vehicle_Population_Data.csv', 'r')
data_matrix = []
unique_data_points_per_category = []
final_data_dict = {}
for line in ev_data:
    data_component_list = line.split(',')
    data_matrix.append(data_component_list)

first_ev_data = data_matrix[0]
category_list = []
for index, datapoint in enumerate(first_ev_data):
    category_list.append(str(datapoint))
    unique_data_points_per_category.append(set())

for data_group in data_matrix[1:]:
    if len(data_group) == 18:
        extra_val = data_group[16]
        data_group.pop(16)
        list_to_join = [data_group[15], extra_val]
        data_group[15] = ",".join(list_to_join)
    for index, item in enumerate(data_group):
        unique_data_points_per_category[index].add(item)
    if not final_data_dict.get(data_group[6]):
        final_data_dict[data_group[6]] = {}
        final_data_dict[data_group[6]]['total_count'] = 1
        final_data_dict[data_group[6]][data_group[7]] = {}
        final_data_dict[data_group[6]][data_group[7]]['total_count'] = 1
    elif not final_data_dict[data_group[6]].get(data_group[7]):
        final_data_dict[data_group[6]]['total_count'] += 1
        final_data_dict[data_group[6]][data_group[7]] = {}
        final_data_dict[data_group[6]][data_group[7]]['total_count'] = 1
    else:
        final_data_dict[data_group[6]]['total_count'] += 1
        final_data_dict[data_group[6]][data_group[7]]['total_count'] += 1

print(final_data_dict['TESLA']['total_count'])

for key, value in  final_data_dict.items():
    print(key, value)





