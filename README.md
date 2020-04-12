# catpossible
![License](https://img.shields.io/github/license/lensvol/pybetter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Tool for sorting out cat photos from your photo collection using pre-trained PyTorch model.

## Why?

Why not?

## How does it work?

It is based on excellent [Detecto](https://detecto.readthedocs.io/en/latest/) package, which in turn uses [Faster R-CNN ResNet-50 FPN](https://arxiv.org/abs/1506.01497) to label objects found in the image. 

Our tool runs the photo through the model and looks through the top labels to see if there is a `cat` amongst them. If it is the case, photo will be copied/moved to the appropriate directory.

False positive rate is ~9%, but that is enough for you to sort through them by hand.

## Usage

```
⇒  catpossible --help
Usage: catpossible [OPTIONS] PHOTO_DIR

Options:
  -d, --dest PATH  Destination for found cat photos (default: current dir).
  -m / --move      Move found cat photos instead of copying.
  --help           Show this message and exit.
```


## Installation

```shell script
# pip install catpossible
```

## Getting started with development

```shell script
# git clone https://github.com/lensvol/catpossible
# poetry install
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

* **Kirill Borisov** ([lensvol@gmail.com](mailto:lensvol@gmail.com))

