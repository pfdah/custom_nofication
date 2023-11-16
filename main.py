import win10toast

pop = win10toast.ToastNotifier()
pop.show_toast("Water Alert","Drink water. It is drinking time."
                ,duration=3,icon_path='src\water.ico')

while pop.notification_active():
    pass

exit(0)
