from MainLoop import MainLoop

class Main(object):

    def __init__(self):
        print "Init Main object..."
        self._mainloop =  MainLoop()


    def run(self):
        self._mainloop.initialize()
        running=True
        frames = 0
        print "ClockDisplay Main starts running..."
        while running:
            try:
                self._mainloop.update()
            except Exception as e:
                running = False
                print str(e)


if __name__ == "__main__":
    print 'Started from: Main.py,  if __name__ == "__main__" '
    gl=Main()
    gl.run()
