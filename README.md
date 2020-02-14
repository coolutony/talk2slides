Talk 2 Slides
============
Talk 2 Slides는 사용자의 음성으로부터 이에 대응되는 프레젠테이션 슬라이드를 제공하는 서비스입니다.
- 음성을 인식해 텍스트로 변환하는 과정에서 NAVER의 CSR(Clova Speech Recognition) API을 이용하였습니다.
- 추출된 텍스트를 바탕으로 이미지를 얻는 과정에서 NAVER의 Image Search REST API를 이용하였습니다.
- 생성된 텍스트와 이미지를 포함한 markdown 파일로부터 슬라이드를 생성하는 generator로 DarkSlide를 활용하였습니다. 

Dependency
-
- Django==3.0.3
- requests==2.22.0
- konlpy==0.5.2
- nltk==3.4.5
- numpy==1.18.1
- pandas==1.0.1
- scikit_learn==0.22.1
- scipy==1.4.1
- spacy==2.2.3

절차
-
1. 사용자가 발표하려는 내용을 음성으로 녹음합니다.
2. 음성이 NAVER의 CSR을 거쳐 텍스트로 변환됩니다.
3. 변환된 텍스트를 NLP를 이용해 key word를 추출합니다.
4. 추출된 key word를 바탕으로 NAVER Image Search REST API를 이용해 관련 이미지를 추출합니다.
5. 추출된 key word 및 이미지를 markdown 파일의 형태로 저장합니다.
6. DarkSlide generator를 이용해 위의 markdown file을 슬라이드로 변환하면 원하는 결과를 얻습니다. 

팀명: 누뗄라
-
- 팀원: 김상엽, 김선욱, 박수형, 이용진

