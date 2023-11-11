# Interactions BTT
# Notes:
# Communication Mediums: Discord, Slack, Text
# Softwares Used: Colab, Librosa, Hugging Face (internal libraries), “Git”

# Action items:
# -> Documentation of prior code
# -> Get github reposition up-to-date
# -> Data Pre-Processing (creating new features to qualify the audio data)
# -> Working on Model

# Road So Far:
# Dataset was converted from Hugging Face to a Pandas Dataframe
# -> Used Pandas
# Created synthetic counterparts for every ‘real’ audio
# -> Used GTTS (Google Text-to-Speech) in order to retrieve AI-generated audio
# Audio files turned into array inputs & feature selection
# -> Used Torch Audio
# -> Getting transcript, path, whether or not AI-generated, and spectrogram array
# Sliced into only 1,000 examples – 500 synthetic and 500 human
# -> Using Pandas
