class Messenger:
    def use_keyboard(self):
        print("Using keyboard")
    def send_message(self):
        print("Text message is sent")
    def receive_message(self):
        print("Text message is received")
        
class WhatsAppMessenger(Messenger):
    def send_message(self):  # Override the method
        print("Text, Photos, Videos and Files are sent")
    def receive_message(self):  # Override the method
        print("Text, Photos, Videos and Files are received")
    def send_live_location(self):
        print("Live location sent")
        
class FacebookMessenger(Messenger):
    def send_message(self):  # Override the method
        print("Text, Photos, Videos and Files are sent via Facebook")
    def receive_message(self):  # Override the method
        print("Text, Photos, Videos and Files are received via Facebook")
    def use_builtin_apps(self):
        print("Using built-in apps of Facebook")
        
class InstaMessenger(Messenger):
    def send_message(self):  # Override the method
        print("Text, Photos, Videos and Files are sent via Instagram")
    def receive_message(self):  # Override the method
        print("Text, Photos, Videos and Files are received via Instagram")
    def add_filters(self):
        print("Filters added to photos and videos")
        
def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()
    
    if type(ref) == WhatsAppMessenger:
        ref.send_live_location()
    elif type(ref) == FacebookMessenger:
        ref.use_builtin_apps()
    elif type(ref) == InstaMessenger:
        ref.add_filters()
        
wa = WhatsAppMessenger()
fb = FacebookMessenger()
insta = InstaMessenger()

use_messenger(wa)
use_messenger(fb)
use_messenger(insta)