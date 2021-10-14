# 課題

## 禁則事項
`test_main.py` を修正した場合、不正行為があったと見なされ本講義を含む今学期の全ての単位を失う可能性があります。

## 内容
1. DxD正則行列AとD次元ベクトルxを入力として、  <img src="https://latex.codecogs.com/gif.latex?\sqrt{x^\top&space;A^{-1}&space;x}" /> を出力する関数 `quadratic` を完成させよ。ただし A, x 共に numpy.array として与えられるとする。
1. DxD対称行列Aを入力として、Aの第二固有値（固有値の中で二番目に大きいもの）を出力する関数 `second_eig` を完成させよ。
1. DxD行列A、D次元ベクトルx、自然数kを入力として、
<div align="center">
<img src="https://latex.codecogs.com/gif.latex?\begin{align}&space;\nonumber&space;v_1&=\dfrac{A^k&space;x}{\|A^k&space;x\|}&space;\\&space;\nonumber&space;\lambda_1&space;&=&space;v_1^\top&space;A&space;v_1&space;\end{align}" /> 
</div>
で定義される<img src="https://latex.codecogs.com/gif.latex?\lambda_1" />を出力する関数 `power_iter` を完成させよ。

## 実行環境の作り方
`pip3 install -r requirements.txt`

## 実行コマンド
`python3 test_main.py`
