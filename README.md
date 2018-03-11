# Python Audio processing tools in a Docker image
This repo is meant to provide a prepared environment to carry out audio processing and analysis in Python 2.7. Currently [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis) is included (its dependencies are also installed), but other tools like relevant [bio.bio packages](https://www.idiap.ch/software/bob/docs/bob/bob/stable/list.html#signal-audio-image-and-video-processing) are also planned to be added.

## Testing
To execute silence removal (from pyAudioAnalysis) on a sample file, execute

    docker run py_audio bash -c "python test/test_silence_removal.py"