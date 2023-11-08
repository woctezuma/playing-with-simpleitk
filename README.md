# Playing with SimpleITK

[![Build status][build-image]][build]
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

### Prepare data

-   Convert data from [DICOM](https://en.wikipedia.org/wiki/DICOM) to [NifTI](https://en.wikipedia.org/wiki/Neuroimaging_Informatics_Technology_Initiative) with SimpleITK:
```bash
python convert_to_nii.py
```

-   Follow instructions for the folder structure of data, as [detailed for nnU-Net](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_format.md).

### Train nnU-Net

-   Connect to a session of [Google Colaboratory](https://colab.research.google.com/)

-   Run the [`playing_with_pytorch.ipynb`][playing_with_pytorch] notebook.
[![Open In Colab][colab-badge]][playing_with_pytorch]

Training was performed with:
-   a training dataset of 5 images downsampled to 4x4x4mm,
-   no cross-validation (in which case the validation dataset is the same as the training dataset to find the best checkpoint and to decrease the learning rate).

Training for 1 epoch can require 2m30s, but up to 10m, depending on the machine which you obtained.

Results obtained after ~ 100 epochs are shown below:

![Training](https://raw.githubusercontent.com/wiki/woctezuma/playing-with-simpleitk/img/training.png)

where:
-   training loss is in blue,
-   validation loss is in red,
-   evaluation metric (to maximize) is in green.

In terms of Dice scores, the average is:
-   99.1% for the 5 patients of the training data,
-   94.8% for the 15 patients of the validation data (training data not used).

## References

-   [Github repository](https://github.com/SimpleITK/SimpleITK) for SimpleITK,
-   [Notebooks](https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks) for SimpleITK,
-   [Documentation](https://simpleitk.readthedocs.io/) for SimpleITK,
-   [nnU-Net](https://github.com/MIC-DKFZ/nnUNet),
-   [Combined (CT-MR) Healthy Abdominal Organ Segmentation](https://chaos.grand-challenge.org/Combined_Healthy_Abdominal_Organ_Segmentation/) (CHAOS) challenge,
-   Evaluation of segmentation results with [tools](https://github.com/emrekavur/CHAOS-evaluation) provided by organizers of CHAOS.

<!-- Definitions -->

[build]: <https://github.com/woctezuma/playing-with-simpleitk/actions>
[build-image]: <https://github.com/woctezuma/playing-with-simpleitk/workflows/build/badge.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/playing-with-simpleitk/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/playing-with-simpleitk/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/playing-with-simpleitk/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/playing-with-simpleitk>
[codecov-image]: <https://codecov.io/gh/woctezuma/playing-with-simpleitk/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/playing-with-simpleitk>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/df2510e9694b409d94ae5ddc36d7f75b>

[playing_with_pytorch]: <https://colab.research.google.com/github/woctezuma/playing-with-simpleitk/blob/master/playing_with_pytorch.ipynb>

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
