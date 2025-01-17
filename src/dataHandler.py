from rocketData import RocketData as rd
class SendData:
    """
    This only deals with sending the rocketdata. RocketData class in src/rocketData.py deals with manipulating the data.  
    
    ...

    Attributes
    ----------
    rocket_data 
        protected attribute that holds all the sensor rocket data imported from rocketData

    Methods
    -------
    send_bme(self, sendingTo)
        Desciption:
            only called in send_all
        Parm:
            sendingTo can either be "blackbox", "antenna"
            
    send_imu(self, sendingTo)
        Desciption:
            only called in send_all
        Parm:
            sendingTo can either be "blackbox", "antenna"
            
    send_strain_gauges(self, sendingTo)
         Desciption:
            only called in send_all
        Parm:
            sendingTo can either be "blackbox", "antenna"
            
    send_all_data(self, sendingTo)
        Desciption:
            Calls all send_[sensor] methods and sends an updated 
        Parm:
            sendingTo can either be "blackbox", "antenna"
            
    format_to_send(self, sendingTo)
        Description:
            formats the data into a sendable state
        Parm:
            sendingTo: can either be "blackbox", "ground"
            dataToFomat: Which sensor is needed to be called
    
    -------
    """
    def __init__(self, rd):
        rocket_data = rd
    
    # TODO: parm rd is a dict of updated 
    def update_rocket_data(self, rocketData):
        rocket_data = rd.data_dict_set(rocketData)
        
    def send_bme(self, sendingTo):
        # call format data
        return

    def send_imu(self, sendingTo):
        return

    def send_strain_gauges(self, sendingTo):
        return
    
    def send_all_data(self, sendingTo):
        return
       
    def format_to_send(self, sendingTo, dataToFomat):
        return

    

