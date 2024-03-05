# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering is less affected by outliers because it builds clusters step by step, incorporating points based on proximity, whereas k-means is more sensitive to outliers as they can significantly influence the position of centroids"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Agglomerative hierarchical clustering produces the same clustering for a given dataset because it follows a deterministic process of merging clusters based on a linkage criterion, whereas k-means can produce different results due to random initialization of centroids."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = " While k-means is generally more efficient in terms of time and memory compared to agglomerative hierarchical clustering, it is not necessarily the most efficient clustering algorithm possible as efficiency can vary based on the dataset and context."

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "The SSE (Sum of Squared Errors) within the cluster is likely to decrease because the split is made to optimize the assignment of points to the nearest centroid, which should reduce the overall error within each new cluster."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = " Decreasing SSE indicates that points are closer to their respective cluster centroids, which implies an increase in cohesion as the internal cluster similarity is improving."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An increase in SSB indicates that clusters are further apart from each other, which implies an increase in separation as the distinctiveness between clusters is enhancing."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = " Improving cohesion by minimizing SSE within clusters does not necessarily mean that the separation (SSB) will improve, as these two metrics can move independently depending on the distribution and allocation of points in the clusters."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The sum of SSE (within-cluster variation) and BSS (between-cluster variation) is not constant in k-means clustering. As clusters change, both SSE and BSS can vary, and their sum is not fixed."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "An increase in cohesion (decrease in SSE) does not necessarily lead to an increase in separation. These two metrics can move independently; improving cohesion does not guarantee an increase in separation."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = False

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "K-means assigns points to the closest centroid.Points on the borders of the shaded circles (Figure a) might be closer to the opposite centroid compared to the one in the center of their shaded area.During iterations, these borderline points could be assigned to the wrong cluster, causing the centroids to shift away from the exact center of the circles.Consequently, after k-means finishes, each shaded circle might not necessarily have a centroid at its precise center."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Although the initial centroids in Figure (b) seem ideal for separation, k-means doesn't guarantee perfect cluster isolation.Points on the edges of the shaded regions could still be closer to the opposite centroid.This could lead to points from one shaded area being assigned to the cluster with the centroid in the other shaded region.As a result, clusters might contain points from both shaded areas, violating the expectation of complete separation."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "In Figure (c), the initial centroids are close to each other and near a data point with a value of 25.During iterations, this data point could be assigned to one of the centroids.If assigned to one, the other centroid might be left with no assigned points.This scenario leads to one empty cluster in the final k-means output."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = '4*R*R'

    # type: a string that evaluates to a float
    answers["(b) SSE"] = '(4*R*R)+(4*a*a)+(4*b*b)'

    # type: a string that evaluates to a float
    answers["(c) SSE"] = '5*R*R'

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 1 or 2

    # type: int
    answers["(a) Circle (c)"] = 1 or 2

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "since initislly b contain 3 but due to more points in c 1 or 2 may be transferred to c"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 0 or 1

    # type: int
    answers["(b) Circle (c)"] = 1 or 2

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "beacause c has vast no of points it may attract the centroids in b"

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "since a and b are far from c and a and b has same poppulation so there is no change"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set({'Group A' , 'Group B'})

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In single-link clustering, the focus is on the shortest link between clusters, and the closest pair of points appears to be between Group A and Group B."

    # type: set
    answers["(b)"] = set({'Group A', 'Group C'})

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The farthest points between Group A and Group C are closer than the farthest points between any other pair of groups, which is the criterion for merging in complete-link clustering."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set({'B','C','E','F','I','J','L','M'})

    # type: set
    answers["(a) boundary"] = set({'D','G'})

    # type: set
    answers["(a) noise"] = set({'A','H'})

    # type: set
    answers["(b) cluster 1"] = set({'B','C','D','E','F','G'})

    # type: set
    answers["(b) cluster 2"] = set({'I','J','L','M'})

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set({'A','B','C','D','E','F','G','H','I','J','L','M'})

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set({'A','B','C','D','E','F','G','H','I','J','L','M'})

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 is notable for its diverse representation across various categories such as Forest, Farm, Shrubland, and Urban. This diversity results in high entropy within the cluster, as there is no single dominant category, rendering its composition the most unpredictable among all the clusters."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "since all are consider in small quantities and water is considered in larger quantity"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The diagonal entries are mostly blue, suggesting shorter distances within clusters, which implies compact and closely-knit clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Non-diagonal entries exhibit notable red regions, indicating greater distances between clusters, consistent with the clear separation observed in Dataset Z."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"
    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The diagonal displays a range of colors because of the diverse composition of clusters, illustrating the intricate mingling of various cluster points."
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Non-diagonal sections display a checkered pattern, suggesting diverse distances between clusters, reflecting the scattered and mixed organization found in Dataset X."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"
    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The diagonal sections uniformly appear blue, indicating minimal distances within clusters, which corresponds to the condensed and distinct clustering evident in Dataset Y."
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Non-diagonal regions sharply differ from diagonal ones, revealing evident red blocks that signal the presence of distinct and clearly separated clusters observed in Dataset Y."


    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "all clusters has different kind of distances"

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "cluster is cohesive and 2 two clusters A,C sre closer to it and D is farther"

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "cluster is cohesive similar to above"

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "closest to C followed by B fartheest from A"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Overlapping', 'Partial']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'Complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'Overlapping', 'Partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "not all cs students take data mining class"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can only be used for (b) since the mouth, nose, and eyes in (b) have points that are considerably closer together than the points that separate them, making DBSCAN able to discriminate between these locations. Since the noise in (a) is significantly denser than the interest patterns, DBSCAN will exclude the mouth,eyes,and nose."

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since the lower density points would also be included, K-means can be used to (b) as long as the number of clusters is set to 4. Regarding (a), K-means is ineffective."

    # type: string
    answers["(c)"] = "we should take the reciprocal of the density"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
