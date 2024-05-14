from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title='****Take Rest****',
            message='Rest is vital for better mental health, increased concentration and memory, a healthier immune system, reduced mood and even a better metabolism.',
            app_icon = "C:/Users\avinay shau/Downloads/Break",
            timout= 5)
        time.sleep(10)