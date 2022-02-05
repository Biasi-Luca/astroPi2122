import numpy as np
from numpy import uint8

fastiecm = np.array([[[255, 255, 255]],

       [[250, 250, 250]],

       [[245, 245, 245]],

       [[241, 241, 241]],

       [[237, 237, 237]],

       [[232, 232, 232]],

       [[228, 228, 228]],

       [[225, 225, 225]],

       [[221, 221, 221]],

       [[216, 216, 216]],

       [[212, 212, 212]],

       [[208, 208, 208]],

       [[204, 204, 204]],

       [[199, 199, 199]],

       [[194, 194, 194]],

       [[190, 190, 190]],

       [[186, 186, 186]],

       [[182, 182, 182]],

       [[177, 177, 177]],

       [[174, 174, 174]],

       [[170, 170, 170]],

       [[166, 166, 166]],

       [[161, 161, 161]],

       [[157, 157, 157]],

       [[153, 153, 153]],

       [[148, 148, 148]],

       [[144, 144, 144]],

       [[139, 139, 139]],

       [[135, 135, 135]],

       [[131, 131, 131]],

       [[128, 128, 128]],

       [[123, 123, 123]],

       [[119, 119, 119]],

       [[115, 115, 115]],

       [[111, 111, 111]],

       [[106, 106, 106]],

       [[102, 102, 102]],

       [[ 97,  97,  97]],

       [[ 93,  93,  93]],

       [[ 89,  89,  89]],

       [[ 84,  84,  84]],

       [[ 80,  80,  80]],

       [[ 77,  77,  77]],

       [[ 73,  73,  73]],

       [[ 68,  68,  68]],

       [[ 64,  64,  64]],

       [[ 60,  60,  60]],

       [[ 55,  55,  55]],

       [[ 51,  51,  51]],

       [[ 55,  55,  55]],

       [[ 60,  60,  60]],

       [[ 64,  64,  64]],

       [[ 68,  68,  68]],

       [[ 73,  73,  73]],

       [[ 77,  77,  77]],

       [[ 80,  80,  80]],

       [[ 84,  84,  84]],

       [[ 89,  89,  89]],

       [[ 93,  93,  93]],

       [[ 97,  97,  97]],

       [[102, 102, 102]],

       [[106, 106, 106]],

       [[111, 111, 111]],

       [[115, 115, 115]],

       [[119, 119, 119]],

       [[123, 123, 123]],

       [[128, 128, 128]],

       [[131, 131, 131]],

       [[135, 135, 135]],

       [[139, 139, 139]],

       [[144, 144, 144]],

       [[148, 148, 148]],

       [[153, 153, 153]],

       [[157, 157, 157]],

       [[161, 161, 161]],

       [[166, 166, 166]],

       [[170, 170, 170]],

       [[174, 174, 174]],

       [[177, 177, 177]],

       [[182, 182, 182]],

       [[186, 186, 186]],

       [[190, 190, 190]],

       [[194, 194, 194]],

       [[199, 199, 199]],

       [[204, 204, 204]],

       [[208, 208, 208]],

       [[212, 212, 212]],

       [[216, 216, 216]],

       [[221, 221, 221]],

       [[225, 225, 225]],

       [[228, 228, 228]],

       [[232, 232, 232]],

       [[237, 237, 237]],

       [[241, 241, 241]],

       [[245, 245, 245]],

       [[250, 250, 250]],

       [[255, 255, 255]],

       [[250, 250, 250]],

       [[245, 245, 245]],

       [[240, 240, 240]],

       [[235, 235, 235]],

       [[230, 230, 230]],

       [[225, 225, 225]],

       [[219, 219, 219]],

       [[214, 214, 214]],

       [[209, 209, 209]],

       [[204, 204, 204]],

       [[199, 199, 199]],

       [[194, 194, 194]],

       [[190, 190, 190]],

       [[185, 185, 185]],

       [[180, 180, 180]],

       [[175, 175, 175]],

       [[170, 170, 170]],

       [[165, 165, 165]],

       [[160, 160, 160]],

       [[154, 154, 154]],

       [[151, 151, 151]],

       [[145, 145, 145]],

       [[140, 140, 140]],

       [[135, 135, 135]],

       [[130, 130, 130]],

       [[125, 125, 125]],

       [[120, 120, 120]],

       [[115, 115, 115]],

       [[111, 111, 111]],

       [[106, 106, 106]],

       [[101, 101, 101]],

       [[ 96,  96,  96]],

       [[ 91,  91,  91]],

       [[ 86,  86,  86]],

       [[ 80,  80,  80]],

       [[ 75,  75,  75]],

       [[ 70,  70,  70]],

       [[ 65,  65,  65]],

       [[ 60,  60,  60]],

       [[ 55,  55,  55]],

       [[ 79,  65,  65]],

       [[105,  77,  77]],

       [[129,  87,  87]],

       [[154,  97,  97]],

       [[180, 107, 107]],

       [[204, 119, 119]],

       [[230, 129, 129]],

       [[255, 139, 139]],

       [[239, 147, 130]],

       [[222, 153, 121]],

       [[207, 161, 112]],

       [[190, 167, 105]],

       [[175, 175,  96]],

       [[158, 182,  87]],

       [[143, 190,  78]],

       [[126, 196,  69]],

       [[111, 204,  60]],

       [[ 94, 211,  51]],

       [[ 78, 218,  42]],

       [[ 63, 226,  35]],

       [[ 46, 232,  26]],

       [[ 31, 240,  17]],

       [[ 14, 246,   8]],

       [[  0, 255,   0]],

       [[  0, 255,   7]],

       [[  0, 255,  14]],

       [[  0, 255,  23]],

       [[  0, 255,  31]],

       [[  0, 255,  38]],

       [[  0, 255,  46]],

       [[  0, 255,  55]],

       [[  0, 255,  63]],

       [[  0, 255,  70]],

       [[  0, 255,  78]],

       [[  0, 255,  87]],

       [[  0, 255,  94]],

       [[  0, 255, 102]],

       [[  0, 255, 111]],

       [[  0, 255, 119]],

       [[  0, 255, 126]],

       [[  0, 255, 134]],

       [[  0, 255, 143]],

       [[  0, 255, 151]],

       [[  0, 255, 158]],

       [[  0, 255, 166]],

       [[  0, 255, 175]],

       [[  0, 255, 182]],

       [[  0, 255, 190]],

       [[  0, 255, 199]],

       [[  0, 255, 207]],

       [[  0, 255, 214]],

       [[  0, 255, 222]],

       [[  0, 255, 231]],

       [[  0, 255, 239]],

       [[  0, 255, 246]],

       [[  0, 255, 255]],

       [[  0, 249, 255]],

       [[  0, 244, 255]],

       [[  0, 239, 255]],

       [[  0, 232, 255]],

       [[  0, 227, 255]],

       [[  0, 222, 255]],

       [[  0, 217, 255]],

       [[  0, 212, 255]],

       [[  0, 207, 255]],

       [[  0, 200, 255]],

       [[  0, 195, 255]],

       [[  0, 190, 255]],

       [[  0, 185, 255]],

       [[  0, 180, 255]],

       [[  0, 175, 255]],

       [[  0, 170, 255]],

       [[  0, 163, 255]],

       [[  0, 158, 255]],

       [[  0, 153, 255]],

       [[  0, 148, 255]],

       [[  0, 143, 255]],

       [[  0, 138, 255]],

       [[  0, 131, 255]],

       [[  0, 126, 255]],

       [[  0, 121, 255]],

       [[  0, 115, 255]],

       [[  0, 111, 255]],

       [[  0, 106, 255]],

       [[  0, 100, 255]],

       [[  0,  94, 255]],

       [[  0,  89, 255]],

       [[  0,  84, 255]],

       [[  0,  78, 255]],

       [[  0,  74, 255]],

       [[  0,  69, 255]],

       [[  0,  63, 255]],

       [[  0,  58, 255]],

       [[  0,  52, 255]],

       [[  0,  46, 255]],

       [[  0,  41, 255]],

       [[  0,  37, 255]],

       [[  0,  31, 255]],

       [[  0,  26, 255]],

       [[  0,  21, 255]],

       [[  0,  14, 255]],

       [[  0,   9, 255]],

       [[  0,   4, 255]],

       [[  0,   0, 255]],

       [[ 14,   0, 255]],

       [[ 31,   0, 255]],

       [[ 46,   0, 255]],

       [[ 63,   0, 255]],

       [[ 78,   0, 255]],

       [[ 94,   0, 255]],

       [[111,   0, 255]],

       [[126,   0, 255]],

       [[143,   0, 255]],

       [[158,   0, 255]],

       [[175,   0, 255]],

       [[190,   0, 255]],

       [[207,   0, 255]],

       [[222,   0, 255]],
       [[239, 0 ,255]]], dtype=uint8)