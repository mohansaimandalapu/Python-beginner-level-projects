from pynotifier import Notification
for i in range(10):
    n = Notification(title="ALTER",description=f"{i}YOUR SYSTEM IS HACKED ,YOU ARE IN DANGER",duration=1e-3,urgency=Notification.URGENCY_CRITICAL,icon_path="/home/panther/Downloads/Hacker-icon.png")
    n.send()
    
    