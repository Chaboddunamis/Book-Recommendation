#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class get_similarities():
    def get_cosine_similarity(self, userIdA, userIdB):
        def check_similarity(text1, text2):
            text1 = text_A
            text_2 = text_B
            vect1 = text_to_vector(text1)
            vect2 = text_to_vector(text2)
            cosine = calculate_cosine(vect1, vect2)
            return cosine
        
        def calculate_cosine(vect1, vect2):
            joint_var = set(vect1.keys()) & set(vect2.keys())
            numerator = sum([vect1[x] * vect2[x] for x in joint_var])
            sum1 = sum([vect1[x] ** 2 for x in list(vect1.keys())])
            sum2 = sum([vect2[x] ** 2 for x in list(vect2.keys())])
            denominator = math.sqrt(sum1) * math.sqrt(sum2)
            if not denominator:
                return 0.0
            else:
                return float(numerator) / denominator

        WORD = re.compile(r"\w+")
        def text_to_vector(text):
            words = WORD.findall(text)
            return Counter(words)


        def get_strings(df):
            checklist = df.values.tolist()
            checkstring = ' '.join([str(item) for item in checklist])
            purestring = " ".join(re.split("[^a-zA-Z]*", checkstring))
            finalstring = purestring.replace("n a n","")
            return finalstring



        A = user_preferences[userIdA]
        B = user_preferences[userIdB]
        A_df = pd.DataFrame(A)
        B_df = pd.DataFrame(B)
        text_A = get_strings(A_df)
        text_B = get_strings(B_df)
        similarities = check_similarity(text_A, text_B)
        sim_score = []
        sim_score.append(similarities)

        return sim_score


    def pearson_correlation(self, userIdA, userIdB):
        a = user_preferences[userIdA]
        b = user_preferences[userIdB]
        A_Df = pd.DataFrame(a)
        B_Df = pd.DataFrame(b)
        ISBN = A_Df.columns.values[0]
        ISBN2 = B_Df.columns.values[0]
        A_Df[ISBN] = A_Df[ISBN].astype('category').cat.codes
        B_Df[ISBN2] = B_Df[ISBN2].astype('category').cat.codes
        Common_Df = pd.concat([A_Df, B_Df], axis=1)
        return Common_Df.corr(method='pearson')
    
    def Spearman_correlation(self, userIdA, userIdB):
        return Common_Df.corr(method='spearman')


    def hamming_distance(self, userIdA, userIdB):
        A = user_preferences[userIdA]
        B = user_preferences[userIdB]
        A_df = pd.DataFrame(A)
        B_df = pd.DataFrame(B)
        text_A = get_strings(A_df)
        text_B = get_strings(B_df)
        return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(text_A, text_B))))

    def get_minkowski_distance(self, userIdA, userIdB):
        c = user_preferences[userIdA]
        d = user_preferences[userIdB]
        C_Df = pd.DataFrame(c)
        D_Df = pd.DataFrame(d)
        isbn = C_Df.columns.values[0]
        isbn2 = D_Df.columns.values[0]
        C_Df[isbn] = C_Df[isbn].astype('category').cat.codes
        D_Df[isbn2] = D_Df[isbn2].astype('category').cat.codes
        C_arr = np.array(C_Df)
        D_arr = np.array(D_Df)
        def nth_root(value, n_root):
            root_value = 1/float(n_root)
            return round (Decimal(value) ** Decimal(root_value),3)
        def minkowski_distance(x,y,p_value):
            return nth_root(sum(pow(abs(k-j),p_value) for k,j in zip(x, y)),p_value)
        return minkowski_distance(C_arr, D_arr, 3)

    def Euclidean_distance(self, userIdA, userIdB):
        dist = distance.euclidean(C_arr, D_arr)
        return dist

    def Chebyshev_distance(self, userIdA,userIdB):
        distnc = distance.chebyshev(C_arr, D_arr)
        return distnc


# In[ ]:


if __name__ == '__main__':
    dataobj = get_similarities()
    cos_score = dataobj.get_cosine_similarity(3194,3197)
    pearson = dataobj.pearson_correlation(3194, 3197)
    spearman = dataobj.Spearman_correlation(3194, 3197)
    hamming = dataobj.hamming_distance(3194, 3197)
    minkowski = dataobj.get_minkowski_distance(3194, 3197)
    Euclidean = dataobj.Euclidean_distance(3194, 3197)
    Chebyshev = dataobj.Chebyshev_distance(3194, 3197)

