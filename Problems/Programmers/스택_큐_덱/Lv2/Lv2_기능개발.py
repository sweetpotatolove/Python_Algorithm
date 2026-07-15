# 프로그래머스 Lv2. 기능개발
# 분류: 스택/큐
# 핵심: 각 기능마다 완료까지 필요한 일수를 계산하고, 앞 기능이 배포될 때 함께 배포되는 기능의 수를 세어 나간다.
# 시간 복잡도: O(n)
# 공간 복잡도: O(n)


# 1. 문제 이해
# - 입력: 작업 진도(progresses)와 작업 속도(speeds) 배열
# - 출력: 각 배포마다 함께 배포되는 기능의 개수를 담은 배열
# - 구해야 하는 것: 각 기능이 완료되는 날짜를 계산하고, 앞 기능이 배포되는 날과 같은 날에 배포 가능한 기능의 개수를 차례대로 반환하는 함수


# 2. 아이디어
# - 각 기능이 완료되기까지 필요한 일수는 ceil((100 - progress) / speed)로 계산할 수 있다.
# - 배포는 하루에 한 번만 이루어지므로, 앞 기능의 완료일과 비교해 같은 날에 배포 가능한 기능을 묶어서 세면 된다.
# - 자료구조: 리스트 (days, answer)


# 3. 풀이 계획
# 1) 각 기능이 완료되는 데 필요한 일수를 days에 계산한다.
# 2) 첫 번째 기능의 완료일을 기준값으로 설정한다.
# 3) 이후 기능들을 순회하며 기준 완료일보다 같거나 빠르면 같은 배포 그룹에 포함하고, 늦으면 새 그룹으로 분리한다.
# 4) 각 그룹의 개수를 answer에 담아 반환한다.


def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        
        day = ((100 - progress) + (speed - 1)) // speed
        """
        정수 올림 공식
        ceil(a / b) 
            = (a + b - 1) // b
        """
        days.append(day)
    
    # 첫 번째 기능의 완료일 -> 배포 시작일
    deploy_day = days[0]
    count = 1

    for d in days[1:]:
        # 앞 배포보다 빠르면 +1
        if d <= deploy_day:   
            count += 1
        else:
            # 새로 배포
            answer.append(count)
            deploy_day = d
            count = 1
    
    # 마지막 배포 추가
    answer.append(count)

    return answer