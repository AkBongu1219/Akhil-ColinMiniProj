#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

# Frequencies for notes in Hz (values rounded from https://forum.professionalcomposers.com/t/note-frequency-chart-free-guide/506)
notes = {
    'C4': 262,  'D4': 294,  'E4': 330,  'F4': 349, 'F#4': 370, 'G4': 392, 'G#4': 415, 'A4': 440,  'Bb4': 466,  'B4': 494,
    'C5': 523,  'D5': 587, 'D#5': 622, 'E5': 659,  'F5': 698, 'F#5': 740, 'G5': 784,  'A5': 880,  'B5': 988
    
}

# The Super Mario Bros Theme (adapted from https://noobnotes.net/super-mario-bros-theme-nintendo/)
melody = [
    ('E5', 0.2), ('E5', 0.2), ('E5', 0.2),
    ('C5', 0.2), ('E5', 0.2), ('G5', 0.2), ('G4', 0.4),

    ('C5', 0.2), ('G4', 0.2), ('E4', 0.2),
    ('A4', 0.2), ('B4', 0.2), ('Bb4', 0.2), ('A4', 0.4),

    ('G4', 0.2), ('E5', 0.2), ('G5', 0.2), ('A5', 0.2),
    ('F5', 0.2), ('G5', 0.2), ('E5', 0.2), ('C5', 0.2), ('D5', 0.2), ('B4', 0.4),

    ('C5', 0.2), ('G4', 0.2), ('E4', 0.2),
    ('A4', 0.2), ('B4', 0.2), ('Bb4', 0.2), ('A4', 0.4),

    ('G4', 0.2), ('E5', 0.2), ('G5', 0.2), ('A5', 0.2),
    ('F5', 0.2), ('G5', 0.2), ('E5', 0.2), ('C5', 0.2), ('D5', 0.2), ('B4', 0.4),

    ('G5', 0.2), ('F#5', 0.2), ('F5', 0.2), ('D5', 0.2), ('E5', 0.2),
    ('G4', 0.2), ('A4', 0.2), ('C5', 0.4),
    ('A4', 0.2), ('C5', 0.2), ('D5', 0.4),

    ('G5', 0.2), ('F#5', 0.2), ('F5', 0.2), ('D5', 0.2), ('E5', 0.2),
    ('C5', 0.2), ('C5', 0.4), ('C5', 0.4),

    ('G5', 0.2), ('F#5', 0.2), ('F5', 0.2), ('D5', 0.2), ('E5', 0.2),
    ('G4', 0.2), ('A4', 0.2), ('C5', 0.4),
    ('A4', 0.2), ('C5', 0.2), ('D5', 0.4),
    ('D#5', 0.2), ('D5', 0.2), ('C5', 0.4),

    ('C5', 0.2), ('C5', 0.2), ('C5', 0.2),
    ('C5', 0.2), ('D5', 0.2), ('E5', 0.2), ('C5', 0.2), ('A4', 0.2), ('G4', 0.4),
    
    ('C5', 0.2), ('C5', 0.2), ('C5', 0.2),
    ('C5', 0.2), ('D5', 0.2), ('E5', 0.4),

    ('E5', 0.2), ('E5', 0.2), ('E5', 0.2),
    ('C5', 0.2), ('E5', 0.2), ('G5', 0.2), ('G4', 0.4),

    ('C5', 0.2), ('G4', 0.2), ('E4', 0.2),
    ('A4', 0.2), ('B4', 0.2), ('Bb4', 0.2), ('A4', 0.4),

    ('G4', 0.2), ('E5', 0.2), ('G5', 0.2), ('A5', 0.2),
    ('F5', 0.2), ('G5', 0.2), ('E5', 0.2), ('C5', 0.2), ('D5', 0.2), ('B4', 0.4),

    ('C5', 0.2), ('G4', 0.2), ('E4', 0.2),
    ('A4', 0.2), ('B4', 0.2), ('Bb4', 0.2), ('A4', 0.4),

    ('E5', 0.2), ('C5', 0.2), ('G4', 0.2),
    ('G4', 0.2), ('A4', 0.2), ('F5', 0.2), ('F5', 0.2), ('A4', 0.2),
    ('B4', 0.2), ('A5', 0.2), ('A5', 0.2), ('A5', 0.2), ('G5', 0.2), ('F5', 0.2),
    ('E5', 0.2), ('C5', 0.2), ('A4', 0.2), ('G4', 0.4),

    ('E5', 0.2), ('C5', 0.2), ('G4', 0.2),
    ('G4', 0.2), ('A4', 0.2), ('F5', 0.2), ('F5', 0.2), ('A4', 0.2),
    ('B4', 0.2), ('F5', 0.2), ('F5', 0.2), ('F5', 0.2), ('E5', 0.2), ('D5', 0.2), ('C5', 0.4),

    ('C5', 0.2), ('G4', 0.2), ('E4', 0.2),
    ('A4', 0.2), ('B4', 0.2), ('A4', 0.2),
    ('G#4', 0.2), ('Bb4', 0.2), ('G#4', 0.2), ('G4', 0.2), ('F#4', 0.2), ('G4', 0.4),
]


print("Playing melody:")

for note, duration in melody:
    freq = notes[note]  # Get the frequency for the note
    print(f"Playing {note} ({freq} Hz) for {duration} seconds")
    playtone(freq, duration)
    

# Turn off the PWM
quiet()
