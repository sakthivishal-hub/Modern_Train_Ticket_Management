class TrainView:

    def get_train_details(self):

        print("\n===== ADD TRAIN =====")

        t_id = int(input("Enter Train ID: "))
        t_name = input("Enter Train Name: ")
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        arr_time = input("Enter Arrival Time: ")
        dep_time = input("Enter Departure Time: ")
        t_type = input("Enter Train Type: ")
        available_seats = int(input("Enter Available Seats: "))

        return (t_id,t_name,source,destination,arr_time,dep_time,t_type,available_seats)

    def get_search_details(self):

        print("\n===== SEARCH TRAIN =====")

        source = input("Enter Source: ")
        destination = input("Enter Destination: ")

        return source, destination


    def display_train(self, train):

        print("\n----------------------------")
        print("Train ID       :", train.t_id)
        print("Train Name     :", train.t_name)
        print("Source         :", train.source)
        print("Destination    :", train.destination)
        print("Arrival Time   :", train.arr_time)
        print("Departure Time :", train.dep_time)
        print("Train Type     :", train.t_type)
        print("Available Seats:", train.available_seats)
        print("----------------------------")

    def display_trains(self, trains):

        if not trains:
            print("\nNo trains found.")
            return

        print("\n===== AVAILABLE TRAINS =====")

        for train in trains:
            self.display_train(train)


    def get_update_details(self):

        print("\n===== UPDATE TRAIN =====")

        t_name = input("New Train Name (Enter to skip): ")
        source = input("New Source (Enter to skip): ")
        destination = input("New Destination (Enter to skip): ")
        arr_time = input("New Arrival Time (Enter to skip): ")
        dep_time = input("New Departure Time (Enter to skip): ")
        t_type = input("New Train Type (Enter to skip): ")

        seats = input("New Available Seats (Enter to skip): ")

        if seats:
            available_seats = int(seats)
        else:
            available_seats = None

        return (
            t_name or None,
            source or None,
            destination or None,
            arr_time or None,
            dep_time or None,
            t_type or None,
            available_seats
        )