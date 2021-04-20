# GitPlayground
깃 관련 기능을 테스트해보고 경험하기 위한 Repo

release 0.1.0 start

deploy dev server

QA

bug fixed

release 0.1.0 completed!!

## git init
깃 초기화
## .gitignore
- file 
- directory
## git add 
- **git add --all** </br>변경한 모든 파일 추가
## git commit
- **git commit -am "..."**</br>추가한 파일을 커밋 ( "" 안에는 원하는 대로 적으면 된다, -am에서 a는 연결된 repository인데 빼도 무관)
- **git commit --amend**</br>커밋 메세지 수정

## git remote
- **git remote add origin \<git-remote-url\>** </br>해당 url로 원격지 설정

## git push
- **git push -u origin master**  </br>원격지 메인 줄기에다가 업로드
- **git push -fu origin master** </br>force 옵션, 원격지 메인 줄기에 강제로 업로드
</br>**origin master** -> origin : 원격지, master: 브랜치 네임

## git log
내가 했던 명령들 기록
- **git log --graph --oneline**

## git reset
- **git reset HEAD** </br> Staging 된 파일들을 취소한다 
- **git reset --soft HEAD~** </br> 맨 위 커밋을 취소한다
- **git reset --hard HEAD~** </br> 맨 위 커밋을 취소하고 소스코드까지 날린다 (주의필요)
- mixed
<br/> history가 없어진다
## git revert
history가 쌓임!
## git branch
- **git branch** </br> 로컬의 브랜치 목록 확인
- **git branch -r** </br> 원격지의 브랜치 목록 확인
- **git branch -a** </br> local / remote 양쪽 브랜치 모두 확인
- **git branch -d \<branch name\>** </br> 로컬에서 브랜치 삭제
- **git push --delete origin \<branch-name\>** </br> 원격지에서 브랜치 삭제
- **git checkout -t origin/\<branch-name\>** </br> 서버의 특정 브랜치 가져오기

- **git branch \<branch-name\>** </br> 해당 이름으로 브랜치 생성
- **git checkout \<branch-name\>** </br> 해당 이름 브랜치로 전환

- **git diff \<branch-name\>** </br> (현재 브랜치와) 다른 브랜치와 다른 소스코드 비교
- **git diff \<branch-name\> <file-name>** </br> (현재 브랜치와) 다른 브랜치의 특정 파일 소스 비교
- **git checkout -p \<branch-name\>** </br>(현재 브랜치에서) 해당 브랜치네임의 소스 업데이트
- **git checkout -p \<branch-name\> <file-name>** </br>(현재 브랜치에서) 해당 브랜치네임의 특정 파일 업데이트

## git pull
- **git pull** </br> master 브랜치에서 pull (git pull하면 기본이 항상 master)
- **git pull origin \<branch-name\>** </br> 원격지의 해당 브랜치 네임을 pull
- **git push origin \<branch-name\>** </br> 원격지의 해당 브랜치에 push

## git rebase
- **git rebase -i HEAD~2** </br> HEAD(맨앞 커밋)에서 2번째 커밋까지 합치겠다 (interactive 모드로)