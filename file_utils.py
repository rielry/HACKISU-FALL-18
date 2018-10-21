import os
import music21
import mido
from collections import Counter

scales = {
    'C':{'A':'Am','B':'Bm7','C':'C','D':'Dm','E':'Em','F':'F','G':'G'},
    'C#':{'A#':'A#m','B#':'B#m7','C#':'C#','D#':'D#m','E#':'E#m','F#':'F#','G#':'G#'},
    'Db':{'Ab':'Ab','Bb':'Bbm','C':'Cm7','Db':'Db','Eb':'Ebm','F#':'F#m','Gb':'Gb'},
    'D':{'A':'A','B':'Bm','C#':'C#m7','D':'D','E':'Em','F#':'F#m','G':'G'},
    'Eb':{'Ab':'Ab','Bb':'Bb','C':'Cm','D':'Dm7','Eb':'Eb','F#':'F#m','G':'Gm'},
    'E':{'A':'A','B':'B','C#':'C#m','D#':'D#m7','E':'E','F#':'F#m','G#':'G#m'},
    'F':{'A#':'A#m','B':'B','C':'C','D':'Dm','E':'Em7','F':'F','G':'Gm'},
    'F#':{'A#':'A#m','B':'B','C#':'C#','D#':'D#m','E#':'E#m7','F#':'F#','G#':'G#m'},
    'Gb':{'Ab':'Abm','Bb':'Bbm','Cb':'Cb','Db':'Db','Eb':'Ebm','F':'Fm7','Gb':'Gb'},
    'G':{'A':'Am','B':'Bm','C':'C','D':'D','E':'Em','F#':'F#m7','G':'G'},
    'Ab':{'Ab':'Ab','Bb':'Bbm','C':'Cm','Db':'Db','Eb':'Eb','F':'Fm','Gm7':'Gm7'},
    'A':{'A':'A','B':'Bm','C#':'C#m','D':'D','E':'E','F':'F#m','G#':'G#m7'},
    'Bb':{'A':'Am7','Bb':'Bb','C':'Cm','D':'Dm','Eb':'Eb','F':'F','G':'Gm'},
    'B':{'A#':'A#m7','B':'B','C#':'C#m','D#':'D#m','E':'E','F#':'F#','G#':'G#m'},
    'Am':{'A':'Am','B':'Bm7','C':'C','D':'Dm','E':'Em','F':'F','G':'G'},
    'A#m':{'A#':'A#m','B#':'B#m7','C#':'C#','D#':'D#m','E#':'E#m','F#':'F#','G#':'G#'},
    'Bbm':{'Ab':'Ab','Bb':'Bbm','C':'Cm7','Db':'Db','Eb':'Ebm','F#':'F#m','Gb':'Gb'},
    'Bm':{'A':'A','B':'Bm','C#':'C#m7','D':'D','E':'Em','F#':'F#m','G':'G'},
    'Cm':{'Ab':'Ab','Bb':'Bb','C':'Cm','D':'Dm7','Eb':'Eb','F#':'F#m','G':'Gm'},
    'C#m':{'A':'A','B':'B','C#':'C#m','D#':'D#m7','E':'E','F#':'F#m','G#':'G#m'},
    'Dm':{'A#':'A#m','B':'B','C':'C','D':'Dm','E':'Em7','F':'F','G':'Gm'},
    'D#m':{'A#':'A#m','B':'B','C#':'C#','D#':'D#m','E#':'E#m7','F#':'F#','G#':'G#m'},
    'Ebm':{'Ab':'Abm','Bb':'Bbm','Cb':'Cb','Db':'Db','Eb':'Ebm','F':'Fm7','Gb':'Gb'},
    'Em':{'A':'Am','B':'Bm','C':'C','D':'D','E':'Em','F#':'F#m7','G':'G'},
    'Fm':{'Ab':'Ab','Bb':'Bbm','C':'Cm','Db':'Db','Eb':'Eb','F':'Fm','Gm7':'Gm7'},
    'F#m':{'A':'A','B':'Bm','C#':'C#m','D':'D','E':'E','F':'F#m','G#':'G#m7'},
    'Gm':{'A':'Am7','Bb':'Bb','C':'Cm','D':'Dm','Eb':'Eb','F':'F','G':'Gm'},
    'G#m':{'A#':'A#m7','B':'B','C#':'C#m','D#':'D#m','E':'E','F#':'F#','G#':'G#m'}
}

def makefile(tempo, style, chords):
    file = open('result.mma' ,'w+', 0)
    file.write('Tempo ' + tempo + '\n')
    file.write('Groove ' + style + '\n')
    i = 1
    for j in chords:
        file.write(i + '\t' + j + '\n')
        i += 1
def getchords(midifile, bpm, timesig, key):
    chords = []
    mf = music21.midi.MidiFile()
    mf.open(str(midifile))
    mf.read()
    mf.close()
    s = music21.midi.translate.midiFileToStream(mf)
    s.insert(0.0, music21.meter.TimeSignature(timesig))
    measures = music21.stream.makeNotation.makeMeasures(s, meterStream=None, refStreamOrTimeRange=None, searchContext=False, innerBarline=None, finalBarline='final', bestClef=False, inPlace=False)
    for measure in measures:
        notes = []
        for pitch in [str(p) for p in measure.pitches]:
            notes.append(pitch[:-1])
        c = Counter(notes)
        if (c.most_common(1)[0][0]) in list(scales[key].keys()):
            chords.append(c.most_common(1)[0][0])
        else:
            chords.append(chords[len(chords)-1])
    prog = []
    for chord in chords:
        prog.append(scales[key][chord])
    return prog