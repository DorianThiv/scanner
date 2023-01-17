class Ip:

    def __init__(self, ip: str):
        startSplitted = ip.split('.')
        self.b1 = int(startSplitted[3])
        self.b2 = int(startSplitted[2])
        self.b3 = int(startSplitted[1])
        self.b4 = int(startSplitted[0])

    def __str__(self) -> str:
        return f'{self.b4}.{self.b3}.{self.b2}.{self.b1}'