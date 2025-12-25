---
layout: post
title: 在Kaggle執行PaddleOCR(百度的OCR library)
date: 2024-05-10 14:06:00
tags:
- kaggle
- paddleocr
---
1.安裝PaddlePaddle

```
!python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
```

2.安裝PaddleOCR whl包

```
!pip install "paddleocr>=2.0.1"
```

3.下載測試用圖片(可自定義)

```
!wget https://paddleocr.bj.bcebos.com/dygraph_v2.1/ppocr_img.zip
```

4.解壓縮圖片

```
!unzip ppocr_img.zip
```

5.執行識別指令

```
!paddleocr --image_dir <圖片路徑> --use_angle_cls true --use_gpu true
```
