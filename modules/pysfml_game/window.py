import sfml as sf

SCREEN_WIDTH = 1024; SCREEN_HEIGHT = 768
window = sf.RenderWindow(sf.VideoMode(SCREEN_WIDTH, SCREEN_HEIGHT), "Super Smash Bros: Trading Card Game")
window.framerate_limit = 60
window.vertical_sync_enabled = True