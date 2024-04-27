import csv 
#leer un csv y generar una lista de diccionarios 
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')#reader es un iterable
        header = next(reader) #titulos
        data =[]
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == '__main__':
    data= read_csv('world_population.csv')
    print(data)
