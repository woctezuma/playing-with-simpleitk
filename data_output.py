from pathlib import Path

from utils import get_data_root, get_ground_truth_keyword


def get_image_modality_convention_dict():
    # We index each modality used in our dataset.

    modality_dict = dict()
    modality_dict['ct'] = 1

    return modality_dict


def get_output_save_folder():
    # This is the folder where the output will be saved.

    output_save_folder = 'output/'

    return output_save_folder


def get_output_folder_structure():
    # Convention used in:
    #   https://github.com/MIC-DKFZ/nnUNet/tree/master/nnunet/dataset_conversion

    output_folder_structure = dict()

    output_folder_structure['training'] = dict()
    output_folder_structure['training']['images'] = 'imagesTr/'
    output_folder_structure['training']['ground_truth'] = 'labelsTr/'

    output_folder_structure['test'] = dict()
    output_folder_structure['test']['images'] = 'imagesTs/'

    return output_folder_structure


def get_image_modality_convention(modality):
    # Convention used in:
    #   https://github.com/MIC-DKFZ/nnUNet/tree/master/nnunet/dataset_conversion

    modality_dict = get_image_modality_convention_dict()

    try:
        modality_no = modality_dict[modality]
        image_modality_convention = '_{:04.0f}'.format(modality_no)
    except (KeyError, TypeError) as e:
        image_modality_convention = ''

    return image_modality_convention


def get_data_file_prefix():
    # Convention used in:
    #   https://github.com/MIC-DKFZ/nnUNet/tree/master/nnunet/dataset_conversion

    data_file_prefix = 'patientID'

    return data_file_prefix


def get_output_folder(data_root=None,
                      modality=None):
    if data_root is None:
        data_root = get_data_root()

    output_folder_structure = get_output_folder_structure()

    if modality is None:
        folder = ''
    elif modality == get_ground_truth_keyword():
        folder = output_folder_structure['training']['ground_truth']
    else:
        folder = output_folder_structure['training']['images']

    output_folder = data_root + get_output_save_folder() + folder

    Path(output_folder).mkdir(parents=True, exist_ok=True)

    return output_folder


def get_output_image_name(patient_no,
                          output_file_format,
                          data_root=None,
                          modality=None):
    output_folder = get_output_folder(data_root, modality=modality)

    file_name = get_data_file_prefix() + str(patient_no) + get_image_modality_convention(modality) + output_file_format

    output_image_name = output_folder + file_name

    return output_image_name


def main():
    return True


if __name__ == '__main__':
    main()
