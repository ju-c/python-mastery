from collections import Counter
from read_rides import read_rides_as_dictionnaries

class DataAnalysis:
    def __init__(self):
        self.rows = read_rides_as_dictionnaries('../Data/ctabus.csv')

    def how_many_routes(self):
        return len(set([d['route'] for d in self.rows]))

    def how_many_people_rode_a_route(self, road, date):
        for row in self.rows:
            if row['route'] == road and row['date'] == date:
                return row.get('rides')

    def number_of_rides_on_each_route(self):
        total_rides = Counter()
        for row in self.rows:
            total_rides[row['route']] += row['rides']
        return total_rides

    def greatest_increase_ridership(self):
        bus_routes = sorted(self.number_of_rides_on_each_route(), key=self.number_of_rides_on_each_route().get, reverse=True)
        return bus_routes[:4]
        
            

if __name__ == "__main__":
    my_object = DataAnalysis()
    print(my_object.how_many_routes())
    print(my_object.how_many_people_rode_a_route('22', '02/02/2011'))
    print(my_object.number_of_rides_on_each_route())
    print(my_object.greatest_increase_ridership())