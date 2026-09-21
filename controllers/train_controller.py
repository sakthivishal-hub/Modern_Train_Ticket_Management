from models.train import Train

class TrainController:

    def __init__(self):
        self.trains=[]

    def add_train(self,t_id,t_name,source,destination,arr_time,dep_time,t_type,available_seats):

        train = Train(t_id,t_name,source,destination,arr_time,dep_time,t_type,available_seats)

        self.trains.append(train)

        return train    

    def search_train(self,source,destination):
        results=[]
        for train in self.trains:
            if train.source==source and train.destination==destination:
                results.append(train)
        return results
    

    def train_details(self,t_id):

        for train in self.trains:

            if train.t_id==t_id:
                return train

        return None

    
    def train_details(self,t_id):

        for train in self.trains:

            if train.t_id==t_id:
                return train

        return None
    

    def update_train(self,t_id,t_name,source,destination,arr_time,dep_time,t_type,available_seats):

        for train in self.trains:

            if train.t_id==t_id:
                if t_name is not None:
                    train.t_name=t_name
                if source is not None:
                    train.source=source
                if destination is not None:
                    train.destination=destination
                if arr_time is not None:
                    train.arr_time=arr_time
                if dep_time is not None:
                    train.dep_time=dep_time
                if t_type is not None:
                    train.t_type=t_type
                if available_seats is not None:
                    train.available_seats=available_seats

                return train
        return None

    def remove_train(self, t_id):

        for train in self.trains:

            if train.t_id == t_id:
                self.trains.remove(train)
                return True

        return False

    def check_available_seats(self, t_id):

        for train in self.trains:

            if train.t_id == t_id:
                return train.available_seats

        return None