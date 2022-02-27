"""
Chapter 4
나만의 패키지 만들기
Keyword - png to gif, pil, image

"""
"""
패키지 작성
-> GIF 이미지 변환기 -> 패키지 호출 형태로 작성

"""

# py_ad_4_3 : 완성된 패키지 임포트
from py_ad_4_3 import GifConverter as gfc

# 클래스
c = gfc("../project/images/*.png", "../project/image_out/result.gif")

# 실행
c.convert_gif()


"""
패키지 배포 순서(PyPI)

1. htts://pypi.org에서 회원가입!
2. 프로젝트 구조 확인
3. __init__.py
4. 프로젝트 Root 필수 파일 작성
    - README.md
    - .gitignore
    - setup.py
    - setup.cfg(optional)
    - LICENSE
    - MANIFEST.in
5. pip install setuptools wheel 설치 후 빌드 업 -> 설치판 생성
    -> 설치 1: python -m pip install --upgrade setuptools wheel
    -> 설치 2: python -m pip install --user --upgrade setuptools wheel
    -> 빌드 : python setup.py sdist bdist_wheel
    
6. PyPI 배포
    -> 설치: pip install twine
    -> 업로드: python -m twine upload dist/*
7. 설치확인(pip install pygifconv_imfk)
    from pygifconv_imfk.gif_converter import GifConverter as Alias
"""