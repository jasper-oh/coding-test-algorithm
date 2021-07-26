# 문제 설명
# 금주의 Q&A
# 난이도: ★★★★★

# 배경
# 험난한 여정을 모두 이겨낸 김토스님은 온보딩세션에서 교육받은 "#무엇이든물어보세요" 슬랙 채널이 어떻게 운영되는지 궁금해졌습니다. 슬랙(Slack)은 토스에서 사용중인 업무용 메신저이고 채널(Channel)은 슬랙 사용자들이 모여있는 채팅방입니다. 토스에는 수백개가 넘는 슬랙 채널이 있고 하루에도 몇천건이 넘는 정보가 쏟아집니다. 그래서 팀원들이 궁금한 정보를 빨리 얻어갈 수 있도록 Q&A 채널인 "#무엇이든물어보세요"를 운영하고 있습니다.

# 이 채널에서는 정기적으로 금주의 Q&A 대회가 열립니다. 대회 기간동안 질문을 업로드하면, 사람들이 본인이 중요하다고 생각하는 질문에 이모티콘을 누르고, 대회기간동안 질문이 획득한 이모티콘의 갯수와 종류에 따라 순위가 정해지는 대회입니다. 예컨대 아래 질문의 경우 획득한 이모티콘의 종류는 4개이고 이모티콘 갯수는 7개 입니다.

# photo.png

# 지금까지 이 대회는 수작업으로 이모티콘 종류와 갯수를 세고 있었다고 합니다. 김토스님은 이런 비효율을 타파하기 위해 대회 순위를 자동으로 출력하는 SQL 쿼리를 작성해드리려 합니다.

# 대회 규칙
# 대회 규칙은 다음과 같습니다.

# 질문의 작성자가 누른 이모티콘은 갯수 및 종류 합계에서 제외됩니다
# 하나의 질문에 대해 한 사람이 여러 종류의 이모티콘을 달 수 있습니다
# 하나의 질문에 대해 한 사람이 한 종류의 이모티콘을 여러번 달 수는 없습니다
# 질문에 달린 이모티콘 갯수의 합이 많을 수록 높은 순위를 가집니다
# 이모티콘 갯수의 합이 동일한 경우, 이모티콘의 종류가 많을수록 더 높은 순위를 가집니다
# 이모티콘 갯수와 종류도 모두 동일한 경우, 먼저 등록된 질문이 더 높은 순위를 가집니다
# 테이블 소개
# 테이블명: toss_users
# 설명: 슬랙을 사용하는 모든 사용자 정보를 담고 있는 테이블

# CREATE TABLE `toss_users`
# (
#     `id`    INT            NOT NULL    AUTO_INCREMENT,
#     `name`  VARCHAR(45)    NULL        COMMENT '사용자 이름',
#      PRIMARY KEY (id)
# );
# 테이블명: toss_questions
# 설명: 사용자가 업로드한 질문 정보 테이블

# CREATE TABLE `toss_questions`
# (
#     `id`          INT             NOT NULL    AUTO_INCREMENT,
#     `content`     VARCHAR(100)    NULL        COMMENT '질문 내용',
#     `uploader`    INT             NULL        COMMENT '질문자 ID',
#     `created_at`  DATETIME            NULL        COMMENT '질문 등록일',
#      PRIMARY KEY (id),
#      FOREIGN KEY (uploader) REFERENCES toss_users (id)
# );
# 테이블명: toss_emoticons
# 설명: 사용자가 질문에 부여할 수 있는 이모티콘 정보 테이블

# CREATE TABLE `toss_emoticons`
# (
#     `id`             INT            NOT NULL    AUTO_INCREMENT,
#     `emoticon_name`  VARCHAR(45)    NULL        COMMENT '이모티콘 이름',
#      PRIMARY KEY (id)
# );
# 테이블명: toss_question_emoticon_votes
# 설명: 사용자가 질문에 부여한 이모티콘 정보 테이블

# CREATE TABLE `toss_question_emoticon_votes`
# (
#     `id`             INT         NOT NULL    AUTO_INCREMENT,
#     `question_id`    INT         NULL        COMMENT '질문 ID',
#     `emoticon_id`    INT         NULL        COMMENT '이모티콘 ID',
#     `click_user_id`  INT         NULL        COMMENT '질문에 이모티콘을 클릭한 사용자의 ID',
#     `created_at`     DATETIME        NULL        COMMENT '질문에 이모티콘이 등록된 날짜',
#      PRIMARY KEY (id),
#      FOREIGN KEY (question_id) REFERENCES toss_questions (id),
#      FOREIGN KEY (emoticon_id) REFERENCES toss_emoticons (id),
#      FOREIGN KEY (click_user_id) REFERENCES toss_users (id)
# );
# 문제
# 이번 대회의 시작일과 종료일은 2021년 8월 23일, 2021년 8월 27일 입니다.
# 위 대회 규칙에 따른 순위가 높은 질문부터 순위가 낮은 질문 순서로 정렬하여 대회 결과를 보여주세요.

# 주의사항
# 대회 시작일 전과 대회 종료일 후에 작성된 질문은 결과에서 제외합니다 (시작일, 종료일 당일은 제외하지 않습니다!)
# 대회 시작일 전과 대회 종료일 후에 달린 이모티콘은 갯수 및 종류 합계에서 제외합니다 (시작일, 종료일 당일은 제외하지 않습니다!)
# 아무 이모티콘도 획득하지 못한 질문 역시 획득 이모티콘 갯수(emoticon_cnt) , 획득 이모티콘 종류 갯수(emoticon_type_cnt) 모두 0으로 결과에 포함되어야 합니다
# 편의상 이모티콘 갯수, 종류 및 등록일이 모두 동일한 질문은 없다고 가정합니다
# 출력
# 질문ID(id), 질문 내용(content), 질문자 이름(user_name), 획득 이모티콘 갯수(emoticon_cnt), 획득 이모티콘 종류 갯수(emoticon_type_cnt), 질문 등록일(created_at) 으로 이루어진 Table

# 출력 예시
# id	content	user_name	emoticon_cnt	emoticon_type_cnt	created_at
# 1	공용우산은 어디에 있나요?	김경섭	10	5	2021-08-24 00:00:00
# 2	코어밸류는 무엇인가요?	한은환	10	3	2021-08-25 00:00:00
# 3	공사가 예정되어있나요?	강재연	10	3	2021-08-27 00:00:00
# 4	화장실은 어디에 있나요?	오지섭	7	7
