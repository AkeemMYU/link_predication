# get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
results_dict = {'5': {0: {'cn': 0.9511916666666667, 'jc': 0.798475, 'ra': 0.9697, 'aa': 0.9597166666666667, 'pa': 0.44914166666666666, 'katz': 0.9559833333333333},
                      1: {'cn': 0.595325, 'jc': 0.5426416666666667, 'ra': 0.6828583333333333, 'aa': 0.5844833333333334, 'pa': 0.403925, 'katz': 0.710275},
                      2: {'cn': 0.9228416666666667, 'jc': 0.8245833333333333, 'ra': 0.93765, 'aa': 0.8135, 'pa': 0.46121666666666666, 'katz': 0.9142583333333333},
                      3: {'cn': 0.9668, 'jc': 0.90565, 'ra': 0.963975, 'aa': 0.8638083333333333, 'pa': 0.4587583333333333, 'katz': 0.9669666666666666},
                      4: {'cn': 0.9766, 'jc': 0.9285833333333333, 'ra': 0.9828666666666667, 'aa': 0.8691, 'pa': 0.34524166666666667, 'katz': 0.9731583333333333},
                      5: {'cn': 0.8862083333333334, 'jc': 0.8137833333333333, 'ra': 0.8882916666666667, 'aa': 0.8063333333333333, 'pa': 0.4421583333333333, 'katz': 0.878275},
                      6: {'cn': 0.9681, 'jc': 0.9111083333333333, 'ra': 0.9704416666666666, 'aa': 0.864275, 'pa': 0.41634166666666667, 'katz': 0.9665833333333333},
                      7: {'cn': 0.903175, 'jc': 0.8281083333333333, 'ra': 0.92405, 'aa': 0.8066416666666667, 'pa': 0.473425, 'katz': 0.9075166666666666},
                      8: {'cn': 0.9248333333333333, 'jc': 0.8436416666666666, 'ra': 0.9416333333333333, 'aa': 0.83145, 'pa': 0.3761583333333333, 'katz': 0.9320083333333333},
                      9: {'cn': 0.965775, 'jc': 0.9066916666666667, 'ra': 0.95775, 'aa': 0.867575, 'pa': 0.38866666666666666, 'katz': 0.966675},
                      10: {'cn': 0.8801833333333333, 'jc': 0.817625, 'ra': 0.9045416666666667, 'aa': 0.8004333333333333, 'pa': 0.4792666666666667, 'katz': 0.8967333333333334},
                      11: {'cn': 0.94305, 'jc': 0.8706666666666667, 'ra': 0.961175, 'aa': 0.848925, 'pa': 0.4861083333333333, 'katz': 0.9473},
                      12: {'cn': 0.8365916666666666, 'jc': 0.7392, 'ra': 0.8587833333333333, 'aa': 0.767575, 'pa': 0.5414, 'katz': 0.8683166666666666},
                      13: {'cn': 0.8381416666666667, 'jc': 0.7674166666666666, 'ra': 0.8830083333333333, 'aa': 0.7834083333333334, 'pa': 0.5196166666666666, 'katz': 0.8076083333333334},
                      14: {'cn': 0.7875333333333333, 'jc': 0.7197, 'ra': 0.7807916666666667, 'aa': 0.7464916666666667, 'pa': 0.4805333333333333, 'katz': 0.7387416666666666},
                      15: {'cn': 0.702775, 'jc': 0.6088416666666666, 'ra': 0.7360916666666667, 'aa': 0.6622333333333333, 'pa': 0.43159166666666665, 'katz': 0.6263916666666667},
                      16: {'cn': 0.6342916666666667, 'jc': 0.5688083333333334, 'ra': 0.6848, 'aa': 0.6123833333333333, 'pa': 0.44330833333333336, 'katz': 0.5609},
                      17: {'cn': 0.6617916666666667, 'jc': 0.6303416666666667, 'ra': 0.7112333333333334, 'aa': 0.6869833333333333, 'pa': 0.50895, 'katz': 0.5870416666666667},
                      18: {'cn': 0.5914, 'jc': 0.5828166666666666, 'ra': 0.67785, 'aa': 0.5875916666666666, 'pa': 0.3875, 'katz': 0.4668583333333333},
                      19: {'cn': 0.5537333333333333, 'jc': 0.5664666666666667, 'ra': 0.6510833333333333, 'aa': 0.5686083333333334, 'pa': 0.33021666666666666, 'katz': 0.40973333333333334}},
                '10': {0: {'cn': 0.7676666666666667, 'jc': 0.7103916666666666, 'ra': 0.8012333333333334, 'aa': 0.7862583333333333, 'pa': 0.40579166666666666, 'katz': 0.8320833333333333},
                       1: {'cn': 0.8855, 'jc': 0.8142166666666667, 'ra': 0.9109666666666667, 'aa': 0.79445, 'pa': 0.416575, 'katz': 0.9086416666666667},
                       2: {'cn': 0.919, 'jc': 0.8604833333333334, 'ra': 0.9333666666666667, 'aa': 0.8238583333333334, 'pa': 0.4099, 'katz': 0.9193083333333333},
                       3: {'cn': 0.9362416666666666, 'jc': 0.8745083333333333, 'ra': 0.9474166666666667, 'aa': 0.838175, 'pa': 0.46324166666666666, 'katz': 0.9382166666666667},
                       4: {'cn': 0.9375, 'jc': 0.85935, 'ra': 0.949075, 'aa': 0.8336666666666667, 'pa': 0.43915, 'katz': 0.94225},
                       5: {'cn': 0.9153, 'jc': 0.843225, 'ra': 0.9314916666666667, 'aa': 0.8315583333333333, 'pa': 0.4442, 'katz': 0.9222666666666667},
                       6: {'cn': 0.8242083333333333, 'jc': 0.7358666666666667, 'ra': 0.8571416666666667, 'aa': 0.768475, 'pa': 0.5265583333333334, 'katz': 0.8247},
                       7: {'cn': 0.747575, 'jc': 0.717475, 'ra': 0.758675, 'aa': 0.7576333333333334, 'pa': 0.4671666666666667, 'katz': 0.688525},
                       8: {'cn': 0.63175, 'jc': 0.6126833333333334, 'ra': 0.6569083333333333, 'aa': 0.6498, 'pa': 0.4429916666666667, 'katz': 0.54425},
                       9: {'cn': 0.5593583333333333, 'jc': 0.58345, 'ra': 0.610775, 'aa': 0.58405, 'pa': 0.40818333333333334, 'katz': 0.44745833333333335}},
                '15': {0: {'cn': 0.740825, 'jc': 0.7003083333333333, 'ra': 0.7635416666666667, 'aa': 0.7539833333333333, 'pa': 0.429325, 'katz': 0.8094583333333333},
                       1: {'cn': 0.9134916666666667, 'jc': 0.8424083333333333, 'ra': 0.9111833333333333, 'aa': 0.8263333333333334, 'pa': 0.4249833333333333, 'katz': 0.915075},
                       2: {'cn': 0.931625, 'jc': 0.863325, 'ra': 0.943475, 'aa': 0.8366833333333333, 'pa': 0.4318416666666667, 'katz': 0.9368916666666667},
                       3: {'cn': 0.9063333333333333, 'jc': 0.8389833333333333, 'ra': 0.9266833333333333, 'aa': 0.8263166666666667, 'pa': 0.4616166666666667, 'katz': 0.9209916666666667},
                       4: {'cn': 0.8018833333333333, 'jc': 0.75885, 'ra': 0.8193, 'aa': 0.8142333333333334, 'pa': 0.49030833333333335, 'katz': 0.7819083333333333},
                       5: {'cn': 0.7153583333333333, 'jc': 0.6932083333333333, 'ra': 0.732925, 'aa': 0.7288833333333333, 'pa': 0.4536833333333333, 'katz': 0.645775},
                       6: {'cn': 0.59395, 'jc': 0.6058916666666667, 'ra': 0.6300666666666667, 'aa': 0.6117666666666667, 'pa': 0.46465, 'katz': 0.5033916666666667}},
                '20': {0: {'cn': 0.7795333333333333, 'jc': 0.7481083333333334, 'ra': 0.7988, 'aa': 0.7919916666666666, 'pa': 0.534775, 'katz': 0.8445583333333333},
                       1: {'cn': 0.9311583333333333, 'jc': 0.8677916666666666, 'ra': 0.9395166666666667, 'aa': 0.836725, 'pa': 0.4277416666666667, 'katz': 0.9317916666666667},
                       2: {'cn': 0.9114916666666667, 'jc': 0.8605, 'ra': 0.9213333333333333, 'aa': 0.9203666666666667, 'pa': 0.4815833333333333, 'katz': 0.9212166666666667},
                       3: {'cn': 0.7934916666666667, 'jc': 0.753675, 'ra': 0.8048583333333333, 'aa': 0.8025833333333333, 'pa': 0.5246833333333333, 'katz': 0.7658833333333334},
                       4: {'cn': 0.5767, 'jc': 0.5775666666666667, 'ra': 0.5899916666666667, 'aa': 0.5840666666666666, 'pa': 0.46208333333333335, 'katz': 0.5047083333333333}}}


def plot_avg_and_std(ndarray, x_label):
    avg = np.mean(ndarray, axis=0)
    std = np.std(ndarray, axis=0)
    plt.title('USAir')
    plt.ylim(0, 1.1)
    plt.Line2D()
    plt.errorbar(x_label, avg, std, linestyle='None', marker='^')
    plt.show()


def plot_size_of_probe_set():
    plt.title('USAir')
    plt.ylim(0, 1.1)
    plt.ylabel('AUC')
    
    plt.xlabel('size of probe set / %')
    x_label = [5, 10, 15, 20]
    plt.xticks(x_label)
    plt.plot(x_label, [0.8245170833333333, 0.8124100000000001,
                               0.8405200000000002, 0.798475], linewidth=1.0, marker='^', label='cn')  # cn
    plt.plot(x_label, [0.7587575, 0.761165,
                               0.7954462499999999, 0.7615283333333334], linewidth=1.0, marker='^', label='jc')  # jc
    plt.plot(x_label, [0.85342875, 0.8357049999999999,
                               0.85907625, 0.8109], linewidth=1.0, marker='^', label='ra')  # ra
    plt.plot(x_label, [0.7665758333333335, 0.7667925,
                               0.80973, 0.7871466666666667], linewidth=1.0, marker='^', label='aa')  # aa
    plt.plot(x_label, [0.44117625, 0.44237583333333336,
                               0.47346124999999994, 0.48617333333333324], linewidth=1.0, marker='^', label='pa')  # pa
    plt.plot(x_label, [0.80406625, 0.79677, 0.8270237499999998,
                               0.7936316666666666], linewidth=1.0, marker='^', label='katz')  # katz
    plt.legend()
    plt.show()


def dict_to_array(results_dict):
    for key, value in results_dict.items():
        dataset_name, fold_dict = key, value
        method_names = list(fold_dict[0].keys())
        results_array = []
        for k, v in fold_dict.items():
            result = []
            for _, res in v.items():
                result.append(res)
            results_array.append(result)
        results_array = np.asarray(results_array)

        return dataset_name, results_array, method_names


def diff_method(results_dict):
    x_label = []
    for key, value in results_dict.items():
        x_label.append(int(key))
        method = list(value[0].keys())
        V = Counter({})
        for k, v in value.items():
            V += Counter(v)
        V = dict(V)
        for k, v in V.items():
            V[k] /= (100/int(key))
    print(x_label)
    print(V)
    return x_label, V


plot_size_of_probe_set()
