import time

class TrafficLight:


    def running(self):
        while True:
            self.__colour = 'Красный'
            print(f'{self.__colour}')
            time.sleep(7)
            self.__colour = 'Желтый'
            print(f'{self.__colour}')
            time.sleep(2)
            self.__colour = 'Зеленый'
            print(f'{self.__colour}')
            time.sleep(7)


res = TrafficLight()
res.running()
