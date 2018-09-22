import operator


def save_word_emb_to_matrix(filename):
    file = open(filename, "r")
    text = file.read()
    text = text.split("\n")[0:-1]
    text[0] = text[0].split(' ')
    print(text[0])
    for i in range(1, len(text)):
        text[i] = text[i].split(" ")[0:-1]
    file.close()
    print("text splitted")
    return text[2:]


def get_sorted_summed_up_dic(emb_matrix, id_to_name_file):
    file = open(id_to_name_file, "r")
    id_to_name = file.read()
    id_to_name = id_to_name.split("\n")
    for i in range(len(id_to_name)):
        id_to_name[i] = id_to_name[i].split(",")[1]
    emb_sumed_dic = {}
    summed = 0
    for i in range(len(emb_matrix)):
        summed = 0
        for j in range(1, len(emb_matrix[i])):
            summed += float(emb_matrix[i][j])
        emb_sumed_dic[id_to_name[int(emb_matrix[i][0]) - 1]] = summed
    emb_sumed_dic = sorted(emb_sumed_dic.items(), key=operator.itemgetter(1),reverse=True)
    return emb_sumed_dic


def save_emb_to_file(emb_summed_up_dic, filename):
    text=""
    for i in emb_summed_up_dic:
        text +=i[0]+","+str(i[1])+"\n"
    open(filename, 'w+').write(text)



emb_matrix = save_word_emb_to_matrix("../emb/dblp_coauthor.emb")
emb_summed_up_dic = get_sorted_summed_up_dic(emb_matrix, "../graph/dblp_coauthor_id_name.net")
save_emb_to_file(emb_summed_up_dic, "../emb/dblp_coauthor_summed_up.emb")
