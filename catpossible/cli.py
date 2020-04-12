import os
import shutil

import click
from pyemojify import emojify
from tqdm import tqdm

from catpossible.detector import cat_detector
from catpossible.utils import resolve_paths

CUSTOM_BAR_FORMAT = emojify(
    "{percentage:3.0f}% {bar} {n_fmt}/{total_fmt} :alarm_clock: {remaining}{postfix}"
)
BAR_POSTFIX = emojify(":cat2: {0} :no_good: {1}")


@click.command()
@click.argument("source", metavar="PHOTO_DIR", type=click.Path(exists=True))
@click.option(
    "-d",
    "--dest",
    "destination",
    type=click.Path(),
    help="Destination for found cat photos (default: current dir).",
    default=".",
)
@click.option(
    "-m/--move",
    "move_not_copy",
    type=bool,
    help="Move found cat photos instead of copying.",
)
def main(source, destination, move_not_copy):
    jpegs = list([fn for fn in resolve_paths(source) if fn.lower().endswith("jpg")])
    cats_found = 0
    not_cats = 0
    moving_function = shutil.move if move_not_copy else shutil.copy

    if not os.path.exists(destination):
        os.mkdir(destination)

    with tqdm(
        total=len(jpegs),
        unit="photo",
        bar_format=CUSTOM_BAR_FORMAT,
        postfix=BAR_POSTFIX.format(0, 0),
    ) as t:
        for fn in jpegs:
            is_possible_cat = cat_detector(fn)
            if is_possible_cat:
                cats_found += 1
                moving_function(fn, destination)
            else:
                not_cats += 1

            t.postfix = BAR_POSTFIX.format(cats_found, not_cats)
            t.update()


if __name__ == "__main__":
    main()
