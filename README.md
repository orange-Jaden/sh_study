# 모듈 설치하기
```bash
pip install pygame
```

# 모듈 가져오기 
```python
import pygame
from pygame.locals import *

pygame.init()

pygame.quit()
```

# 창 설정
```python
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
```

# 게임 실행 루틴

```python
run = True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
```

# 백그라운드 이미지 설정

- 이미지 불러오기
    `bg = pygame.image.load('img/bg.png')`

- 이미지 그리기 

- 이미지 움직이기 
    ```python
    ```
