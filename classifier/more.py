#encoding: utf-8

def pos_features(sentence , i):
    features = {"auffix(1)":sentence[i][-1:],
                "auffix(2)":sentence[i][-2:],
                "auffix(3)":sentence[i][-3:]
                }
    if i==0:
        features["prev_word"] = "<start>"
    else:
        features["prev_word"] = sentence[i-1]
    return features