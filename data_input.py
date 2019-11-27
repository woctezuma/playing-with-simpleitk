# Data downloaded from:
#   https://chaos.grand-challenge.org/Combined_Healthy_Abdominal_Organ_Segmentation/

from utils import get_data_root


def get_data_path(data_root=None):
    if data_root is None:
        data_root = get_data_root()

    data_path = data_root + 'Train_Sets/'

    return data_path


def get_definition_file_name(data_root=None):
    definition_file_name = get_data_path(data_root) + 'definitions.txt'

    return definition_file_name


def get_patient_indices(data_root=None,
                        verbose=True):
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


def get_patient_data_path(patient_no,
                          data_root=None):
    patient_data_path = get_data_path(data_root) + 'CT/' + str(patient_no) + '/'

    return patient_data_path


def get_path_to_image(patient_no,
                      data_root=None):
    path_to_image = get_patient_data_path(patient_no, data_root) + '/DICOM_anon/'

    return path_to_image


def get_path_to_ground_truth(patient_no,
                             data_root=None):
    path_to_ground_truth = get_patient_data_path(patient_no, data_root) + 'Ground/'

    return path_to_ground_truth


def main():
    return True


if __name__ == '__main__':
    main()
