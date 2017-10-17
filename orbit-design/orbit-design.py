from astropy.time import TimeEpochDate


class orbit():
    def __init__(self, *, pos, vel, epoch, **kwargs):
        print(pos, vel, epoch)
        print(kwargs)

if __name__ == '__main__':
    sat = orbit(pos=[0, 0, 0], vel=[0, 0, 0], epoch=TimeEpochDate.value)
