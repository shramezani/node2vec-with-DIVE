import json


def save_word_emb_to_dic(filename):
    file = open(filename, "r")
    text = file.read()
    text = text.split("\n")[0:-1]
    text[0] = text[0].split(' ')
    print text[0]
    for i in range(1, len(text)):
        text[i] = text[i].split(" ")[0:-1]
    file.close()
    print("text splitted")
    return text[2:]


def save_word_emb(from_file_path, to_file_path):
    print(from_file_path)
    text = save_word_emb_to_dic(from_file_path)
    formatted_emb = {}
    for i in range(1, len(text)):
        # print(i)
        emb = {}
        for dim in range(1, len(text[i])):
            v = (text[i][dim])
            v = float(v)

            # vectors___init2_context_D_50_S_5_K_03
            # vectors___init2_context_D_50_S_0_K_03
            # vectors___init2_context_D_10_S_5_K_03
            # vectors___init2_context_D_70_S_4_K_03
            # vectors___init2_context_D_70_S_5_K_03
            # vectors___init2_context_D_70_S_5_K_1_point_5
            # vectors___init2_context_D_50_S_3_K_1_point_5
            # vectors___init1_context_D_50_S_3_K_1_point_5
            # vectors___init1_context_D_20_S_4_K_1_point_5
            # vectors___init2_context_D_20_S_5_K_1_point_5
            # vectors___init2_context_D_50_S_5_K_1_point_5
            # vectors___init1_context_D_50_S_5_K_1_point_5
            # vectors___context_D_50_S_4_K_1_point_5
            # vectors___context_D_70_S_4_K_1_point_5
            # vectors___context_D_50_S_5_K_1_point_5
            # vectors___context_D_70_S_5_K_1_point_5
            # vectors___context_D_70_S_3_K_1_point_5
            if v !=0: emb[str(dim)] = v
            # vectors___context_D_50_S_3_K_03
            # if v >= 0.0008: emb[str(dim)] = v

            # vectors___context_D_50_S_4_K_03
            # if v >= 0.001: emb[str(dim)] = v

            # vectors__context_D_10_S_4_K_03
            # if v >= 1.25: emb[str(dim)] = v

            # vectors__context_D_10_S_3_K_03
            # if v >= 1.2: emb[str(dim)] = v

            # vectors__context_D_20_S_5_K_03
            # if v >= 1.11: emb[str(dim)] = v

            # vectors__context_D_20_S_3_K_03
            # if v >= 1.11: emb[str(dim)] = v

            # vectors__context_D_20_S_4_K_03
            # if v >= 1.15: emb[str(dim)] = v

            # vectors__target_over_V_10_S_6_K_03
            # if v >=0.88: emb[str(dim)] = v

            # vectors__target_over_V_10_S_3_K_03
            # if v >= 0.001: emb[str(dim)] = v

            # vectors__target_over_V_15_S_4_K_03
            # if v >= 0.0006: emb[str(dim)] = v

            # vectors__target_over_V_15_S_6_K_03
            # if v >= 0.85: emb[str(dim)] = v

            # vectors__target_over_V_20_S_5_K_03
            # if v >= 0.29: emb[str(dim)] = v
            # vectors__target_over_V_20_S_4_K_03
            # if v >= 0.0007: emb[str(dim)] = v

            # vectors__target_over_V_20_S_6_K_03
            # if v >=0.82: emb[str(dim)] = v

            # vectors__target_over_V_15_S_3_K_03
            # if v >=0.0015: emb[str(dim)] = v

            # vectors__target_over_V_20_S_3_K_03
            # if v >=0.002: emb[str(dim)] = v

            # vectors__target_over_V_20?10_S_6_K_03
            # if v >= 0.75: emb[str(dim)] = v

            # vectors__target_over_V_10_S_5_K_03
            # if v >= 0.85: emb[str(dim)] = v

            # vectors__target_over_V_15_S_5_K_03
            # if v >=0.5: emb[str(dim)] = v

            # vectors__target_over_V_20_S_5_K_03
            # if v >=0.3: emb[str(dim)] = v

            # vectors__target_over_V_1_S_4_K_03
            # if v >=0.001: emb[str(dim)] = v

            # vectors__target_over_V_15_S_4_pmi_1_point_5
            # if v >=1.3: emb[str(dim)] = v

            # vectors__target_over_V_15_S_4
            # if v >= 1.1: emb[str(dim)] = v

            # vectors__target_over_V_2_S_4
            # if v >= 0.7: emb[str(dim)] = v

            # vectors__context_over_V_2_S_5
        # if v >= 1.3: emb[str(dim)] = v

        # vectors__target_over_V_2_S_5
        # if v>=1.2 :emb[str(dim)] = v

        # vectors__context_over_V_2_S_4
        # if v >= 1.2: emb[str(dim)] = v

        # vectors__context_over_V_05_S_3
        # if v >= 1.55: emb[str(dim)] = v

        # vectors__target_over_V_1_S_3
        # if v>=0.5: emb[str(dim)] = v

        # vectors__target_D_1_S_4
        # if v >0.00002: emb[str(dim)] = v

        # target_over_V_1_S_5
        # if v >=1.35: emb[str(dim)] = v

        # context_over_V_1_S_3
        # if v >=1.5: emb[str(dim)] = v

        # __context_D_1_S_6&5&4&3&2
        # if v!=0: emb[str(dim)] = v

        # __context_D_1
        # if v!=0: emb[str(dim)] = v

        # NEW_target_over_V_2
        # if v >=0.7: emb[str(dim)] = v

        # context over_V_fixed_alpha
        # if v >=1.35: emb[str(dim)] = v

        # target_over_V_1_new
        # if v >=1.2: emb[str(dim)] = v

        # context over_V_05_new
        # if v >=1.6: emb[str(dim)] = v

        # target D_05_new
        # if v >=0.0007: emb[str(dim)] = v

        # target over_V_1
        # if v >=1.475: emb[str(dim)] = v

        # target over_V_25
        # if v >=1.1: emb[str(dim)] = v

        # target over_V_25
        # if v >=0.515: emb[str(dim)] = v

        # target_D_8
        # if v >=0.004: emb[str(dim)] = v

        # target_D
        # if v >=0.0004: emb[str(dim)] = v

        # context_D
        # if v>=0.7: emb[str(dim)] = v

        # only non neg2
        # if v>=0.00015: emb[str(dim)] = v1

        # raw data
        # if v>=0.45: emb[str(dim)] = v
        formatted_emb[text[i][0]] = emb
    open(to_file_path, 'w+').write(json.dumps(formatted_emb, indent=4, separators=(',', ': ')))


def save_word_emb_with_name(from_file_path, to_file_path, id_to_name_file):

    file = open(id_to_name_file,"r")
    id_to_name = file.read()
    id_to_name = id_to_name.split("\n")
    for i in range(len(id_to_name)-1):
        id_to_name[i]=id_to_name[i].split(",--,")[1]

    print("part1")
    word_emb = save_word_emb_to_dic(from_file_path)
    formatted_emb = {}
    for i in range(len(word_emb)):
        # print(i)
        emb = {}
        for dim in range(1, len(word_emb[i])):
            v = (word_emb[i][dim])
            v = float(v)
            # vectors___context_D_70_S_3_K_1_point_5
            if v != 0: emb[str(dim)] = v
        formatted_emb[id_to_name[int(word_emb[i][0])]] = emb

    print("part2")
    print formatted_emb
    open(to_file_path, 'w+').write(json.dumps(formatted_emb, indent=4, separators=(',', ': '),ensure_ascii=False))
    print("part3")


#save_word_emb_with_name('../graph/Name_ID.net')
