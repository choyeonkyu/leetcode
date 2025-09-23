📌 DFS / 백트래킹 문제 유형별 템플릿
1️⃣ 조합 (Combination)

특징: 순서 상관 없음, 같은 원소 여러 번 쓸 수 있는지 여부에 따라 달라짐

문제 예시: Combination Sum, nCr, Subset

def dfs(start, path):
    # 종료 조건
    if 조건:
        ret.append(path[:])   # 정답 저장
        return

    for i in range(start, len(nums)):
        # 선택
        path.append(nums[i])
        dfs(i, path)          # i → 같은 원소 재사용 가능
        # dfs(i+1, path)     # i+1 → 같은 원소 재사용 불가
        path.pop()            # 백트래킹 (원상 복구)

2️⃣ 순열 (Permutation)

특징: 순서 중요, 방문 여부 체크 필요

문제 예시: Permutations, 순열 생성

def dfs(path, used):
    if len(path) == len(nums):
        ret.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True
        dfs(path + [nums[i]], used)
        used[i] = False   # 백트래킹

3️⃣ 부분집합 (Subset / Power Set)

특징: 원소를 선택 or 선택 안 함

문제 예시: Subsets, 부분집합 생성

def dfs(index, path):
    if index == len(nums):
        ret.append(path[:])
        return
    
    # 1. 현재 원소 선택
    dfs(index + 1, path + [nums[index]])
    # 2. 현재 원소 선택하지 않음
    dfs(index + 1, path)

4️⃣ 그래프 탐색 (Graph DFS)

특징: 노드 방문 체크 필수

문제 예시: 경로 탐색, 연결 요소 찾기

def dfs(node, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited)

5️⃣ 경로 찾기 (Path Search)

특징: 시작 ~ 목표까지 경로를 저장해야 함

문제 예시: 모든 경로 찾기, Maze Path

def dfs(node, path):
    if node == target:
        ret.append(path[:])
        return
    
    for nei in graph[node]:
        if nei not in path:  # 사이클 방지
            dfs(nei, path + [nei])

✅ 정리

공통 구조

종료 조건 → 정답 저장 or return

가능한 선택 반복

유효성 검사

선택 → 재귀 호출 → 백트래킹(원상복구)

문제별 차이점

종료 조건 (if ...: return)

탐색 범위 (nums[i:], nums[:i]+nums[i+1:], graph[node])

정답 저장 방식 (ret.append(path), 카운트 증가 등)
