# Red Dead Redemption 2 - PC Photomode extractor

This script extracts your photomode pictures from your save games folder and converts them to jpg. Simply run rdr2_photomode.py and a folder with your images will appear. 

# Troubleshooting
## What do I need to run this?
Install [Python 3](https://www.python.org/)

## Nothing happens?
You might need to adapt the path to your RDR2 save game folder. Edit rdr2_photomode.py and replace the path in this line:
```
dir = os.path.expanduser('~') + "\Documents\Rockstar Games\Red Dead Redemption 2\Profiles"
```

Have fun