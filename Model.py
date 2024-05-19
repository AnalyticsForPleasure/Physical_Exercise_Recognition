import pandas as pd

# This dataset represents sequential poses that can be used to distinguish 5 physical exercises.
# The exercises are:
# Push-up,
# Pull-up,
# Sit-up,
# Jumping Jack
# Squat
# The dataset consists of 33 landmarks that
# represents several important body parts' positions. Using these landmarks, the angles and the distances between
# several landmarks are calculated and included in the dataset. The sequence of the poses is provided by preserving
# the frame order in every record.


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    pd.set_option('display.max_columns', 50)




    df_labels = pd.read_csv('/home/shay_diy/PycharmProjects/Physical_Exercise_Recognition/Data/labels.csv')
    df_3d = pd.read_csv('/home/shay_diy/PycharmProjects/Physical_Exercise_Recognition/Data/calculated_3d_distances.csv', nrows= 100)
    df_landmarks = pd.read_csv('/home/shay_diy/PycharmProjects/Physical_Exercise_Recognition/Data/landmarks.csv',nrows= 100)
    df_xyz =pd.read_csv('/home/shay_diy/PycharmProjects/Physical_Exercise_Recognition/Data/xyz_distances.csv')
    df_angles = pd.read_csv('/home/shay_diy/PycharmProjects/Physical_Exercise_Recognition/Data/angles.csv')

    print(f'columns are: {df_labels.columns}')
    print('*')


    # Finding the inber of vid_id in each class activity :

    list_of_activities = pd.unique(df_labels['class'])

    for activity in list_of_activities:
        res =df_labels.loc[df_labels['class'] == activity , :]
        number_of_row_each_activity = res.shape[0]
        print('*')


