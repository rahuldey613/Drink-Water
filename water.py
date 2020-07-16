import time
from plyer import notification

if __name__== "__main__":
    while True:
         notification.notify(
                title ="please drink water",
                message= "Benefits",
                
                timeout=5
  )
         time.sleep(60*60)
