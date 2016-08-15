import os
import pandas as pd

msit_files = [f for f in os.listdir(".") if
              os.path.isfile(os.path.join(".", f)) and "control_task" in f.lower() and f.endswith("csv")]

# dictionary that we will use to hold all of our stats
msit_stats_df = pd.DataFrame(columns=('id', 'congruent_correct', 'congruent_rt_mean', 'congruent_rt_var',
                                      'incongruent_correct', 'incongruent_rt_mean', 'incongruent_rt_var'))

for file in msit_files:
    msit_data = pd.read_table(file, sep=",", header=0)
    pt_id = '_'.join(file.split('_')[0:2])

    if pd.isnull(msit_stats_df.index.max()):
        new_idx = 0
    else:
        new_idx = msit_stats_df.index.max() + 1

    try:
        congruent_correct = float((msit_data["first_resp.corr"] == 1).sum()) / float(
            (msit_data["first_resp.corr"] == 1).sum() + (msit_data["first_resp.corr"] == 0).sum())
        congruent_rt_mean = msit_data["first_resp.rt"][msit_data["first_resp.corr"] == 1].mean()
        congruent_rt_var = msit_data["first_resp.rt"][msit_data["first_resp.corr"] == 1].var()
    except:
        print "could not find first_resp.corr in ", file, msit_data.columns
        print "skipping... "
        continue

    try:
        incongruent_correct = float((msit_data["second_response.corr"] == 1).sum()) / float(
            (msit_data["second_response.corr"] == 1).sum() + (msit_data["second_response.corr"] == 0).sum())
        incongruent_rt_mean = msit_data["second_response.rt"][msit_data["second_response.corr"] == 1].mean()
        incongruent_rt_var = msit_data["second_response.rt"][msit_data["second_response.corr"] == 1].var()
    except:
        print "could not find second_response.corr in ", file, msit_data.columns
        print "skipping... "
        continue

    msit_stats_df.loc[new_idx] = [pt_id, congruent_correct, congruent_rt_mean, congruent_rt_var, incongruent_correct,
                                  incongruent_rt_mean, incongruent_rt_var]

msit_stats_df.to_csv("msit_stats.csv")
