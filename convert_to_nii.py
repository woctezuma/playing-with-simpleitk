import glob
from pathlib import Path

import SimpleITK as sitk

from data_input import get_patient_indices, get_path_to_ground_truth, get_path_to_image
from data_output import get_output_image_name
from utils import get_ground_truth_keyword


def convert_stack_of_slices_to_nii_image(patient_no,
                                         modality,  # either 'truth' or 'ct'
                                         input_file_format=None,
                                         output_file_format=None,
                                         data_root=None):
    if input_file_format is None:
        if modality == get_ground_truth_keyword():
            input_file_format = '.png'
        else:
            input_file_format = '.dcm'

    if output_file_format is None:
        output_file_format = '.nii.gz'

    if modality == get_ground_truth_keyword():
        input_directory = get_path_to_ground_truth(patient_no, data_root)
    else:
        input_directory = get_path_to_image(patient_no, data_root)

    output_file_name = get_output_image_name(patient_no, output_file_format, data_root, modality=modality)

    if Path(output_file_name).is_file():
        print('{} data is already processed for patient n°{}'.format(
            modality.capitalize(),
            patient_no
        ))

    else:
        print('Processing {} for patient n°{}'.format(
            modality,
            patient_no
        ))

        slice_file_list = glob.glob(input_directory + '*' + input_file_format)
        slice_file_list.sort()

        reader = sitk.ImageSeriesReader()

        reader.SetFileNames(slice_file_list)
        image = reader.Execute()

        sitk.WriteImage(image, output_file_name)

    return


def main(data_root=None):
    output_file_format = '.nii.gz'

    patient_indices = get_patient_indices(data_root=data_root)

    for modality in [get_ground_truth_keyword(),
                     'ct']:
        for patient_no in patient_indices:
            convert_stack_of_slices_to_nii_image(patient_no,
                                                 modality=modality,
                                                 output_file_format=output_file_format,
                                                 data_root=data_root)

    return True


if __name__ == '__main__':
    main()
