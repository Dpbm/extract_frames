# extract frames from a mp4 video



https://github.com/Dpbm/extract_frames/assets/75098594/789637b4-6ba7-488a-95d2-07de1737251a



This is an old project of mine, using python, to extract frames from a video.

The idea here is an automate this process, and learning something about [Pillow](https://pillow.readthedocs.io/en/stable/) and [OpencvPython](https://pypi.org/project/opencv-python/).

## Requirements

To run that you need to have installed in your machine:

* python3 (3.8)
* pip
* git

Using [Pipenv](https://pipenv.pypa.io/en/latest/) or [conda](https://www.anaconda.com/) is optional here, but recommended.

## Installation

To install this project:

1. clone this repo

```bash
git clone https://github.com/Dpbm/extract_frames.git
cd extract_frames
```

3. install dependencies

```bash
# using pip
pip install -r requirements.txt

# using conda
conda env create -f enviroment.yml
conda activate extract_frames

# using pipenv
pipenv install
pipenv shell
```

## Using

In the project directory run:

```bash
python3 main.py
```

Then provide the `folder path` where the videos are and the `salt number`, this number provides how much time you need to wait before getting a frame.

The resulting images are put inside the directory `./frames`

`Note: this scripts run over a folder, not a single file!` 

--- 

For sure, this is a too simple project, and all this could be done so much better using [ffmpeg](https://ffmpeg.org/) or similar. However, this project I've made a couple of year ago, and I don't intend to update it for now.

If you want to update this project by yourself, I'll be pleasured to accept your pull request :)
