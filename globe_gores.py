#! /usr/bin/env python3
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser(
        prog="GlobGores",
        description="Program for making globe gores from EqRec images.")

    # Positional arguments:
    parser.add_argument(
        "INPUT IMAGE", type=str,
        help="Input file with equirectangular data for one or two hemispheres"
    )
    parser.add_argument(
        "OUTPUT IMAGE", type=str,
        help="File name to use for the resulting gores image"
    )

    # Optional arguments:
    parser.add_argument(
        "-n", "--gores", dest="n_gores", type=int, default=12,
        help="Number of gores (DEFAULT: 12)"
    )
    parser.add_argument(
        "-t", "-type", dest="gores_type", type=str, default="gores",
        choices=["gores", "daisy"],
        help="Type of gores to produce (DEFAULT: 'gores')"
    )
    parser.add_argument(
        "-p", "--projection", dest="projection", type=str, default="cassini",
        choices=["cassini", "mercator", "sinus"],
        help="Projection to use for the gores (DEFAULT: 'cassini')"
    )
    parser.add_argument(
        "-a", "--fillangle", dest="fill_angle", type=float, default=0,
        help="Angle from poles to fill with Lambert azimuthal "
        "(DEFAULT: 0, only works for gore type 'daisy')"
    )
    parser.add_argument(
        "-s", "--scale", dest="scale", type=float, default=1,
        help="Scale of output image relative to input (DEFAULT: 1)"
    )
    parser.add_argument(
        "-b", "--bleed", dest="bleed", type=float, default=0,
        help="Bleed in percent (DEFAULT: 0)"
    )
    parser.add_argument(
        "-X", "--lonstretch", dest="lon_strech", type=float, default=0,
        help="Stretch amount in longitudinal ('X') direction (DEFAULT: 0)"
    )
    parser.add_argument(
        "-Y", "--latstretch", dest="lat_strech", type=float, default=0,
        help="Stretch amount in latitudinal ('Y') direction (DEFAULT: 0)"
    )
    parser.add_argument(
        "-S", "--single", dest="single_hemisphere", action="store_true",
        help="Treat input image as a single hemisphere"
    )
    parser.add_argument(
        "-f", "--force", dest="force_eqrec", action="store_true",
        help="Treat input image as equirectangular, ignoring proportions"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    print(args)
