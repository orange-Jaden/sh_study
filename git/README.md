# git 이란
- Git은 현재 가장 유명한 **분산 버전 관리 시스템(DVCS)**입니다.
- Git은 프로그램의 
    - **버전**을 관리하고, 
    - 코드의 변화를 **추적**하고, 
    - **협업**을 효율적으로 하기 위해서 사용합니다.
- Git은 파일 단위로 내용의 변화를 추적합니다.
    - 서로 다른 branch에 의해 동일한 파일이 수정되었을 때 충돌이 발생할 수 있습니다.

# Git 기본 용어
- **Repository** : 프로젝트를 저장하는 곳
- **Stage** : Commit을 하기 위해 파일을 선택하는 것
- **Commit** : 변경 사항을 저장하는 것
- **Clone** : 원격 저장소를 복사하는 것
- **Push** : 원격 저장소에 Commit을 업로드하는 것
- **Pull** : 원격 저장소에서 변경 사항을 가져오는 것
- **Switch** : 특정 Branch로 이동하는 것
- **Checkout** : Branch를 이동하거나, 파일을 되돌리는 것
- **Branch** : 각각의 Commit을 연결하는 것 (가지)
- **Merge** : Branch를 합치는 것
- **Pull Request** : Branch를 합치는 것을 요청하는 것
- **Conflict** : Merge를 할 때, 같은 파일의 같은 부분을 수정했을 때 발생하는 충돌
- **Rebase** : Commit을 새로 정렬하는 것

- What is difference between git pull and git fetch?
    - git pull = git fetch + git merge
    - git fetch : 원격 저장소의 변경 사항을 가져오는 것
    - git merge : 가져온 변경 사항을 현재 Branch에 합치는 것

- What is difference between switch and checkout?
    - git switch : Branch를 이동하는 것
    - git checkout : Branch를 이동하거나, 파일을 되돌리는 것

<br/>

# Git 시작하기

## Git 설정하기

- Git을 사용하기 위해서는 가장 먼저 사용자 정보를 설정해야 합니다.
    - 사용자 이름 설정
        - `git config --global user.name "사용자 이름"`
    - 사용자 이메일 설정
        - `git config --global user.email "사용자 이메일"`
    - 설정 확인
        - `git config --global --list`
- 참고: 해당 폴더에서만 사용자 정보를 설정하고 싶다면 `--global`을 빼면 됩니다.
    - `git config user.name "사용자 이름"`
    - `git config user.email "사용자 이메일"`

<br/>

## Git 초기화 하기 

- Git을 사용하기 위해서는 가장 먼저 해당 폴더를 Git으로 관리하겠다고 초기화를 해야 합니다.
    - `git init`

> `.git` 폴더가 생성되면서 Git으로 관리되는 폴더가 됩니다.

<br/>

## 파일 추적하기
- 파일 생성하기 
- 파일 상태 확인하기
    - `git status`
- 파일 추적하기
    - `git add 파일명`
    - `git add .` 또는 `git add -A`: 현재 폴더의 모든 파일을 추적
    - `git add -A` : 현재 폴더의 모든 파일을 추적
- 파일 추적 취소하기
    - `git rm --cached 파일명`
    - `git rm -r --cached .` : 현재 폴더의 모든 파일 추적 취소
- 파일 추적 저장하기
    - `git commit -m "커밋 메시지"`
- 파일 추적 취소하기
    - `git reset HEAD 파일명`
    - `git reset HEAD .` : 현재 폴더의 모든 파일 추적 취소
    
<br/>


# GUI로 git 제어하기


# Github 계정 만들기


# 나만의 홈페이지 만들기

