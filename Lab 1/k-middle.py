import numpy as np
import pandas


def euklid_distance(center, coord):
    return round(np.linalg.norm(center - coord), 1)


def recalculate_centroids(coords, clusters):
    def recalculation(coord_assign_to_cluster):
        num = 0
        new_x = 0
        new_y = 0
        for index, value in coord_assign_to_cluster.iterrows():
            x, y = value['coords']
            new_x = new_x + x
            new_y = new_y + y
            num = num + 1
        return (round(new_x/num, 1), round(new_y/num, 1))

    data = pandas.DataFrame({'coords': coords, 'cluster': clusters})
    centroid1 = recalculation(data[data.values == 1])
    centroid2 = recalculation(data[data.values == 2])
    centroid3 = recalculation(data[data.values == 3])
    centroid4 = recalculation(data[data.values == 4])
    return [centroid1, centroid2, centroid3, centroid4]


centroids = [(2, 2), (2, 8), (8, 2), (8, 8)]

dataset = {
    'coords': [(5, 7),
               (2, 1),
               (1, 3),
               (9, 8),
               (5, 4),
               (10, 7),
               (1, 9),
               (8, 2),
               (2, 8),
               (9, 3)],
    'centroid1': ["","","","","","","","","",""],
    'centroid2': ["","","","","","","","","",""],
    'centroid3': ["","","","","","","","","",""],
    'centroid4': ["","","","","","","","","",""],
    'cluster': ["","","","","","","","","",""]
}

dataframe = pandas.DataFrame(data=dataset)
print('Start dataset'.center(150, "="))
print(dataframe)
print("End start dataset".center(150, "="))

while True:
    cluster = []
    needs_recalculation = []
    dataframe['centroid1'] = dataframe['coords'].map(lambda coord: euklid_distance(np.array(centroids[0]), np.array(coord)))
    dataframe['centroid2'] = dataframe['coords'].map(lambda coord: euklid_distance(np.array(centroids[1]), np.array(coord)))
    dataframe['centroid3'] = dataframe['coords'].map(lambda coord: euklid_distance(np.array(centroids[2]), np.array(coord)))
    dataframe['centroid4'] = dataframe['coords'].map(lambda coord: euklid_distance(np.array(centroids[3]), np.array(coord)))
    for index, row in dataframe.iterrows():
        min = pandas.Series(data=[row['centroid1'], row['centroid2'], row['centroid3'], row['centroid4']]).min()
        cluster_count = 0
        for num, item in enumerate([row['centroid1'], row['centroid2'], row['centroid3'], row['centroid4']]):
            if item == min:
                potential_cluster = num+1
                cluster_count = cluster_count+1
        cluster.append(potential_cluster)
        if cluster_count == 1:
            needs_recalculation.append(False)
        else:
            needs_recalculation.append(True)
    dataframe['cluster'] = pandas.Series(cluster)
    dataframe['recalc'] = pandas.Series(needs_recalculation)

    if dataframe['recalc'].max():
        centroids = recalculate_centroids(dataframe['coords'], dataframe['cluster'])
    else:
        break

print("Result dataframe".center(150, "*"))
print(dataframe)



