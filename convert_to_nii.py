import glob
from pathlib import Path

import SimpleITK as sitk


def get_data_root():
    data_root = 'data/'

    return data_root


def get_data_path(data_root=None):
    # Data downloaded from:
    #   https://chaos.grand-challenge.org/Combined_Healthy_Abdominal_Organ_Segmentation/

    if data_root is None:
        data_root = get_data_root()

    data_path = data_root + 'Train_Sets/'

    return data_path


def get_definition_file_name(data_root=None):
    definition_file_name = get_data_path(data_root) + 'definitions.txt'

    return definition_file_name


def get_patient_indices(verbose=True, data_root=None):
    definition_file_name = get_definition_file_name(data_root)

    with open(definition_file_name, 'r') as f:
        lines = f.readlines()

    patient_indices_as_str = lines[1]

    patient_indices = [int(patient_no)
                       for patient_no in patient_indices_as_str.split(',')]

    if verbose:
        print('{} patients found: {}'.format(
            len(patient_indices),
            patient_indices
        ))

    return patient_indices


def get_patient_data_path(patient_no, data_root=None):
    patient_data_path = get_data_path(data_root) + 'CT/' + str(patient_no) + '/'

    return patient_data_path


def get_path_to_image(patient_no, data_root=None):
    path_to_image = get_patient_data_path(patient_no, data_root) + '/DICOM_anon/'

    return path_to_image


def get_path_to_ground_truth(patient_no, data_root=None):
    path_to_ground_truth = get_patient_data_path(patient_no, data_root) + 'Ground/'

    return path_to_ground_truth


def get_output_folder(data_root=None):
    if data_root is None:
        data_root = get_data_root()

    output_folder = data_root + 'output/'

    Path(output_folder).mkdir(exist_ok=True)

    return output_folder


def get_output_image_name(patient_no, output_file_format, data_root=None):
    output_folder = get_output_folder(data_root)
    output_image_name = output_folder + str(patient_no) + output_file_format

    return output_image_name


def get_ground_truth_suffix():
    ground_truth_suffix = '_gt'

    return ground_truth_suffix


def get_output_ground_truth_name(patient_no, output_file_format, data_root=None):
    output_folder = get_output_folder(data_root)
    output_ground_truth_name = output_folder + str(patient_no) + get_ground_truth_suffix() + output_file_format

    return output_ground_truth_name


def convert_stack_of_slices_to_nii_image(patient_no,
                                         keyword,  # either 'images' or 'ground truth'
                                         input_file_format=None,
                                         output_file_format=None,
                                         data_root=None):
    if input_file_format is None:
        if keyword == 'images':
            input_file_format = '.dcm'
        else:
            input_file_format = '.png'

    if input_file_format is None:
        output_file_format = '.nii.gz'

    if keyword == 'images':
        input_directory = get_path_to_image(patient_no, data_root)
        output_file_name = get_output_image_name(patient_no, output_file_format, data_root)
    else:
        input_directory = get_path_to_ground_truth(patient_no, data_root)
        output_file_name = get_output_ground_truth_name(patient_no, output_file_format, data_root)

    if Path(output_file_name).is_file():
        print('{} data is already processed for patient n°{}'.format(
            keyword.capitalize(),
            patient_no
        ))

    else:
        print('Processing {} for patient n°{}'.format(
            keyword,
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

    for keyword in ['images', 'ground truth']:
        for patient_no in patient_indices:
            convert_stack_of_slices_to_nii_image(patient_no,
                                                 keyword=keyword,
                                                 output_file_format=output_file_format,
                                                 data_root=data_root)

    return True


if __name__ == '__main__':
    main()
