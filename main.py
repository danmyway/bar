#!/usr/bin/env python3
import argparse
from copr.v3 import BuildProxy

COPR_CONFIG = {"copr_url": "https://copr.fedorainfracloud.org"}
SESSION = BuildProxy(COPR_CONFIG)

parser = argparse.ArgumentParser(
    description="Returns copr build ID based on alias contained in package version.",
    formatter_class=argparse.RawTextHelpFormatter,
)

parser.add_argument(
    "project", help="Specify, under which project to look for the package build ID."
)

parser.add_argument("package", help="Specify, which package to get the build ID for.")

parser.add_argument(
    "reference", help="Specify a string for which to look for in the NVR."
)

parser.add_argument(
    "-o",
    "--owner",
    default="@oamg",
    help="Define required package build owner.\nDefault: %(default)s",
)

args = parser.parse_args()


def get_build_id():
    query = SESSION.get_list(args.owner, args.project)
    for build in query:
        if (
            build.state != "failed"
            and build.submitter == 'packit'
            and args.reference in build.source_package["version"]
            and args.package in build.source_package["name"]
        ):
            print(build.id)


if __name__ == "__main__":
    get_build_id()
