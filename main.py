from pydub import AudioSegment

global mp3
global sped_up_speed
global slow_down_speed

mp3 = None
speed_up_speed = 1.5
slow_down_speed = 0.5 

def spedup(speed, song, output_name):
    sound = AudioSegment.from_file(song)
    sped_up_sound = sound.speedup(playback_speed=float(speed))
    sped_up_sound.export(output_name, format="mp3")

def slowdown(speed, song, output_name):
    sound = AudioSegment.from_file(song)
    slowed_down_sound = sound.speedup(playback_speed=float(speed))
    slowed_down_sound.export(output_name, format="mp3")

def nightcore(song, output_name):
    sound = AudioSegment.from_file(song)
    nightcore_sound = sound.speedup(playback_speed=speed_up_speed)
    nightcore_sound = nightcore_sound.set_frame_rate(int(sound.frame_rate * (speed_up_speed ** 0.5)))
    nightcore_sound.export(output_name, format="mp3")

def pitchup(pitch_factor, song, output_name):
    sound = AudioSegment.from_file(song)
    pitchup_sound = sound.set_frame_rate(int(sound.frame_rate * pitch_factor))
    pitchup_sound.export(output_name, format="mp3")

def pitchdown(pitch_factor, song, output_name):
    sound = AudioSegment.from_file(song)
    pitchdown_sound = sound.set_frame_rate(int(sound.frame_rate / pitch_factor))
    pitchdown_sound.export(output_name, format="mp3")

def reverse(song, output_name):
    sound = AudioSegment.from_file(song)
    reversed_sound = sound.reverse()
    reversed_sound.export(output_name, format="mp3")

def fadein(duration, song, output_name):
    sound = AudioSegment.from_file(song)
    faded_sound = sound.fade_in(duration)
    faded_sound.export(output_name, format="mp3")

def fadeout(duration, song, output_name):
    sound = AudioSegment.from_file(song)
    faded_sound = sound.fade_out(duration)
    faded_sound.export(output_name, format="mp3")

def normalize(song, output_name):
    sound = AudioSegment.from_file(song)
    normalized_sound = sound.normalize()
    normalized_sound.export(output_name, format="mp3")

def concatenate(songs, output_name):
    combined_sound = AudioSegment.silent(duration=0)
    for song in songs:
        sound = AudioSegment.from_file(song)
        combined_sound += sound
    combined_sound.export(output_name, format="mp3")

def adjust_volume(change_db, song, output_name):
    sound = AudioSegment.from_file(song)
    adjusted_sound = sound + change_db
    adjusted_sound.export(output_name, format="mp3")

def adjust_bass(factor, song, output_name):
    sound = AudioSegment.from_file(song)
    adjusted_sound = sound.low_pass_filter(factor)
    adjusted_sound.export(output_name, format="mp3")

def adjust_treble(factor, song, output_name):
    sound = AudioSegment.from_file(song)
    adjusted_sound = sound.high_pass_filter(factor)
    adjusted_sound.export(output_name, format="mp3")



question = input("Do you want to modify the audio? Choose from 'spedup', 'slowdown', 'nightcore', 'pitchup', 'pitchdown', 'reverse', 'fadein', 'fadeout', 'normalize', 'concatenate', 'adjust_volume', 'adjust_bass', 'adjust_treble':")
mp3 = input("Enter the name of the MP3 file (it should be in the same directory as the code):")

output_name = input("Enter the name for the output MP3 file (without extension, leave blank for 'results.mp3'):").strip()
if output_name == "":
    output_name = "results.mp3"
else:
    output_name += ".mp3"

if question.lower() == "spedup":
    speed = input("Enter the speed factor for speeding up (leave blank for default {:.2f}):".format(speed_up_speed))
    if speed == "":
        speed = speed_up_speed
    spedup(speed, mp3, output_name)
    print("Congratulations! Your sped-up song is saved as '{}'.".format(output_name))
elif question.lower() == "slowdown":
    speed = input("Enter the speed factor for slowing down (leave blank for default {:.2f}):".format(slow_down_speed))
    if speed == "":
        speed = slow_down_speed
    slowdown(speed, mp3, output_name)
    print("Congratulations! Your slowed-down song is saved as '{}'.".format(output_name))
elif question.lower() == "nightcore":
    nightcore(mp3, output_name)
    print("Congratulations! Your nightcore version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "pitchup":
    pitch_factor = float(input("Enter the pitch factor for pitching up (e.g., 1.5):"))
    pitchup(pitch_factor, mp3, output_name)
    print("Congratulations! Your pitched-up version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "pitchdown":
    pitch_factor = float(input("Enter the pitch factor for pitching down (e.g., 0.5):"))
    pitchdown(pitch_factor, mp3, output_name)
    print("Congratulations! Your pitched-down version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "reverse":
    reverse(mp3, output_name)
    print("Congratulations! Your reversed version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "fadein":
    duration = int(input("Enter the fade-in duration in milliseconds:"))
    fadein(duration, mp3, output_name)
    print("Congratulations! Your faded-in version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "fadeout":
    duration = int(input("Enter the fade-out duration in milliseconds:"))
    fadeout(duration, mp3, output_name)
    print("Congratulations! Your faded-out version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "normalize":
    normalize(mp3, output_name)
    print("Congratulations! Your normalized version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "concatenate":
    num_songs = int(input("Enter the number of songs you want to concatenate:"))
    songs = [input(f"Enter the name of song {i + 1}:") for i in range(num_songs)]
    concatenate(songs, output_name)
    print("Congratulations! Your concatenated version of the songs is saved as '{}'.".format(output_name))
elif question.lower() == "adjust_volume":
    change_db = int(input("Enter the volume change in dB (positive for increase, negative for decrease):"))
    adjust_volume(change_db, mp3, output_name)
    print("Congratulations! Your adjusted volume version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "adjust_bass":
    factor = int(input("Enter the bass adjustment factor (recommended range: 20-200):"))
    adjust_bass(factor, mp3, output_name)
    print("Congratulations! Your adjusted bass version of the song is saved as '{}'.".format(output_name))
elif question.lower() == "adjust_treble":
    factor = int(input("Enter the treble adjustment factor (recommended range: 2000-5000):"))
    adjust_treble(factor, mp3, output_name)
    print("Congratulations! Your adjusted treble version of the song is saved as '{}'.".format(output_name))
else:
    print("Invalid choice. Please choose one of the available options.")
