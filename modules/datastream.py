class DataStream(object):
    def __init__(self) -> None:
        print("Datastream initialized...")

    def unpack_arduino_data(self, datastream: str)-> list:
        if datastream is None:
            print("Error: Datastream is None")
            return
        
        incoming_data = datastream.split(';')
        length = len(incoming_data)

        for element in range(length):
            if incoming_data[element].replace(".", "").isnumeric():
                #print(incoming_data[element])
                incoming_data[element] = float(incoming_data[element])

        return incoming_data
    
    def unpack_start_data(self, datastream: str) -> list:
        if datastream is None:
            print("Error: Datastream is None")
            return
        
        incoming_data = datastream.split(';')
        length = len(incoming_data) 

        for i in range(length):
            if incoming_data[i].isdigit():
                incoming_data[i] = float(incoming_data[i])

        return incoming_data
