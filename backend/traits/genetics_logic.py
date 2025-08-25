# This dictionary stores the inheritance rules for each trait.
TRAITS_DATA = {
    # --- Original Traits ---
    'dimples': {
        'dominant_allele': 'D',
        'recessive_allele': 'd',
        'phenotypes': {
            'DD': 'Dimples',
            'Dd': 'Dimples',
            'dd': 'No Dimples'
        },
        'allele_map': {
            'Dimples': ['DD', 'Dd'],
            'No Dimples': ['dd']
        }
    },
    'earlobes': {
        'dominant_allele': 'E',
        'recessive_allele': 'e',
        'phenotypes': {
            'EE': 'Free Earlobes',
            'Ee': 'Free Earlobes',
            'ee': 'Attached Earlobes'
        },
        'allele_map': {
            'Free Earlobes': ['EE', 'Ee'],
            'Attached Earlobes': ['ee']
        }
    },
    'nose_shape': {
        'dominant_allele': 'N',
        'recessive_allele': 'n',
        'phenotypes': {
            'NN': 'Roman Nose',
            'Nn': 'Roman Nose',
            'nn': 'Straight Nose'
        },
        'allele_map': {
            'Roman Nose': ['NN', 'Nn'],
            'Straight Nose': ['nn']
        }
    },
    'height': {
        'dominant_allele': 'T',
        'recessive_allele': 't',
        'phenotypes': {
            'TT': 'Tall',
            'Tt': 'Tall',
            'tt': 'Short'
        },
        'allele_map': {
            'Tall': ['TT', 'Tt'],
            'Short': ['tt']
        }
    },
    'face_shape': {
        'dominant_allele': 'O',
        'recessive_allele': 'o',
        'phenotypes': {
            'OO': 'Oval Face',
            'Oo': 'Oval Face',
            'oo': 'Square Face'
        },
        'allele_map': {
            'Oval Face': ['OO', 'Oo'],
            'Square Face': ['oo']
        }
    },
    'pigmentation': {
        'dominant_allele': 'P',
        'recessive_allele': 'p',
        'phenotypes': {
            'PP': 'Normal Pigmentation',
            'Pp': 'Normal Pigmentation',
            'pp': 'Albinism'
        },
        'allele_map': {
            'Normal Pigmentation': ['PP', 'Pp'],
            'Albinism': ['pp']
        }
    },
    'hairline': {
        'dominant_allele': 'W',
        'recessive_allele': 'w',
        'phenotypes': {
            'WW': "Widow's Peak",
            'Ww': "Widow's Peak",
            'ww': 'Straight Hairline'
        },
        'allele_map': {
            "Widow's Peak": ['WW', 'Ww'],
            'Straight Hairline': ['ww']
        }
    },
    'tooth_gap': {
        'dominant_allele': 'G',
        'recessive_allele': 'g',
        'phenotypes': {
            'GG': 'Gap in Teeth',
            'Gg': 'Gap in Teeth',
            'gg': 'No Gap in Teeth'
        },
        'allele_map': {
            'Gap in Teeth': ['GG', 'Gg'],
            'No Gap in Teeth': ['gg']
        }
    },
    'head_shape': {
        'dominant_allele': 'R',
        'recessive_allele': 'r',
        'phenotypes': {
            'RR': 'Round Head',
            'Rr': 'Round Head',
            'rr': 'Long Head'
        },
        'allele_map': {
            'Round Head': ['RR', 'Rr'],
            'Long Head': ['rr']
        }
    },

    # --- Newly Added Traits ---
    'freckles': {
        'dominant_allele': 'F',
        'recessive_allele': 'f',
        'phenotypes': {
            'FF': 'Has Freckles',
            'Ff': 'Has Freckles',
            'ff': 'No Freckles'
        },
        'allele_map': {
            'Has Freckles': ['FF', 'Ff'],
            'No Freckles': ['ff']
        }
    },
    'cleft_chin': {
        'dominant_allele': 'C',
        'recessive_allele': 'c',
        'phenotypes': {
            'CC': 'Cleft Chin',
            'Cc': 'Cleft Chin',
            'cc': 'Smooth Chin'
        },
        'allele_map': {
            'Cleft Chin': ['CC', 'Cc'],
            'Smooth Chin': ['cc']
        }
    },
    'eyebrow_shape': {
        'dominant_allele': 'B',
        'recessive_allele': 'b',
        'phenotypes': {
            'BB': 'Connected Eyebrows',
            'Bb': 'Connected Eyebrows',
            'bb': 'Separated Eyebrows'
        },
        'allele_map': {
            'Connected Eyebrows': ['BB', 'Bb'],
            'Separated Eyebrows': ['bb']
        }
    },
    'eyelash_length': {
        'dominant_allele': 'L',
        'recessive_allele': 'l',
        'phenotypes': {
            'LL': 'Long Eyelashes',
            'Ll': 'Long Eyelashes',
            'll': 'Short Eyelashes'
        },
        'allele_map': {
            'Long Eyelashes': ['LL', 'Ll'],
            'Short Eyelashes': ['ll']
        }
    },
    'hair_texture': {
        'dominant_allele': 'H',
        'recessive_allele': 'h',
        'phenotypes': {
            'HH': 'Curly Hair',
            'Hh': 'Curly Hair',
            'hh': 'Straight Hair'
        },
        'allele_map': {
            'Curly Hair': ['HH', 'Hh'],
            'Straight Hair': ['hh']
        }
    },
    'hair_color': {
        'dominant_allele': 'K',
        'recessive_allele': 'k',
        'phenotypes': {
            'KK': 'Dark Hair',
            'Kk': 'Dark Hair',
            'kk': 'Light Hair'
        },
        'allele_map': {
            'Dark Hair': ['KK', 'Kk'],
            'Light Hair': ['kk']
        }
    },
    'finger_mid_digital_hair': {
        'dominant_allele': 'M',
        'recessive_allele': 'm',
        'phenotypes': {
            'MM': 'Has Mid-Digital Hair',
            'Mm': 'Has Mid-Digital Hair',
            'mm': 'No Mid-Digital Hair'
        },
        'allele_map': {
            'Has Mid-Digital Hair': ['MM', 'Mm'],
            'No Mid-Digital Hair': ['mm']
        }
    },
    'hitchhikers_thumb': {
        'dominant_allele': 'S',
        'recessive_allele': 's',
        'phenotypes': {
            'SS': 'Straight Thumb',
            'Ss': 'Straight Thumb',
            'ss': "Hitchhiker's Thumb"
        },
        'allele_map': {
            'Straight Thumb': ['SS', 'Ss'],
            "Hitchhiker's Thumb": ['ss']
        }
    },
    'tongue_rolling': {
        'dominant_allele': 'U',
        'recessive_allele': 'u',
        'phenotypes': {
            'UU': 'Can Roll Tongue',
            'Uu': 'Can Roll Tongue',
            'uu': 'Cannot Roll Tongue'
        },
        'allele_map': {
            'Can Roll Tongue': ['UU', 'Uu'],
            'Cannot Roll Tongue': ['uu']
        }
    },
    'handedness': {
        'dominant_allele': 'X',
        'recessive_allele': 'x',
        'phenotypes': {
            'XX': 'Right-Handed',
            'Xx': 'Right-Handed',
            'xx': 'Left-Handed'
        },
        'allele_map': {
            'Right-Handed': ['XX', 'Xx'],
            'Left-Handed': ['xx']
        }
    },
    'earwax_type': {
        'dominant_allele': 'Y',
        'recessive_allele': 'y',
        'phenotypes': {
            'YY': 'Wet Earwax',
            'Yy': 'Wet Earwax',
            'yy': 'Dry Earwax'
        },
        'allele_map': {
            'Wet Earwax': ['YY', 'Yy'],
            'Dry Earwax': ['yy']
        }
    }
}