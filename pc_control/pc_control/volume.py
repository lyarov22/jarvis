from .sound import Sound


# Устанавливает громкость
def volumeSet(vol):
    Sound.volume_set(vol)

    
# Повышает громкость на 2
def volumeUp():
    Sound.volume_up()


# Понижает громкость на 2
def volumeDown():
    Sound.volume_down()


# Убирает громкость, сохраняет предыдущее
def volumeMute():
    cur = Sound.current_volume()
    Sound.mute()

    return cur


# Ставит громкость на всю, сохраняет предыдущее
def volumeMax():
    cur = Sound.current_volume()
    Sound.volume_max()
    
    return cur
