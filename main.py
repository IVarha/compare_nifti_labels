# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import nibabel as nib
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #functions
    dice_f = lambda x, y: 2 * (x & y).sum() / (x.sum() + y.sum())
    jac_f = lambda x, y:  (x & y).sum() / (x | y).sum()

    train_subjects_file = sys.argv[1]
    labels_subjects_file = sys.argv[2]

    label_file = nib.load(train_subjects_file)
    true_file = nib.load(labels_subjects_file)

    label_img = label_file.get_fdata()

    true_img = true_file.get_fdata()

    true_img = true_img.astype(np.int32)
    setel = np.unique(true_img)
    setel = setel[setel != 0]
    for i in range(setel.shape[0]):
        arr_true = true_img == setel[i]
        arr_label = label_img.astype(np.int32) == setel[i]
        print(dice_f(arr_label,arr_true))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
