# Playing with SimpleITK

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to play with [SimpleITK](https://github.com/SimpleITK/SimpleITK).

## Requirements

-   Install version 3.7 of [Python 3.X](https://www.python.org/downloads/),
-   Install the required packages:

```bash
pip install -r requirements.txt
```

NB: As of November 2019, the PyPI package of SimpleITK does not work with Python 3.8.

## Data

-   Download data from the [Combined (CT-MR) Healthy Abdominal Organ Segmentation](https://chaos.grand-challenge.org/Combined_Healthy_Abdominal_Organ_Segmentation/) (CHAOS) challenge,
-   Extract the archive to `data/`.

## Usage

Convert data from [DICOM](https://en.wikipedia.org/wiki/DICOM) to [NifTI](https://en.wikipedia.org/wiki/Neuroimaging_Informatics_Technology_Initiative):
```bash
python convert_to_nii.py
```

## References

-   [Github repository](https://github.com/SimpleITK/SimpleITK) for SimpleITK,
-   [Notebooks](https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks) for SimpleITK,
-   [Documentation](https://itk.org/SimpleITKDoxygen/html/index.html) for SimpleITK,
-   [Combined (CT-MR) Healthy Abdominal Organ Segmentation](https://chaos.grand-challenge.org/Combined_Healthy_Abdominal_Organ_Segmentation/) (CHAOS) challenge,
-   Evaluation of segmentation results with [tools](https://github.com/emrekavur/CHAOS-evaluation) provided by organizers of CHAOS.   

<!-- Definitions -->

[build]: <https://travis-ci.org/woctezuma/playing-with-simpleitk>
[build-image]: <https://travis-ci.org/woctezuma/playing-with-simpleitk.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/playing-with-simpleitk/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/playing-with-simpleitk/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/playing-with-simpleitk/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/playing-with-simpleitk>
[codecov-image]: <https://codecov.io/gh/woctezuma/playing-with-simpleitk/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/playing-with-simpleitk>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/TODO>
