from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    # 모든 조합에 대한 점수를 저장할 딕셔너리
    all_combinations = defaultdict(list)

    # 각 지원자의 정보를 반복하면서 모든 조건의 조합을 만듭니다.
    for applicant in info:
        language, job, career, food, score = applicant.split()
        score = int(score)
        for l in [language, '-']:
            for j in [job, '-']:
                for c in [career, '-']:
                    for f in [food, '-']:
                        # 각 조합의 키를 만들고 점수를 추가합니다.
                        key = (l, j, c, f)
                        all_combinations[key].append(score)

    # 점수를 정렬합니다.
    for scores in all_combinations.values():
        scores.sort()

    # 쿼리를 실행하고 결과를 반환합니다.
    result = []
    for q in query:
        qlang, qjob, qcareer, qfood, qscore = q.replace(' and ', ' ').split()
        qscore = int(qscore)
        key = (qlang, qjob, qcareer, qfood)
        scores = all_combinations[key]
        # bisect_left를 사용하여 qscore 이상의 점수가 시작되는 위치를 찾습니다.
        count = len(scores) - bisect_left(scores, qscore)
        result.append(count)

    return result
