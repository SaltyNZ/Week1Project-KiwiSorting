import time
kiwidata = [2.049,2.398,2.009,1.809,2.894,2.054,2.927,2.848,2.246,1.971,2.432,2.739,2.256,3.167,2.289,2.462,2.044,1.951,2.455,3.719,2.586,1.644,2.994,2.5,2.331,2.21,3.101,2.204,2.289,2.633,2.675,2.47,2.253,1.67,3.142,2.799,2.686,2.159,3.101,2.457,2.542,2.758,2.933,2.299,2.563,3.017,2.908,3.116,2.505,2.125,2.33,2.141,3.138,2.297,2.713,2.662,3.668,3.453,2.48,2.612,3.445,2.302,2.461,2.168,3.397,2.371,2.835,1.824,2.691,2.506,2.853,2.794,2.572,3.471,2.026,2.896,3.222,2.454,1.905,2.322,2.411,1.679,2.817,2.549,2.206,2.418,2.914,3.822,3.27,2.258,3.294,2.745,2.643,3.313,2.057,2.393,2.389,2.377,2.102,3.26,2.135,2.929,2.387,2.787,2.367,1.959,2.414,3.436,2.172,3.033,2.085,2.213,2.834,1.61,2.89,2.612,2.702,3.128,2.536,2.702,2.239,2.186,2.363,2.922,2.01,3.096,2.923,2.003,2.159,2.922,1.604,2.548,2.532,2.438,2.187,3.714,3.503,1.878,2.317,2.952,2.884,2.2,2.878,2.567,3.556,3.484,2.249,2.747,2.424,1.882,2.884,3.176,2.673,1.825,2.341,2.328,2.162,2.74,2.205,2.516,3.02,2.663,2.623,2.222,2.405,2.402,3.026,2.333,2.147,2.734,3.194,2.512,1.96,2.482,2.004,2.281,3.084,2.157,2.175,1.862,2.552,2.253,2.991,2.795,1.947,2.695,2.693,1.663,2.573,2.414,1.834,3.128,1.652,2.5,2.271,3.012,3.674,2.018,2.959,2.44,2.993,2.694,2.099,2.641,3.237,3.387,2.585,3.595,1.826,3.143,2.717,2.239,3.21,1.591,2.13,3.007,2.418,3.074,2.117,2.274,2.021,3.021,2.773,2.188,1.95,2.321,2.567,2.029,3.322,2.88,3.218,2.086,2.157,2.369,3.232,3.458,2.087,2.488,2.485,2.338,2.246,2.045,2.615,2.767,2.722,2.89,2.431,2.396,3.022,2.716,1.886,1.965,2.844,3.06,2.399,2.612,1.831,2.414,2.721,3.183,2.384,4.143,2.837,3.452,2.203,1.921,2.952,3.504,2.389,2.371,2.193,3.102,3.522,2.526,2.753,2.198,2.079,3.58,2.364,1.88,3.05,2.429,2.006,2.889,2.274,2.081,2.449,2.573,2.339,3.155,3.578,2.687,2.816,3.226,2.182,3.111,2.638,1.957,2.403,2.681,2.732,2.899,2.39,3.353,3.239,1.93,2.748,3.291,2.256,2.044,3.454,3.105,2.204,2.841,2.041,2.276,2.912,3.139,2.475,2.604,2.395,2.313,2.271,2.749,2.461,2.093,3.249,3.749,2.874,2.687,2.846,3.283,2.749,3.677,2.35,2.009,2.244,2.388,2.285,3.381,2.429,2.603,2.312,3.002,3.518,3.079,2.301,2.653,2.834,2.723,2.904,2.842,2.033,1.916,2.259,3.45,1.689,2.621,2.15,2.372,2.958,2.81,2.981,2.508,2.53,2.924,1.675,3.249,3.773,2.133,2.486,3.063,2.486,4.008,2,2.497,1.921,2.353,1.987,2.339,2.735,2.225,3.127,2.353,2.817,2.384,2.195,1.822,2.264,3.491,2.705,2.455,2.579,1.796,2.469,2.691,3.522,3.294,2.384,2.465,3.119,3.213,3.591,2.404,2.857,2.014,3.163,3.573,2.662,2.008,2.22,1.836,2.287,2.841,3.309,2.257,3.156,2.596,2.772,2.647,2.441,2.59,3.314,2.186,2.898,2.751,2.992,2.905,2.426,3.332,2.548,2.502,2.915,3.134,3.386,2.874,2.716,2.349,2.251,2.148,2.337,2.796,3.35,2.869,2.229,2.165,1.928,2.535,2.421,2.905,2.517,3.206,2.246,2.563,2.659,3.115,2.549,2.243,3.94,2.878,2.266,2.471,3.267,3.391,2.232,2.65,2.245,3.306,2.674,2.059,2.435,2.064,2.124,2.54,2.768,1.959,3.392,3.089,3.497,2.014,2.065,3.854,2.993,2.133,3.446,2.631,3.274,2.929,2.101,2.368,2.292,2.254,3.481,1.916,2.541,2.994,2.45,3.656,2.294,3.29,3.142,2.028,2.191,2.173,2.871,2.522,2.221,2.629,2.665,2.017,1.718,2.16,2.708,2.62,2.559,2.312,3.136,2.103,3.504,2.096,2.757,2.557,2.768,2.095,2.303,2.298,3.374,2.602,2.909,2.936,2.291,2.696,2.468,3.186,1.758,3.311,2.417,2.004,2.142,2.587,2.073,2.39,2.699,3.335,2.716,2.528,2.19,2.96,2.201,2.421,1.948,1.979,2.435,1.97,2.797,2.538,2.868,2.849,3.045,2.755,3.317,3.005,3.347,2.511,2.975,3.187,3.416,2.195,2.159,2.331,2.361,2.195,2.687,2.29,2.66,2.405,2.842,2.982,2.155,1.689,2.016,3.226,2.312,3.046,2.425,2.863,2.468,2.915,2.702,3.417,2.24,2.469,2.29,2.216,2.806,2.41,2.122,3.206,2.109,3.234,3.16,3.074,2.363,2.093,2.488,2.857,3.147,2.084,2.992,2.304,3.111,2.604,2.312,2.486,3.029,2.958,2.093,2.986,1.999,2.34,2.508,3.185,2.596,2.092,2.598,2.176,2.501,1.923,3.298,2.898,2.485,2.171,2.297,2.159,2.177,2.317,2.076,2.271,1.984,2.25,2.61,3.266,2.152,2.544,3.448,2.967,2.237,3.272,2.46,2.282,2.103,1.884,2.94,2.654,2.797,2.022,3.02,2.247,1.57,2.573,2.72,2.151,2.095,2.033,2.494,3.114,2.661,2.05,3.413,2.489,1.824,2.722,2.79,2.335,2.179,3.07,2.297,2.68,2.638,2.784,2.653,2.625,2.177,2.575,3.937,1.996,2.444,3.519,2.424,2.818,2.011,2.393,2.156,3.19,2.436,2.309,2.414,2.49,2.953,3.695]
datalen = len(kiwidata)


start_time = time.time()
for i in range(datalen):

    minimum = i
    for j in range(i+1, datalen):
        if kiwidata[minimum] > kiwidata[j]:
            minimum = j



    kiwidata[i], kiwidata[minimum] = kiwidata[minimum], kiwidata[i]
end_time = time.time()

print(kiwidata)
print(end_time - start_time)