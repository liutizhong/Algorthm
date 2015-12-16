from collections import defaultdictfrom collections import Counter__author__ = 'liutizhong'salaries_and_tenures = [(83000, 8.7), (88000, 8.1),                        (48000, 0.7), (76000, 6),                        (69000, 6.5), (76000, 7.5),                        (60000, 2.5), (83000, 10),                        (48000, 1.9), (63000, 4.2)]#keys are years,values are lists of the salaries for each tenuresalary_by_tenure = defaultdict(list)for salary, tenure in salaries_and_tenures:    salary_by_tenure[tenure].append(salary)#keys are years,each value is average salary for that tenureaverage_salary_bytenure = {    tenure : sum(salaries) / len(salaries)    for tenure, salaries in salary_by_tenure.items()}print average_salary_bytenure   # result {6.5: 69000, 7.5: 76000, 6: 76000, 10: 83000, 8.1: 88000, 4.2: 63000, 8.7: 83000, 0.7: 48000, 1.9: 48000, 2.5: 60000}def tenure_bucket(tenure):    if tenure < 2:        return "less than two"    elif tenure < 5:        return "between two and five"    else:        return "more than five"#keys are tenure buckets, values are lists of salaries for that bucketsalary_by_tenure_bucket = defaultdict(list)for salary, tenure in salaries_and_tenures:    bucket=tenure_bucket(tenure)    salary_by_tenure_bucket[bucket].append(salary)#keys are tenure buckets,values are average salary for that bucketaverage_salary_bucket={    tenure_bucket: sum(salaries) / len(salaries)    for tenure_bucket, salaries in salary_by_tenure_bucket.items()}print average_salary_bucket  # result {'more than five': 79166, 'between two and five': 61500, 'less than two': 48000}def predict_paid_or_unpaid(years_experience):    if years_experience < 3.0:        return "paid"    elif years_experience <8.5:        return "unpaid"    else:        return "paid"print predict_paid_or_unpaid(2.5)interests = [    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),    (3, "statistics"), (3, "regression"), (3, "probability"),    (4, "machine learning"), (4, "regression"), (4, "decision trees"),    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),    (6, "probability"), (6, "mathematics"), (6, "theory"),    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),    (9, "Java"), (9, "MapReduce"), (9, "Big Data")]words_and_counts=Counter(word                         for user, interest in interests                         for word in interest.lower().split())for word, count in words_and_counts.most_common():    if count > 1:        print word, count