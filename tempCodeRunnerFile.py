    def _check_events(self):
        #watch for keyboard and mouse events .
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        sys.exit()