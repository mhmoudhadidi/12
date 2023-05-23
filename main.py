def on_forever():
    rain = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever)
