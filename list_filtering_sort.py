#다음과 같은 DB가 있을 때, 이중 grade가 a인 데이터중 평균이 높은 3명을 리턴.
DB = [{'id' : 1, 'grade' : '1', 'name' : '홍길동', 'kor' : 94, 'eng' : 81, 'math' : 75},
      {'id' : 2, 'grade' : '3', 'name' : '김철수', 'kor' : 84, 'eng' : 91, 'math' : 85},
      {'id' : 3, 'grade' : '2', 'name' : '김연우', 'kor' : 74, 'eng' : 71, 'math' : 95},
      {'id' : 4, 'grade' : '1', 'name' : '유재석', 'kor' : 97, 'eng' : 96, 'math' : 85},
      {'id' : 5, 'grade' : '3', 'name' : '유도혁', 'kor' : 77, 'eng' : 76, 'math' : 65},
      {'id' : 6, 'grade' : '2', 'name' : '차주한', 'kor' : 87, 'eng' : 86, 'math' : 55},
      {'id' : 7, 'grade' : '2', 'name' : '이승기', 'kor' : 91, 'eng' : 92, 'math' : 75},
      {'id' : 8, 'grade' : '1', 'name' : '강호동', 'kor' : 71, 'eng' : 72, 'math' : 91},
      {'id' : 9, 'grade' : '2', 'name' : '엄준식', 'kor' : 81, 'eng' : 82, 'math' : 78}]

def solution(DB):
      a = '2'
      highest = []
      temp = []
      #data 에서 grade가 2인것만 필터링 후 temp에 저장
      for data in DB:
            if data['grade'] == '2':
                  temp.append(data)

      #필터링한 temp를 람다식으로 평균값을 구한 뒤, 그 값을 키로 잡고 내림차순으로 answer에 저장
      highest = sorted(temp, key=lambda x: ((x['kor']+x['eng']+x['math'])/3), reverse=True)
      
      return highest[0:3]
print(solution(DB))
