class Messenger:
    def send_message(self):
        print("Text message is sent")
    def receive_message(self):
        print("Text message is received")
class InternalMessenger(Messenger):
    pass
class WhatsAppMessenger(Messenger):
    def send_message(self):  # Override the method
        print("Text, Photos, Videos and Files are sent")
    def receive_message(self):  # Override the method
        print("Text, Photos, Videos and Files are received")
    def set_dp(self):  #Specialized method
        print("Display picture is set")
    def set_status(self):  #Specialized method
        print("Status is set")
        
im = InternalMessenger()
im.send_message()  #Inherited method
im.receive_message()  #Inherited method

wam = WhatsAppMessenger()
wam.send_message()  #Overridden method
wam.receive_message()  #Overridden method
wam.set_dp()  #Specialized method
wam.set_status()  #Specialized method
