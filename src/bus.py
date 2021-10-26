class Bus:
    def __init__(self, route, destination):
        self.route = route
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "brum brum"
            
    def passenger_total(self):
        return self.passengers
    
    def new_person(self, person):
        return self.passengers.append(person)

    def remove_person(self, person):
        return self.passengers.remove(person)

    def remove_all(self, onboard_passengers):
        return self.passengers.remove(onboard_passengers)
    
    def collect_all_queued(self, queued_stop):
        self.queue.append(self.passengers)
        self.queue.remove(queued_stop)



# first - take all passengers in queue and add them to the bus
# remove people from queue from bus stop

