https://github.com/rsennrich/subword-nmt

에 구현된 BPE(byte pair encoding)코드를 좀더 보기 쉽고 실행하기 편하게 재구성 하였습니다.

### 설치 (windows) 
https://github.com/rsennrich/subword-nmt
에 INSTALLATION을 참조하시면 됩니다. 저는 windows, anaconda 환경에서 pip으로 설치 하였습니다.
설치 순서는 아래와 같습니다.

1. anaconda에 pip 설치
conda install pip

2. subword-nmt 설치
pip install subword-nmt


### 실행 
실행 파일은 test_bpe.py입니다.
test_bpe.py를 실행 시키면 corpus.en의 문장을 읽어 vocap.out과 corpus_space.en을 출력합니다.

vocap.out는 corpus.en에서 자주 사용하는 단어들이 저장되어 있으며, corpus_space.en는 vocap.out의 단어를 토대로 합성어를 띄워쓰기한 결과가 저장되어 있습니다.
